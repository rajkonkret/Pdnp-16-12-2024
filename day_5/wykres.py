import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 5, 8, 9, 10]

plt.plot(x, y, color="red")
plt.title("Wykres liniowy")
plt.xlabel("Oś X")
plt.ylabel("Oś y")

plt.savefig('wykres.png')
plt.savefig('wykres.pdf')
plt.show()
