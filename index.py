from Food import Food
import random


def build_large_menu(num_items, max_val, max_cost):
    items = []
    for i in range(num_items):
        items.append(Food(str(i), random.randint(1, max_val), random.randint(1, max_cost)))
    return items


def build_menu(names, values, calories):
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i]))
    return menu


def greedy(items, max_cost, key_func):
    items_copy = sorted(items, key=key_func, reverse=True)
    result = []
    total_value, total_cost = 0.0, 0.0

    for i in range(len(items_copy)):
        if (total_cost + items_copy[i].get_cost()) <= max_cost:
            result.append(items_copy[i])
            total_cost += items_copy[i].get_cost()
            total_value += items_copy[i].get_value()

    return result, total_value


def test_greedy(items, constrains, key_func):
    taken, val = greedy(items, constrains, key_func)
    print('Total value of items taken =', val)

    for item in taken:
        print(' ', item)


def test_greedys(foods, max_units):
    print('Use greedy by value to allocate', max_units, 'calories')
    test_greedy(foods, max_units, Food.get_value)

    print('\nUse greedy by cost to allocate', max_units, 'calories')
    test_greedy(foods, max_units, lambda x: 1/Food.get_cost(x))

    print('\nUse greedy by density to allocate', max_units, 'calories')
    test_greedy(foods, max_units, Food.density)


def max_val(to_consider, avail):
    if to_consider == [] or avail == 0:
        result = 0, ()
    elif to_consider[0].get_cost() > avail:
        result = max_val(to_consider[1:], avail)
    else:
        next_item = to_consider[0]
        with_val, with_to_take = max_val(to_consider[1:], avail - next_item.get_cost())
        with_val += next_item.get_value()
        without_val, without_to_take = max_val(to_consider[1:], avail)

        if with_val > without_val:
            result = with_val, with_to_take + (next_item,)
        else:
            result = without_val, without_to_take

    return result


def fast_max_val(to_consider, avail, memo=None):
    if memo is None:
        memo = {}

    if (len(to_consider), avail) in memo:
        result = memo[(len(to_consider), avail)]
    elif to_consider == [] or avail == 0:
        result = 0, ()
    elif to_consider[0].get_cost() > avail:
        result = fast_max_val(to_consider[1:], avail, memo)
    else:
        next_item = to_consider[0]
        with_val, with_to_take = fast_max_val(to_consider[1:], avail - next_item.get_cost(), memo)
        with_val += next_item.get_value()
        without_val, without_to_take = fast_max_val(to_consider[1:], avail, memo)

        if with_val > without_val:
            result = with_val, with_to_take + (next_item,)
        else:
            result = without_val, without_to_take

    memo[(len(to_consider), avail)] = result
    return result


def test_max_val(foods, max_units, alg, print_items=True):
    print('Use search tree to allocate', max_units, 'calories')
    val, taken = alg(foods, max_units)

    if print_items:
        print('Total value of items taken =', val)
        for item in taken:
            print('    ', item)

    print('\n')


# names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola', 'apple', 'donut', 'cake']
# values = [89, 90, 95, 100, 90, 79, 50, 10]
# calories = [123, 154, 258, 354, 365, 150, 95, 195]
# foods = build_menu(names, values, calories)
# test_greedys(foods, 750)
# print(' ')
# test_max_val(foods, 750)

for num in (5, 10, 15, 20, 25, 30, 35, 40, 45):
    print('Try a menu with', num, 'items')
    items = build_large_menu(num, 90, 250)
    test_max_val(items, 750, fast_max_val, False)
