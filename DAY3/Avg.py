print("Enter the values of numbers whose average is to be found: ")
n= int(input())
print("Enter the " +str(n)+ " numbers:")

nums=[]
for i in range(n):
    nums.insert(i, int(input()))

sum=0
for i in range(n):
    sum=sum+nums[i]

avg = sum/n
print("Average:", avg)
