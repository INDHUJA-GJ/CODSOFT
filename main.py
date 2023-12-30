import random
n=int(input("Enter the length of the password:"))
d= ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
a= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                         'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                         'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                         'z']
A = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                         'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                         'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                         'Z']
s= ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
               '*', '(', ')', '<']
final=""
for i in range(n):
    z=random.randint(1,4)
    if z==1:
        d = random.choice(d)
    if z==2:
        d= random.choice(a)
    if z==3:
        d= random.choice(A)
    if z==4:
        d= random.choice(s)
    final=final+d
print("The password is:",final)

