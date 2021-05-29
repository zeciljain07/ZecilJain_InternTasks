print("Enter the year:")
yr=int(input())

if yr%4==0 and yr%100!=0:
    print("Entered year is a leap year.")
elif yr%400==0:
    print("Entered year is a leap year.")
else:
    print("Entered year is not a leap year.")
