import csv
from lib2to3.pgen2.token import NEWLINE
from tkinter import W
veg=["IDLI","PODI IDLI","MEDUHU VADA","MASALA VADA","PLAIN DOSA","GINGERLY DOSA","GHEE ROST",
    "PAPER ROST","RAVA DOSA","WHEAT DOSA","VEN PONGAL","PLAINOTHAPPAM",
     "KAL DOSA","ONION DOSA","PODI DOSA","POORI MASALA","BARROTA","PANEER TIKKA",
     "MUSHROM TIKKA","GOBI TIKKA","VEGCLEARSOUP","MANCHOW SOUP","TOMATO SOUP",
     "SEEETCON SOUP","HOT&SOUR SOUP","MUSHROOM SOUP"]
amt=[20,45,15,12,40,45,40,50,50,55,40,55,50,60,40,40,50,160,170,110,80,100,100,100,100,100]

print("\n\t\t BESENT HOTELS FOOD MENUE\n")
i=0
j=len(veg)
print("---------------------------------------------------------------")
print("\tS.NO\t ITEMS\t\t\tAMOUNT")

print("---------------------------------------------------------------")
while i < j:
    print("\t",i+1,"\t",veg[i].ljust(10),"\t\t ",amt[i])  
    i+=1
print("---------------------------------------------------------------")

tot=[]
qn=[]
bm=[]
while True:
    slt=int (input("PLACE YOUR ORDER TO ENTER S.NO TO SELECT ITEM OR 0 TO EXIT: "))
    te=len(veg)
    if slt>te:
        print("INVALID INPUT PLESE ENTER CORRECTLY")
    elif slt!=0:
        print("YOUR SELECTED ITEM IS", veg[slt-1])
        qnt=int(input("ENTER YOUR QUANTITY: "))
        if qnt==0:
            continue    
        temp=qnt*amt[slt-1]
        ordno=0
        if slt!=0:
           bm.insert(ordno,slt-1)
        tot.insert(ordno,temp)
        qn.insert(ordno,qnt)
        ordno+=1
    elif slt==0:
        break
tot.reverse()
qn.reverse()
bm.reverse()

print("\n\t\t\tYOUR ORDER BILL IS")
print("------------------------------------------------------------------")
print("\tS.NO\t ITEMS\t\tQUANTITY\tAMOUNT")
print("------------------------------------------------------------------")
i=0
it=[]
od=0
for x in range (len(tot)):
    item=veg[bm[i]]
    it.insert(od,item)
    od+=1
    print("\t",i+1,"\t",item,"\t",qn[i],"\t","\t",tot[i])
    
    i+=1

print("------------------------------------------------------------------")

sum=0
for y in range (len(tot)):
    sum=sum+tot[y]

print("\tYOUR TOTAL AMOUNT IS\t\t\t",sum)
print("------------------------------------------------------------------")

with open("https://github.com/GANESH9403/PYTHON/blob/main/hotelS.csv","a",newline="") as hot:
   
    w = csv.writer(hot)
    w.writerow("")
    w.writerow(it)
    w.writerow(qn)
    w.writerow(tot)
    
  
