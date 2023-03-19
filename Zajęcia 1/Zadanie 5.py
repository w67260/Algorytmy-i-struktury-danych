tablica=[[1,2,3,4],[3,6,5,2],[6,0,9,6]]
for row in tablica :
    min_index=0
    min_value=row[0]
    for i in range(1,len(row)):
        if row[i]<min_value:
            min_index=i
            min_value = row[i]
        row[0], row[min_index]=row[min_index], row[0]