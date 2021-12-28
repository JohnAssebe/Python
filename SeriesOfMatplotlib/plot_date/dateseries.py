from matplotlib import pyplot as plt 
from datetime import datetime
from matplotlib import dates as mpl_date
plt.style.use('seaborn')
dates=[
	datetime(2020,3,5),
	datetime(2020,3,3),
	datetime(2020,3,6),
	datetime(2020,3,1),
	datetime(2020,3,30)
]
y=[1,2,3,9,0]
plt.plot_date(dates,y,linestyle='solid')
plt.gcf().autofmt_xdate() 
# gcf stands for get current figure 
date_format=mpl_date.DateFormatter('%b, %d %y') 
# b for abbrevated day , m for month ,and y for year 
plt.gca().xaxis.set_major_formatter(date_format) 
# gca stands for get current axis 
plt.xlabel("Date")
plt.ylabel("Sale")
plt.title("Total Sale Over time")
plt.tight_layout()
plt.show()