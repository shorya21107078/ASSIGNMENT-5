#Q1 Program to reverse the string.
a = input('Enter the string to reverse: ')
print(a[::-1])

#Q2 Python Program to Print all Numbers in a Range Divisible by a Given Number.
a=int(input('enter the number: '))
r1=int(input('enter the first value of range: '))
r2=int(input('enter the last value of range: '))
for i in range(r1,r2+1):
    if (i%a==0):
        print(i)
        

#Q3 Program to calculate the area of a triangle using heron’s formula.
a=int(input("Enter first side: "))
b=int(input("Enter second side: "))
c=int(input("Enter third side: "))
if(a+b>c and a+c>b and b+c>a): 
    s=(a+b+c)/2
    area=(s*(s-a)*(s-b)*(s-c))**0.5
    print("Area of the triangle is: ",round(area,3))
else: 
    print("Triangle can not be formed with",a,b,c,"as sides")
    
    
#Q4 program to construct following pattern
n=5;
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')
    
#Q5 program to print triangular pattern of alphabet
n = int (input('enter the no. of rows: '))
k = ord('A')
for i in range(n):
    for j in range (i+1):
        print (chr(k), end=" ")
        k+=1
        if (k>=91):
            k = k-26
    print()
    
#Q6 program to print prime numbers for a user input range
a=int(input('Enter the starting value of range: '))
b=int(input('Enter the end value of range: '))
for i in range(a,b):
    for j in range(2,i):
        if (i%j)==0:
            break
    else:
        print(i)
        
        
#Q7 to find no. multiple of 7 and divisible by 11
for i in range(0,501):
    if (i%7==0 and i%11==0):
      print (i)
      
      
#Q8 input 10 integer values from user
lst = []
positive_numbers = set()
negative_numbers = set()
odd_numbers = set()
even_numbers = set()
print ('Enter the 10 no. for list')
for i in range(0,10):
    print ('Enter the', i+1,'no. for list')
    n = int(input())
    lst.append(n)  # adding the element
print ('list entered',lst)
for i in lst:
    if (i>0):
        positive_numbers.add(i)
    if (i<0):
        negative_numbers.add(i)
    if (i%2!=0) :   
        odd_numbers.add(i)
    if (i%2==0) :
        even_numbers.add(i)  
print ("positive no. \n", positive_numbers)
print ('negative no.\n', negative_numbers)
print ('odd no.\n', odd_numbers)
print ('even no.\n', even_numbers)
number_occurs= dict()
for i in lst:
    if i in number_occurs:
        number_occurs[i]+=1
    else:
        number_occurs[i]=1
print('No. of occurrence is',number_occurs)
    
#Q9 to count no. of occurence of each word in list 
str = input('Enter the words: ')
sentence = dict()
words = str.split()
for word in words:
    if word in sentence:
        sentence[word]+=1
    else:
        sentence[word] = 1
print (sentence)



