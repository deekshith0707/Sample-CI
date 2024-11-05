list=[]
n=int(input("Enter the range of the elements in the list \n"))
for i in range (n):
    n=int(input("enter the numbers\n"))
    list.append(n)
print(list)
sum=sum(list)
print("The sum is %d \n",sum)
average=sum/n
print("The average is %d \n",average)