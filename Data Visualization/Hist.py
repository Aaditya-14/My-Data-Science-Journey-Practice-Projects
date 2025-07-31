import matplotlib.pyplot as plt
Marks = [
    34, 28, 36, 45, 27, 27, 45, 37, 25, 35,
    25, 25, 32, 10, 12, 24, 19, 33, 20, 15,
    44, 27, 30, 15, 24, 31, 18, 33, 23, 27,
    23, 48, 29, 19, 38, 17, 32, 10, 16, 31,
    37, 31, 28, 26, 15, 22, 25, 40, 33, 12,
    33, 26, 23, 36, 40, 39, 21, 26, 33, 39,
    25, 28, 18, 18, 38, 43, 29, 40, 33, 23,
    33, 45, 29, 45, 3, 38, 30, 27, 30, 10,
    27, 33, 44, 24, 21, 24, 39, 33, 24, 35,
    30, 39, 22, 26, 26, 15, 32, 32, 30, 27
]
bins = [10, 20, 30, 40, 50, 60, 70]
plt.hist(Marks,bins, edgecolor="Black",)
plt.xlabel("Bins")
plt.ylabel("Marks")
plt.title("Marks distribution in historogram")
plt.axvline(25,color="Red",linestyle="--", linewidth=3, label="Highest Marks")
plt.grid(True,linestyle="--", alpha=0.7)
plt.legend()
plt.show()