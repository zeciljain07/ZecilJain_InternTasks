#Variable-length arguements.
def sum(*n1):
    sum=0
    for i in n1:
        sum=sum+i

    print("answer is ", sum)


sum(14,29)
sum(23,124,64)
