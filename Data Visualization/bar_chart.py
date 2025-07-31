import matplotlib.pyplot as plt
import numpy as np
years = [1990, 1992, 1994, 1996, 1998, 2000, 2003, 2005, 2007, 2010]

sachin = [500, 700, 1100, 1500, 1800, 1200, 1700, 1300, 900, 1500]
sehwag = [10, 200, 900, 1400, 1600, 1800, 1500, 1100, 800, 20]
kohli  = [40, 40, 500, 800, 1100, 1300, 1500, 1800, 1900, 2100]

x=np.arange(len(years))
width=0.20
plt.bar(x-width,sachin,width=width,color='Red',label="sachin")
plt.bar(x,sehwag,width=width,color='Blue',label="sehwag")
plt.bar(x+width,kohli,width=width,color='Green',label="kohli")

plt.legend()
plt.ylabel("Runs")
plt.xlabel("years")
plt.title("Runs and years Comparision")

plt.xticks(x,years)
plt.grid(True)

for i in range(len(x)):
    plt.text(x[i]-width, sachin[i]+50, str(sachin[i]), ha='center', fontsize=8)
    plt.text(x[i], sehwag[i]+50, str(sehwag[i]), ha='center', fontsize=8)
    plt.text(x[i]+width, kohli[i]+50, str(kohli[i]), ha='center', fontsize=8)
    
plt.show()