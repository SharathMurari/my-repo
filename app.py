mylist=[10,2,30,2,15]
mylist2 = mylist.copy()
mylist2.sort()
print(mylist2)
print(mylist)
for x in mylist:
    if x==2:
        print("yes")

if 2 in mylist2:
    print("yes")