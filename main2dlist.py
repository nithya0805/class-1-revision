list=[[0,1]
      ,[2,3]
      ,[4,5]]
length = len(list)
print(length) # giving number of rows
#to get number of columns
column = len(list[0])
print(column)


for row in range(length):
    for col in range (column):
        print(list[row][col],end="\t")

    print()