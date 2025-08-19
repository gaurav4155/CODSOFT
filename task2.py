a=float(input("enter first number:"))
b=float(input("enter second number:"))
sum=a+b
product=a*b
difference=a-b
division=a/b
modulo=a%b
power=a**b
print('choose operation from the following 1=sum,2=product,3=difference,4=division,5=modulo,6=power')
operation=float(input("choose operation"))
if(operation==1):
    print(sum)
elif(operation==2):
    print(product)
elif(operation==3):
    print(difference)
elif(operation==4):
    print(division)#indentation :proper spacing
elif(operation==5):
    print(modulo)
elif(operation==6):
    print(power)
else:
    print("wrong operation")



    

