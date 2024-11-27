list = [9,2,6,4,8]
length = len(list)
i = 0
max = list[0]
min = list[0]


for i in range (length):
    print(list[i])
    if max < list[i]:
        max = list[i]
        
    

    if min > list[i]:
        min = list[i]

    

print("max is" , max)

print("min is " , min)

    
print("using negative indexing to print the list items")

for i in range (1,length + 1):
    print(list[-i])
