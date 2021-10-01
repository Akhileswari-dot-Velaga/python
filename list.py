list=[]
print("blank list: ",list)
print(type(list))

list1=[10,20,30,40]
print("\n list elements: ",list1)

list2=["hello","good","morning"]
print("\n list string items: ",list2)


list3=[["hii","hello"],["how","are","you"]]
print("\n multi dimenstional list: ",list3)

list4=[1,2,2,3,1,8,5,4,5,2]
print("\n duplicate elements :",list4)

list5=[1,1.23,'akhila','hii']
print("\n with diffrent data types: ",list5)

print("\n priting the length of each list")
print("list",len(list))
print("list1",len(list1))
print("list2",len(list2))
print("list3",len(list3))
print("list4",len(list4))
print("list5",len(list5))

print("\n appending elements into list")
print(" before appending:" ,list)
list.append(1)
print("\n after appending:",list)


print("\n using for loop we appending the elements into the list")
print(list1)
for i in range(1,5):
    list1.append(i)
print("\n",list1)



print("\n appending tuple into list")
print(list2)
list2.append((5,6))
print("\n",list2)


print("\n appending a list into a list")
print("\n elements of list",list)
print("\n eleents of list2",list2)
list.append(list2)
print("\n  after appending the list elements: ",list)


print(" \n using insert method we can specify with index number")

print("\n",list5)
list5.insert(3,"i am inserted at pos 3")
print("\n",list5)


print(" \n using extend method")

print("\n",list2)
list2.extend([7,900,"extend"])
print("\n ",list2)


print("\n accessing elemets from the list")
print(list1)
print(list[1])


print("\n accessing elements from the multidiemntional list")
print(list3)
print(list3[1][0])
print(list3[0][1])



print("\n removing elements from the list")
print(list2)
list2.remove(900)
print(list2)


print("\n pop method ")
print(list2)
list2.pop()
print(list2)



print("\n clear method is used to clear all the ites from the list")

print(list4)
list4.clear()
print(list4)


print("\n print all lists at single print statement")
print(list1,list2)


print("\n count method")
pet=[1,2,2,8,5,2]
print(pet.count(2))




a=[9,5,7,2,1,8,6,3,7,1]
a.sort()
print(a)
a.sort(reverse=True)
print(a)

print("index  starts from 0")
print(" we can know the index value of specific elment")
print(a.index(9))


print("copying a list elements into balnk list")
b=[]
c=[45,55,66]
b=c.copy()
print(b)



























             

























