'''
@Author:Yohannes Assebe(John Assebe)
'''
from matplotlib import pyplot as plt
# Use a scatter graph to demonstrate a distribution of data in relation to other data
import random as ra 
plt.style.use('ggplot')
x_index=[ ra.randint(10,10000000000) for i in range(100)] 
# Fake data generated here(List comprehension) for x axis(No of Views)
y_index=[ ra.randint(10,10000000000) for i in range(100)]
# Fake data generated here(List comprehension) for y axis(No of Likes)
colors=[ra.randint(100,500) for i in range(100)]
# Fake data generated here(List comprehension) for setting color based on the values 
# The color contrast changes 
plt.xscale('log')
# setting a log values make it more visible if their values vary greatly
plt.yscale('log')
plt.scatter(x_index,y_index,c=colors,edgecolor='black',linewidth=1,alpha=0.75,cmap="Greens") 
# plt.scatter have 
  # 's' argument for size we can set integeric value or list 
  # change default marker by setting marker='X'
cbar=plt.colorbar()
cbar.set_label("Like/Dislike ratio")
plt.xlabel("No of Views")
plt.ylabel("No of Likes")
plt.title("Youtube Top Viewed Videos(Fake Data)")
plt.tight_layout()
plt.show()
