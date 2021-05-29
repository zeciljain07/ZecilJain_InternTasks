print("Enter the 1st number:")
a=int(input())
print("Enter the 2nd number:")
b=int(input())
print("Enter the 3rd number:")
c=int(input())


if a<b and a<c:
    print("1st number is smallest!!")
elif b<a and b<c:
    print("2nd number is smallest!!")
else:
    print("3rd number is smallest!!")
