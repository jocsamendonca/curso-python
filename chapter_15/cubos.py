import matplotlib.pyplot as plt

numeros = range(1, 5001)
cubos = [x**3 for x in numeros]

plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots()
ax.scatter(numeros, cubos, c=cubos, cmap=plt.cm.Blues, s=30)
ax.plot(numeros, cubos, linewidth=3)
ax.set_title("Cubos", fontsize=24)
ax.set_xlabel("Valores", fontsize=14)
ax.set_ylabel("Cubos", fontsize=14)

ax.axis([1, 5500, 0, 130_000_000_000])
ax.ticklabel_format(style='plain')

plt.show()