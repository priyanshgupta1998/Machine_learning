
#Till Now we've  created  the datafile which contains everything rank , college , category , branch
#import pandas  linrary
import pandas as pd
df = pd.read_csv('OUTPUT.csv')  # datafile


df.rename(columns = {"Department":"DEPARTMENT"} ,inplace=True)
rank = int(input('ENTER THE RANK : '))
cat = input('ENTER THE CATEGORY FROM ("SC" , "ST" , "OBC" , "GENERAL") : ')
fin = df[(df['RANK_PREDICTOR']==rank) & (df['CATEGORY']==cat)].iloc[: , :2] #take all relevant data from entire table
fin.reset_index(inplace=True)
fin.drop('index' ,axis =1,inplace=True)
order = input("Enter the order from ('DEPARTMENT' ,'INSTITUTES' ) : ")
dic = {} # cretae a empty list
for i in range(len(fin[order])):
  dic[list(fin[order])[i]] = []
  
app = list(fin.columns)
app.remove(order)

for i in range(len(fin[order])):
  dic[list(fin[order])[i]]+=[list(fin[app[0]])[i].strip()]


dat = pd.DataFrame(list(dic.items()) ,columns=[order, app[0]])
print(dat)
