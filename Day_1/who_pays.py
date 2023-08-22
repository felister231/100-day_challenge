import random
#get_names = input("Enter the names of your friends separated by a comma").split(",")
#who_pays = random.randint(0,len(get_names) - 1)
#you_pay = get_names[who_pays]
#print(f"{you_pay} is the one going to pay today. Sorry!")

# you can also get the sme using choice function
get_names = input("Enter the names of your friends separated by a comma").split(",")
print(f"{random.choice(get_names)} will pay the bill. Sorry!\n I promise next time it will be someone esle")
      #print(f"{who_pays} is the one going to pay today. Sorry!")





