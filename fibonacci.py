#fibonacci series
i=0
m=1
n=0
count=int(input("Enter the number : "))
while n<=count:
     print(i)
     t=i+m
     i=m
     m=t
     n=n+1
