'''
@author Yohannes Assebe
sololearn python data science course project 1 question answer 
'''
players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]
sumation=0
for i in range(len(players)):
    sumation+=players[i]
mean=sumation/len(players)
sum_of_square_difference=0
for i in range(len(players)):
    sum_of_square_difference+=(players[i]-mean)**2
varience=sum_of_square_difference/len(players)
standard_deviation=varience**0.5
count=0
for i in range(len(players)):
    if (mean-standard_deviation)<=players[i]<=(mean+standard_deviation):
        count+=1
print(count)
