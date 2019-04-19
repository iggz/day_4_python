# list_exercises.py 
#                              
#
# ip - 4/18


#######################
### Sum the Numbers ###
#######################

"""
list = [1,2,3,4]

total = 0

for i in list:
    total = total + i

print(total)
"""
######################
### Largest Number ###
######################
'''

list = [1,2,3,4]

largest_num = 0

for i in list:
    if i > largest_num:
        largest_num = i
    elif i <= largest_num:
        continue

print(largest_num)
'''

#######################
### Smallest Number ###
#######################
'''
list = [1,2,3,4]

smallest_num = list[0]

for i in list:
    if i < smallest_num:
        smallest_num = i
    elif i >= smallest_num:
        continue

print(smallest_num)
'''
####################
### Even Numbers ###
####################
'''
list = [1,2,3,4]

even_num = []

for i in list:
    if i % 2 == 0:
        even_num.append(i)
    elif i % 2 != 0:
        continue

print(even_num)
'''

########################
### Positive Numbers ###
########################

'''
list = [-4,-3,-2,-1,0,1,2,3,4]

pos_num = []

for i in list:
    if i > 0:
        pos_num.append(i)
    elif i <= 0:
        continue

print(pos_num)
'''

########################
### Multiply a list ####
########################

'''
list = [-4,-3,-2,-1,0,1,2,3,4]
factor = 2

new_list = []

for i in list:
    new_list.append(i * factor)

print(new_list)
'''

#########################
### Multiply Vectors ####
#########################

'''
list1 = [2,4,5]
list2 = [2,3,6]
count = 0

new_list = []

for i in list1:
    new_list.append(i*list2[count])
    count += 1
    #for j in list2:
        #new_list.append(i*j)

print(new_list)
'''

#########################
### Matrix Addition #####
#########################

matrix1 = [[1,3],[2,4]]
matrix2 = [[5,2],[1,0]]
list_answer = []

for i in range(len(matrix1)):
    print (i)
    for j in range(len(matrix2[0])):
        print(j)

