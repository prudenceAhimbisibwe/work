# write a python program that takes a string 
# and returns the reverse of the string.

def number(y):
     x = y.split()
     start=0
     end=len(x)-1
     while start<end:
        x[start],x[end]=x[end],x[start]
        start+=1
        end-=1
        str=" "
     print(str.join(x))
number("my name is prudence and I am 20 years old")

# using inbult function
def program(list1):
    x=list1.split()
    list2 =[]
    while x != []:
       poppedItem = x.pop()
       list2.append(poppedItem)    
    print(" ".join(list2))
program("my name is prudence and I am a student at Akirachix")

# write a python program that checks
#  if a given string is a pelidrome
def word(s):
    y=s[::-1]
    if y==s:
        print("palidrom")
    else:
        print("It's not")
word("word")
# Alternatively
def program(x):
    left=0
    right=len(x)-1
    while x[left]!=x[right]:
        print("It's not a peldrome")
        break
    else:
        left+=1
        right-=1
        print("It's a pelidrome")
program("mum")
