#First Program

sportspersons=["Virat","CR7","Messi","Bumrah","Stefan"]

print(f"The length of the list is {len(sportspersons)}\n")

sportspersons.append("DDP")
print(f"After adding a player to end {sportspersons}\n")

sportspersons.remove("DDP")
sportspersons.insert(2,"DDP")
print(f"After inserting the player after 2nd position {sportspersons}\n")

sportspersons.remove("DDP")
sportspersons.remove("Stefan")
sportspersons.extend(["Rajat","Magnus"])
print(f"After replacing two players {sportspersons}\n")

sportspersons.sort()
print(f"After sorting the players alphabetically {sportspersons}\n")

#Second Program

x=18
y=45
even_nums=[]
for num in range(x,y+1):
    if num%2==0:
       even_nums.append(num)
print(f"Even numbers in range of {x} and {y} is {even_nums}")       
