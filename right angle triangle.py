a_length = int(input("WHAT IS A_LENGTH?")) #can be adjacent or the opposite
b_length = int(input("WHAT IS b_LENGTH?")) #can be adjacent or the opposite
c_length = int(input("WHAT IS c_LENGTH?")) #hypotenuse
if c_length**2 == a_length**2 + b_length**2: #uses pyhtagoras' theorem
    print("this is a right angle triangle") #if a^2 and b^2 = c^2 , it is a right angle triangle
else:
    print("not a right angle triangle") #if a^2 and b^2 =/= c^2 , it is not a right angle triangle