from ctypes import string_at
import math
import sys
from collections import Counter

# task 1
def returnSquareRoot(x1,x2,y1,y2):
    xDifference=(x2-x1)**2
    yDifference=(y2-y1)**2
    Summation=xDifference+yDifference
    result=math.sqrt(Summation)
    print(result)
#returnSquareRoot(4,8,4,8)    
  
  
#task two    
def uniqueNumbers(mylist):
    list_set=set(mylist)
    uniqueList=(list(list_set))
    for x in uniqueList:
        print(x)

#task Five    
def removeVowels(myString):
    new_string=myString
    vowelsList=['a','e','i','o','u']
    for x in myString.lower():
        if x in vowelsList:
            new_string=new_string.replace(x, "")
    print(new_string)   
                   
# str="apple"
# removeVowels(str) 

# task 6 with enumerate function
def returnCharWithLocation(myString,myChar):
    mylist=[]
    for index,char in enumerate(myString):
        if(char==myChar):
            mylist.append(index)
    print(mylist)        
            
# str="Googole"
# returnCharWithLocation(str,'o')   

#task 4
def readMyFile():
    with open(sys.argv[1], 'r') as my_file:
        contents=my_file.read()
        my_file.close()
        words=Counter(contents.split()).most_common(20)
        words=[x[0] for x in words]
        file=open("popular_words.txt","w")
        file.write("\n".join(map(lambda x: str(x),words)))
        file.close()
        #   count = Counter(word for line in my_file
        #                  for word in (line.split()))
        #   print(count.most_common(20))   
#readMyFile()        

#task 3
def divideString(a,b):
    aindex=int((len(a)+1)/2)
    bindex=int((len(b)+1)/2)
    print(a[:aindex]+b[:bindex]+a[aindex:]+b[bindex])
    print("\n")
    
    
    
    

#Operator module
import operator

a = 4
b = 3
# using add() to add two numbers
print ("The addition of numbers is :",end="");
print (operator.add(a, b))

# using sub() to subtract two numbers
print ("The difference of numbers is :",end="");
print (operator.sub(a, b))

# using mul() to multiply two numbers
print ("The product of numbers is :",end="");
print (operator.mul(a, b))


# using lt() to check if a is less than b
if(operator.lt(a,b)):
	print ("3 is less than 3")
else : print ("3 is not less than 3")

# using le() to check if a is less than or equal to b
if(operator.le(a,b)):
	print ("3 is less than or equal to 3")
else : print ("3 is not less than or equal to 3")

# using eq() to check if a is equal to b
if (operator.eq(a,b)):
	print ("3 is equal to 3")
else : print ("3 is not equal to 3")


# using gt() to check if a is greater than b
if (operator.gt(a,b)):
	print ("4 is greater than 3")
else : print ("4 is not greater than 3")

# using ge() to check if a is greater than or equal to b
if (operator.ge(a,b)):
	print ("4 is greater than or equal to 3")
else : print ("4 is not greater than or equal to 3")

# using ne() to check if a is not equal to b
if (operator.ne(a,b)):
	print ("4 is not equal to 3")
else : print ("4 is equal to 3")
     
            

  
        
        
    


      
              