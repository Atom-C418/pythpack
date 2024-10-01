"""
create a program that an atc could use to calculate the flight time given the wind, speed, destination, and distance
a boeing 747 can go 576mph however they can travel much faster or slower depending on wind speed.
"""

wind=int(input("What is the wind speed (in mph, and negative if against, pos if with)? "))
dist=int(input("How far is the destination (in miles)? "))
speed=int(input("How fast are you going (for ref a Boeing 747 goes 576mph)? "))

print("It should take you", speed/(dist+wind), "hours.")