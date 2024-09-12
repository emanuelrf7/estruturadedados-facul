from math import log
import numpy as np
import matplotlib.pyplot as plt

n = np.linspace(1, 10, 100)
# print(n)
# print(np.ones(2))
# print(np.ones(3))
labels = [
    "Constant",
    "Logarithmic",
    "Linear",
    "Log linear",
    "Quadratic",
    "Cubic",
    "Exponential",
]
big_o = [np.ones(n.shape), np.log(n), n, n * np.log(n), n ** 2, n ** 3, 2 ** n]
# print(np.ones(n.shape))
# print(np.log(n))

plt.figure(figsize=(10, 8))
plt.ylim(0, 100)
for i in range(len(big_o)):
    plt.plot(n, big_o[i], label=labels[i])
plt.legend()
plt.ylabel("Runtime")
plt.xlabel("n")

lista = [1, 2, 3, 4, 5]
def constant(n):
    print(n[0])
constant(lista)

def linear(n):
    for i in n:
        print(i)
linear(lista)

def quadratic(n):
    for i in n:
        for j in n:
            print(i, j)
        print("---")
quadratic(lista)