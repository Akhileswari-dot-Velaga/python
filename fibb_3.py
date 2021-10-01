#WAP to print fibonacci series using recursion between n1 and n2 (n1 and n2 should be user inputs)



nterms = int(input("How many terms? "))

# first two terms
n1=int(input("enter first number:"))
n2=int(input("enter second number :"))
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
