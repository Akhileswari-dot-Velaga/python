#WAP to interchange first and last elements in a list.



list=[1,2,3,4]
temp=list[-1]
list[-1]=list[0]
list[0]=temp
print(list)
