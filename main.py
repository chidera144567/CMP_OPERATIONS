from math import Math
from physics import Physics
phy = Physics()
mth = Math()
print("welcome to our math and physics opration")
operators  = input("what operation would you like to carry out\n>math or physics ")
if operators == "math":
    print(" you can \n+, -, *, /, and find exponent of a number (^)")
    num1 = int(input("first num\n> "))
    num2 = int(input("second num\n> "))
    ops = input("enter the operation you want to carry out\n>")
    if ops == "-":
        print(mth.minus())
    if ops == "+":
        print(mth.add(num1, num2))
    if ops == "*":
        print(mth.multiply(num1, num2))
    if ops == "/":
        print(mth.divide(num1, num2))
    if ops == "^":
        print(mth.exponent(num1, num2))



if operators == "physics":
    print("you can calculate speed, potential energy, force ")
    ops = input ("what operation do you want to carry out").lower()
    if ops == "speed":
        num1 = int(input("distance\n> "))
        num2 = int(input("time\n\> "))
        print(phy.calc_speed())
    if ops == "potential energy ":
        num1 = int(input("mass\n> "))
        num2 = int(input("height\n> "))
        print(phy.calc_PE())
    if ops == "force ":
        num1 = int(input("mass\n>"))
        num2 = int(input("acceleration\n>"))
        print(phy.calc_force())
    if ops == "velocity":
        num1 = int(input("initial velocity\n> "))
        num2 = int(input("acceleration\n> "))
        num3 = int(input("time\n> "))
        print(phy.pressure(num1, num2, num3))
    if ops == "pressure":
        num1 = int(input("force\n> "))
        num2 = int(input("acceleration\n> "))
        print(phy.pressure(num1, num2))