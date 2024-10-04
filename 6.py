zomb=int(input("How many zombies are there? "))
speed=int(input("How many people are bit a day by the zombies? "))
days=int(input("How many days has it been since the initial infection? "))
form = (zomb*speed)**days

if form <2:
    print("There is 1 zombie at the moment.")
else:
    print("There are", form, "zombies at the moment.")
