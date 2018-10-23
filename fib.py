def fast_fib(n, memo=None):
    if memo is None:
        memo = {}

    if n == 0 or n == 1:
        return 1

    try:
        return memo[n]
    except KeyError:
        result = fast_fib(n - 1, memo) + fast_fib(n - 2, memo)
        memo[n] = result
        return result


for i in range(121):
    print('fib('+str(i)+') =', fast_fib(i))
