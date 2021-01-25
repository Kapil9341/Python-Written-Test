# WAP to sum of the list of numbers...
list_size = int(input("Enter list size: "))      # input size of list
lst=[]
for n in range (list_size):                       # for loop for iterate list size
    numbers = int(input("Enter list numbers: "))  # input list numbers
    lst.append(numbers)                           # append method insert an item
print("list = ",lst)
                                             
def list_sum(lst):                                 # User define function
    total=0
    for x in lst:                                  # for loop for iterate lst value
        total=total+x
    print("sum of list =",total)
list_sum(lst)                                      # function call

# using predefine sum function....
'''
list=[1,2,3,4,5,6,7,8,9,10]
print(list)
list_sum = sum(list)
print(list_sum)

'''