from ast import Break
from datetime import date, datetime
from pickle import FALSE,TRUE

today=date.today()
ticket_verefi=False
covid_verefi=False
immg_verefi=False
lug_verefi=False
dot=False
covid_certi=False

#dateverfication

dateoftravel=input("ENTER YOUR DATA OF TRAVEL AS PER TICKET (DD/MM/YYYY)\t:")
d=today.strftime("%d/%m/%Y")

if dateoftravel==d:
    print("----------------------------------------------------------------------") 
    print("Date verfication pass")
    print("----------------------------------------------------------------------") 
    dot=True

else:
    print("Date verefication failed. Your ticket expired")
    exit()

#covidcerficate verefication

while True:
        covidcertification= input("IF YOU HAVE A COVIDCERTFICATE PRESS 'Y' IF YOU DON'T HAVE COVID CERFICATE PRESS 'N'\t:")[0].upper()
               
        if  covidcertification=="Y":
            print("----------------------------------------------------------------------")
            print("COVIDCERTIFCATION VEREFIED")
            covid_certi=True
            print("----------------------------------------------------------------------") 
            break
       
        elif covidcertification=="N":
            print("----------------------------------------------------------------------")
            print("YOU MUST HAVE COVID19 CERTFICATION")
            print("You could not able to enter into the airport")
            print("----------------------------------------------------------------------")
            exit()
            break
        
        else:
            print("INVALID INPUT")

#security ticket checking process:

if dot==True and covid_certi==True:
    ticket_verefi=True

#covid test inside airport:

while True:
    print("\n\n----------------------------------------------------------------------") 
    covid=input("ENTER YOUR CURRENT COVID TEST STATUS IF POSITIVE PRESS 'P' OR IF NEGATIVE PRESS 'N'\t:")[0].upper()
    
    if covid=="P":
        print("COVID POSITIVE")
        break
    
    elif covid=="N":
        print("----------------------------------------------------------------------") 
        print("COVID NEGATIVE")
        covid_verefi=True
        print("----------------------------------------------------------------------")   
        break


#immigiration process:

format = "%d/%m/%Y"
temp = True

t_name=input("ENTER YOUR NAME AS PER TICKET\t:")
t_dob=input("ENTER YOUR DATE OF BIRTH AS PER TICKET (DD/MM/YYYY)\t:")

try:
    temp = bool(datetime.strptime(t_dob, format))

except ValueError:
    temp = False
print("INVALIDE DATE")

a_name=input("ENTER YOUR NAME AS PER ANY GOVERNMENT ID PROOF\t:")
a_dob=input("ENTER YOUR DATE OF BIRTH AS PER ANY GOVERNMENT ID PROOF (DD/MM/YYYY)\t:")

try:
    temp = bool(datetime.strptime(t_dob, format))

except ValueError:
    temp = False
print("INVALIDE DATE")

if(t_name==a_name and a_dob==t_dob):
    print("----------------------------------------------------------------------") 
    print("IMMIGIRATIION PROCESS COMPLETEED")
    print("----------------------------------------------------------------------") 
    immg_verefi=True
    
else:
    print("----------------------------------------------------------------------") 
    print("IMMIGIRATION PROCESS INCOMPLETED")
    print("----------------------------------------------------------------------") 
    print("Name or age Missmatch")
    
#luggage weight 

weight=int (input("ENTER YOUR WEIGHT OF LUGGAGE\t:"))
a_weight=20
weightpayment=(weight-a_weight)*600

if weight<=20:
     print("----------------------------------------------------------------------") 
     print("YOU ARE ALLOWED")
     print("----------------------------------------------------------------------") 
     print("\nPLEASE RECEIVE YOUR BOADING PASS IN THE COUNTER NO : 23")
     lug_verefi=True

elif(weight<=45):
    print("----------------------------------------------------------------------")
    print("YOUR LUGGAGE IS MORE THAN 20 WILL NOT ALLOWED")
    print("YOUR NEED TO PAY PER KG RS.600")
    print(f"YOUR TOTAL LUGGAGE IS{weight}YOU NEED TO PAY {weightpayment} FOR THE EXTRA LUGGAGE{weight-a_weight} KG")
    print("----------------------------------------------------------------------") 
   
    while True:
        pay=input("IF YOU PAY PRESS 'Y' OR IF YOU DONT PAY PRESS 'N'\t:")[0].upper()
        
        if pay=="Y":
            print("you are allowed")
            print("Please recive your boading pass in counter:27")
            lug_verefi=True
            break
        
        elif pay=="N":
            print("----------------------------------------------------------------------") 
            print("LUGGAGE WEIGHT CHECKING PROCESS FAILD")
            print("----------------------------------------------------------------------") 
            break
        
        else:
            print("INVALIDE INPUT")

else:
    print("PROCESS FAILD")
final_p=int(input("ENTER YOUR BOADING PASS NUMBER TO FINAL VEREFICATION:\t CODE(1234) "))

if final_p==1234:
    print("\n\t\t\tFINAL VEREFICATION PROCESS\n")
    print("----------------------------------------------------------------------")
   
    if ticket_verefi==True:
        print("TICKET CHEACKING\t\t:\t COMPLETED SUCESSFULLY",'\u2714')
    
    else:
        print("TICKET CHEACKING\t\t:\t FAILD",'\u2715')

    if covid_verefi==True:
        print("COVID19 CHEACKING\t\t:\t COMPLETED SUCESSFULLY",'\u2714')
    
    else:
        print("COVID19 CHEACKING\t\t:\t FAILD",'\u2715')
   
    if immg_verefi==True:
        print("IMMIGRATION PROCESS\t\t:\t COMPLETED SUCESSFULLY",'\u2714') 
    
    else:
        print("IMMIGRATION PROCESS\t\t:\t FAILD",'\u2715')

    
    if lug_verefi==True:
  
        print("LUGGAGE WEIGHT CHECKING PROCESS\t:\t COMPLETED SUCESSFULLY",'\u2714') 
        print("----------------------------------------------------------------------")
   
    else:
        print("IMMIGRATION PROCESS\t\t:\t FAILD",'\u2715')
        print("----------------------------------------------------------------------")
    
    if(ticket_verefi==True and covid_verefi==True and immg_verefi==True and lug_verefi==True):
        print("\nONCE AGANI WELCOME TO ARIPORT PLEASE GO TO THE MAIN GATE")
    
    else:
    
        print("YOU COULD NOT ABLE TO TRAVEL")

else:
        print("YOU COULD NOT ABLE TO TRAVEL")
    
    

 
    

