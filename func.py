print("please type 1 for X and 2 for O")

j=input("type 1 or 2")
if j==1:
    global j=X
    print(j)
elif j==2:
    global j =O
    print(j)
else:
    print("please type in 1 and 2 only")