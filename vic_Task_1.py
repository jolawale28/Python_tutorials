radius = float(input("please type the radius of the circle:"))
prefered_working = input("State here if you want python to calculate the  1.Area, 2.Circumference or 3.both: ")

Area = 3.142 * radius * radius
Circumference = 2 * 3.142 * radius

if(prefered_working == "1"):
    print(f"The Area is: {round(Area)}")
elif(prefered_working == "2"):
    print(f"The Circumference is: {round(Circumference)}")
else:
    print(f"The Area is: {round(Area)}, and The Circumference is:{round(Circumference)}")