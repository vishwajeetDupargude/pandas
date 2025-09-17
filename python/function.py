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

def hello(greeting,title,first,last):
    print(f"{greeting},{title},{first},{last}")

    

#hello("hello","Mr.","vishwajeet","Dupargude")
#
# print(hello(title="mr",first="vishwajeet",greeting="hello",last="dupargude"))  #keyword argument doesn't contain the order
print(hello("hello",title="mr",first="vishwajeet",last="dupargude"))