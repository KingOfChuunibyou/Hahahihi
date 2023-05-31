

# user_input = input("Put your input: ")

# while user_input != "exit":
#     print(user_input)
#     user_input = input("Put your input: ")

# n = input("You're in the Lost Forest. Go left or right? ")
# while n == "right":
#     n = input("You're in the Lost Forest. Go left or right? ")
# print("You got out of the Lost Forest!")

while True:
    user_input = input("Put your input: ")
    if user_input == "exit":
        break
    print(user_input)

print("SAYA BEBASS!!")

# mysum = 0 (LINE 1)
# for i in range(5,11, 12): (LINE 2) | 
## i = 5
### mysum += i (LINE 3) | mysum = 0 + 5 = 5
### if mysum == 5 | 5 == 5 | True
#### break (LINE 4) | break the loop
## print(mysum) | print 5

for i in range(1,4):
    print(i)
    for j in range(3,10):
        print(j)
        break