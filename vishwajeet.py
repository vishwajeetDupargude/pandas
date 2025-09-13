#Q1(write the function that takes list of numbers and retursns the sum)

def sum_of_lists(nums):
    return sum(nums)

print(sum_of_lists([1,5]))



#revers string

def reverse_string(s):
    return s[::-1]

print(reverse_string("vishwajeet"))


#palindrome word

def is_palindrome(word):
    return word==word[::-1]

print(is_palindrome("level"))

#remove duplicate fron list

def remove_duplicates(lst):
    return list(set(lst))


print(remove_duplicates([4,5,4]))

#how to handle exception 

try:
    x=1/0
except ZeroDivisionError:
    print("cannot divide by zero")    


# lambada example

multiply=lambda x,y:x*y
print(multiply(3,4))