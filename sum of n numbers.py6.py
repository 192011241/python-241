input = int(input("Enter a number: "))  
if input < 0:  
   print("Enter a positive number")  
else:  
   sum = 0  
   while(input > 0):  
       sum += input  
       input -= 2 
   print("The result is",sum)  
