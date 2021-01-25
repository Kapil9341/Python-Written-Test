lst = [0,0,0.1,1,1,0,0,0,1,1,0,1,1,1,1,0,0,1,1,1,1,1,1,1,1]
x=0
y=0
max=0
for i in range(len(lst)):
    print(i)
    if(lst[i]==0):
        x+=1
        if(y>0 and max==0):
            max=y
            y=0
        elif(max<y):
            max=y
            y=0
        elif(max<x and len(lst)==i+1):
            max=x
            x=0
        
        else:
            y=0    
    else:
        y+=1
        if(x>0 and max==0):
            max=x
            x=0
        elif(max<x):
            max=x
            x=0
        elif(max<y and len(lst)==i+1):
            max=y
            y=0
        else:
            x=0
              
print(max)      

    
