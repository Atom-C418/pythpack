numb = int(input("Give me a number and I will perform some moves with it: "))

move1 = 2**numb
move2 = numb*2
move3 = 100-numb

print("If I perform move number 1 you would get:", move1)
print("If I perform move number 2 you would get:", move2)
print("If I perform move number 3 you would get:", move3)

"""
number: 3   2   1   7   10   15     100
move 1: 8   4   2   128 1024 32768  126765060022822940149670325376
move 2: 6   4   2   14  20   30     200
move 3: 97  98  99  93  90   85     0
"""