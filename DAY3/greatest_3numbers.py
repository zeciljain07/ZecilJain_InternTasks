print("Enter 1st number:")
a=int(input())
print("Enter 2nd number:")
b=int(input())
print("Enter 3rd number:")
c=int(input())

if a>b:
    if a>c:
        print("1st number is greatest!!")
    else:
        print("3rd number is greatest!!")
else:
    if b>c:
        print("2nd number is greatest!!")
    else:
        print("3rd number is greatest!!")
