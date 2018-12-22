# finding a pair in an array who's addition is a given number
arr = [1,2,3,4,5]
addn = 6
for index,item in enumerate(arr):
    key = addn - item
    a = index + 1
    for a,ite in enumerate(arr):
        if(key==ite):
            print (item,ite)
