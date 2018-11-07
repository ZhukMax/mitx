import pylab as plt

mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range(0, 30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)

plt.figure('lin')
plt.title('Linear')
plt.plot(mySamples, myLinear)

plt.figure('quad')
plt.title('Quadratic')
plt.plot(mySamples, myQuadratic)

plt.figure('cubic')
plt.title('Cubic')
plt.plot(mySamples, myCubic)

plt.figure('exp')
plt.title('Exponential')
plt.plot(mySamples, myExponential)

plt.figure('cubic expo')
plt.title('Cubic vs. Exponential')
plt.plot(mySamples, myCubic, 'g^', label='Cubic', linewidth=4.0)
plt.plot(mySamples, myExponential, 'r--', label='Exponential', linewidth=5.0)
plt.legend()
