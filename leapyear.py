
#reading year to check leap year or not
year=int(input("Enter a Year "))
#dividing year with 4
if year%4==0:
    #if decade year it may or may not be a leap year
    if year%100==0:
        #if decade year divide by 400 then leap year
        if (year%400==0):
            print("Yes, Leap Year")
        else:
            print("Not a Leap Year")
    else:
        print("Yes, Leap Year")     
    
else:
    print("Not a Leap Year")
    
        
    
