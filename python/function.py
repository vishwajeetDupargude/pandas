#def fucntion using three parameter

'''
def invoice_bill(username,amount,due_date):
    print(f"hello {username}")
    print(f"the {amount} of bill")

    print(f"The  {due_date} of bill ")

invoice_bill('vishwajeet',2000,"12/2/2026")    
'''



# Retutn statement
'''

def create_name(first,last):
    first=first.capitalize()
    last=last.capitalize()

    return first + " " + last

full_name=create_name( "vishwajeet", "Dupargude")

print(full_name)

'''

#fuction using default value
'''
def net_price(price,discount=0,tax=0.05):  # use default value for discount and tax
    return price*(1-discount)*(1+tax)

print(net_price(5000))

'''

#count timer
'''
import time

def count(start,end):
    for i in range(start,end+1):
        print(i)
        time.sleep(1)

    print("done")    
print(count(1,10))    

'''

#keyword
'''
def hello(greeting,title,first,last):
    print(f"{greeting},{title},{first},{last}")

    

#hello("hello","Mr.","vishwajeet","Dupargude")
#
# print(hello(title="mr",first="vishwajeet",greeting="hello",last="dupargude"))  #keyword argument doesn't contain the order
print(hello("hello",title="mr",first="vishwajeet",last="dupargude"))


'''

# *args  using this function we pass multiple non key arguments
'''

def display_name(*args):
    for i in  args:
        print(i,end=" ")
print(display_name("Mr.","vishwajeet","Dupargue"))

'''

#**kwargs =this function pass multiple keyword-arguments


'''


def print_address(**kwargs):
    for key,value in kwargs.items():  #this **kwargs used dictionary type in pair of key value
        print(f"{key}, {value}")

    



print(print_address(street="Akurdi",state="India",zipcode="12345"))    

'''

# iterable= this is used over the loop and output one by one

'''


for char in "vishwajeeet":
    print(char,end=" ")  #iterable for one by one output

    
'''


#membership operator= used to test whether the value and varibles found  in a sequence 1)in  2)not in


'''
word="VISHWAJEET"

letter=input("Guess a letter in words:")

if letter in word:   #in return values  boolean value like either True or False
    print(f"there is a {letter}")

else:
    print(f"{letter} was not found")    


'''

 #for not in


'''
word="VISHWAJEET"

letter=input("Guess a letter in words:")

if letter not in word:
    print(f"{letter} was not found")      
   

else:
    print(f"there is a {letter}")   
    
'''

#example

student={"vishwajeet","vijay","sumit","chetan"}

students=input("Enter a student name:" )

if students in student:
    print(f" the student is in list{students}")

else:
    print(f"{students} not in list")    