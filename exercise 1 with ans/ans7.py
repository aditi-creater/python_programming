print("Question 7: - The distance between two cities (in km.) is input through the keyboard. Write a program to convert and print this distance in meters, feet, inches and centimetres.")
distance=float(input("enter the distance in km:"))
meters=(distance*1000)
print("the distance in meters is:",meters)
feet=(distance*3280.84)
print("the distance in feet is:",feet)
inches=(distance*39370.1)
print("the distance in inches is:",inches)
centimeters=(distance*1000*100)
print("the distance in centimeters is:",centimeters)

