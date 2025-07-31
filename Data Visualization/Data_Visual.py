import matplotlib.pyplot as plt
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
Kohli= [800,950,1100,1250,1400,1350,1500,1450,1600,1550]

Rohit_Sharma= [750,900,1000,1150,1300,1400,1300,1500,1400,1650]

Sehwag =[900,850,1050,950,1100,1000,1200,1150,1300,1250]

plt.plot(years,Kohli, color="Red",label="Kohli",linewidth=2,linestyle="--",marker="o")
plt.plot(years,Rohit_Sharma , color="Pink",label="Rohit_Sharma",linewidth=3,linestyle="-.",marker="^")
plt.plot(years,Sehwag , color="green",label="Sehwag",linewidth=4,linestyle="-.",marker="*")
plt.legend()
plt.title("Run Rate of Kohli Rohit Sharma and Sweag")
plt.xlabel("Race Run")
plt.ylabel("Years")
plt.grid(True)
plt.show()

