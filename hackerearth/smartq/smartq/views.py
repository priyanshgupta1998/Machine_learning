from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request ,'welcome.html')





 #for first part 
import pandas as pd
liss1= []
for i in range(13, 113):
  liss1.append(i)
data1 = pd.read_csv('smartq.csv',skiprows = liss1)
data1['timeslot1'] = data1['availabletime'].apply(lambda x:x.split(',')[0])
data1['timeslot2'] = data1['availabletime'].apply(lambda x:x.split(',')[1])
time1 = []
time2 = []
items = []
for i in range(len(data1)):
  time1.append(list(data1['timeslot1'])[i])
  time2.append(list(data1['timeslot2'])[i])
  items.append(list(data1['itemname'])[i])
df1 = pd.DataFrame()
df1['item'] = items + items
df1['timeslot'] = time1+time2
df1['intTime'] = df1['timeslot'].apply(lambda x:','.join([str(int(x.split('-')[0].split(':')[0])*60 + int(x.split('-')[0].split(':')[1])) , str(int(x.split('-')[1].split(':')[0])*60 +int(x.split('-')[1].split(':')[1]))]))

st= [420 ,750 , 990 , 1170]
e = [660 ,750 , 930 ,990 , 1140 ,1170,1380]
dic = ['Breakfast', 'Lunch' , 'Snack' , 'Dinner']
k=0
good = []
for i in range(len(st)):
  count = 0
  s = i
  aaj = dic[i]
  for j in range(k,len(e)):
    good.append(aaj)
    count+=1
    if(count==2):
      count=0
      s+=1
      aaj = aaj +','+ dic[s]
  k+=2
joker = []
for i in range(len(st)):
  for j in range(len(e)):
    l =str(st[i]) + ',' + str(e[j])
    joker.append(l)


go =[]
for i in range(len(good)):
  go.append(good[i] + '_'+ joker[i])
go.sort(reverse = True)
joker1 = []
good1 = []
for i in range(len(go)):
  good1.append(go[i].split('_')[0])
  joker1.append(go[i].split('_')[1])
res = []
for i in range(len(df1)):
  x = list(df1['intTime'])[i]
  x1 =int( x.split(',')[0])
  x2 = int(x.split(',')[1])
  for j in range(len(good)):
    y1 = int(joker1[j].split(',')[0])
    y2 = int(joker1[j].split(',')[1])
    if(x1>=y1 and x2<=y2):
      res.append(good1[j])
      break
df1['have'] = res
print(df1.shape)
df1.head()




####################################################
######################################################

#######################################################
################################################
# for second part
import ast
import re
liss2= []
for i in range(13):
  liss2.append(i)
data2 = pd.read_csv('smartq.csv',skiprows = liss2)
df2 = data2.copy()
data2['date'] = data2['timestamp'].apply(lambda x:'-'.join(x.split()[0].split('-')[::-1]))
data2['time'] = data2['timestamp'].apply(lambda x:x.split()[1])
data2['item'] = data2['orderedItems'].apply(lambda x:ast.literal_eval(re.sub('’','"' , re.sub('‘','"' , x)))[0]['itemname'])
data2['quantity'] = data2['orderedItems'].apply(lambda x:ast.literal_eval(re.sub('’','"' , re.sub('‘','"' , x)))[0]['quantity'])
data2.rename(columns={'billamount': 'bill'}, inplace=True)
data2.drop(['orderid','orderedItems' ,  'timestamp'] , inplace=True , axis=1)
# print(data2.shape)
# data2.head()

# resid = input("Enter the Restaurant ID : " )
# date = input("Enter the date : ")
new_d2 = data2[(data2['restaurantid']==resid) & (data2['date']==date)].quantity.sum()
print("Total sales sample : " , new_d2)




# resid = input("Enter the Restaurant ID : " )
# item = input("Enter the sample Item : " )
# date = input("Enter the date : ")
new_d2 = data2[(data2['restaurantid']==resid) & (data2['item']==item) & (data2['date']==date)].quantity.sum()
if(new_d2>0):
  print("Item Available ,  {} quantity sold".format(new_d2))
else:
  print("Item Not Available ,0 quantity sold")