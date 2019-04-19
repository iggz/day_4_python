# string_exercises.py 
#                              
#
# ip - 4/18


##########################
### Uppercase a String ###
##########################

'''
string = str(input("Enter a string... ")).upper()

print(string)
'''

###########################
### Capitalize a String ###
###########################

'''
string = str(input("Enter a string... ")).capitalize()

print(string)
'''

########################
### Reverse a String ###
########################

'''
**Version 1**

def rev_string():
    word = (input("Enter a word... "))
    counter = -1
    total_length = (len(word) * -1)
    ret_val = ""


    while counter >= total_length:
        ret_val = ret_val + word[counter] 
        counter = counter - 1
    return ret_val

print(rev_string())
'''



'''
**Version 2**

def rev_string():
    word = input("Enter a word...")
    length = len(word) - 1
    counter = 0
    ret_val = ""

    while length >= counter:
        ret_val = ret_val + word[length]
        length = length - 1
    return ret_val

print(rev_string())
'''

        
#################
### Leetspeak ###
#################
'''

def leetspeak():
    paragraph = input("Enter a paragraph: ")
    ret_val = ""

    for letter in paragraph:
        if letter == "A":
            ret_val = ret_val + "4"
        elif letter == "E":
            ret_val = ret_val + "3"
        elif letter == "G":
            ret_val = ret_val + "6"
        elif letter == "I":
            ret_val = ret_val + "1"
        elif letter == "O":
            ret_val = ret_val + "0"
        elif letter == "S":
            ret_val = ret_val + "5"
        elif letter == "T":
            ret_val = ret_val + "7"
        else:
            ret_val = ret_val + letter
    return ret_val

print(leetspeak())

'''

########################
### Long-long Vowels ###
########################

def long_vowel():
    word = input("Enter word: ")
    ret_val = ""
    count = 0

    for char in word:
        if char == word[count + 1]:
            #print("yes")
            ret_val += char * 5
        elif char == word[count - 1]:
            #print("no")
            count += 1
            continue
        else:
            ret_val = ret_val + char

    count += 1
    return ret_val

print(long_vowel())




