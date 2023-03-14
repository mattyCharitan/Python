from functools import reduce
import string
import os

#1:
#Method 1:

def sum_list(nums):
    return sum(nums)


#Method 2:
def sum_list(nums):
    sum = 0
    for num in nums:
        sum += num
    return sum



#Method 3:

def sum_list(nums):
    sum = 0
    i = 0
    while i < len(nums):
        sum += nums[i]
        i += 1
    return sum

#Method 4:


def sum_list(nums):
    return reduce(lambda x, y: x + y, nums)

#2:

def in_range(num, start, end):
    return True if start <= num <= end else False

#3:
def count_upper_lower(string):
    upper = 0
    lower = 0

    for ch in string:
        if ch.isupper():
            upper+=1
        elif ch.islower():
            lower+=1
    return upper, lower

#4:

def even(list):
    for item in list:
        if item%2 ==0:
            print(item)

#5:

def is_palindrome(string):
    string = string.lower().replace(" ", "")
    return True if string == string[::-1] else False

#6:

def sortDictionary(list):
   return sorted(list, key=lambda x: x['color'])

#7:
def fileLetters():
    letters = string.ascii_uppercase
    for letter in letters:
        filename = letter + ".txt"
        with open(filename, "w") as file:
            file.write(letter)

#8:


def copy_file(source_file):
    with open(source_file, 'r') as f_source:
        contents = f_source.read()

    source_filename = os.path.basename(source_file)
    dest_filename = "copy_" + source_filename

    with open(dest_filename, 'w') as f_dest:
        f_dest.write(contents)

    return dest_filename











    



