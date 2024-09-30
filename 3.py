L=int(input("How long is the area you're putting turf in? "))
W=int(input("How wide? "))
cost=int(input("What is the ft^2 cost? "))

print("The area is", L*W+"square feet.")
print("The perimeter is", L+W+W+L, "feet around.")
print("The cost to put the turf down is", cost*L*W, "dollars.")