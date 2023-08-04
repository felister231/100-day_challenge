print("Welcome to the love calculator")
my_name = input("What is your name?\n")
their_name = input("What is their name\n")

two_names = my_name.lower() + their_name.lower()
t = two_names.count("t")
r = two_names.count("r")
u = two_names.count("u")
e1 = two_names.count("e")

l = two_names.count("l")
o = two_names.count("o")
v = two_names.count("v")
e = two_names.count("e")

true = t + r + u  + e1
love = l + o + v + e
true_loveScore = int(str(true) + str(love))
if (10 < true_loveScore) or (true_loveScore > 90):
    print(f"Your score is {true_loveScore} you go together like coke and methos")
elif(true_loveScore >= 40) and (true_loveScore <= 50):
    print(f"Your score is {true_loveScore} and you are alright together")
else:
    print("Your score is {true_loveScore}")




                   