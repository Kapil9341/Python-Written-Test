# WAP to find maximum value and which key store max value
n=int(input("Enter Element: "))                 # put dictionay element
dict = {}                                       # take blank list for storing elemnet by user
                                                
for i in range(n):                              # for loop for iteration
    key=int(input("Entery key: "))              # put key in dict...
    value=input("Enter value: ")                # put value in dict...
    dict.update({key:value})                    # update method use for update value in dict.....

print("First Distionary = ",dict)               
print("Dictionary key = ",dict.keys())

def Exam_score(dict):                           # crete function with argument
    dict2 = {}                                  # take second dictionay store 1st dict keys but different value
    for n1 in dict.keys():                      # again iterate , and n1 is key container
        value1=int(input("Enter Exam score: ")) # put Exam score
        dict2.update({n1:value1})               # update dict.. value
    print("Second Dictionary = ",dict2)
    m=max(dict2, key=dict2.get)                 # find key which store max value by get method
    m1=max(dict2.values())                      # max method use for get dict.. max value
    #print("maximum =",m)
    print("maximum: ",m,":",m1)

Exam_score(dict)

