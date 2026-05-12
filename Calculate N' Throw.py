h=int(input("Enter the height of your object(inches):"))
l=int(input("Enter the length of your object(inches):"))
w=int(input("Enter the width of your object(inches):"))
wall_toss=int(h*l*w)
print("Here is your object's dimensions:",
"height:",h,"length",l,"and width",w)
print("Here's your objects area:",wall_toss)
print("And here's a bonus: your object thrown at a wall!")
if wall_toss==(0):
    print("*splat* D Class destruction!")
elif wall_toss in range (1,250):
    print('*clang* C Class destruction!')
elif wall_toss in range(251,750):
    print("*clooong* B Class destruction!")
elif wall_toss in range(751,1500):
    print("*CLLLOOOOOOOOOOOOOONNNNNKKKKK* A Class destruction!")
else:
    print("!$#@%^!Why can't I throw this? Emotional Damage destruction!")
