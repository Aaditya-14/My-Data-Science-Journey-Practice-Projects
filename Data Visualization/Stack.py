import matplotlib.pyplot as plt
days = [1, 2, 3, 4, 5, 6, 7]  # Days of the week
studying = [3, 4, 3, 5, 4, 3, 4]
playing = [2, 2, 1, 1, 2, 3, 2]
watching_tv = [2, 1, 2, 2, 1, 1, 1]
sleeping = [5, 5, 6, 5, 6, 5, 5]

label=["Study","Play","TV","Sleep"]
color=["Red","Green","Pink","Yellow"]

plt.stackplot(days,studying,playing,watching_tv,sleeping,labels=label,colors=color)
plt.legend(loc='upper left')
plt.title("Sedule pattern")
plt.ylabel("Tasks")
plt.xlabel("Days")
plt.grid("True")
plt.show()