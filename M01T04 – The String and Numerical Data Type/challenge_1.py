import math

#Get side 1
side1 = 0
while side1 <= 0:
    side1 = input("What is the value of side 1 of the triangle? ").strip()
    if side1 == '':
        print("Please enter a number for side 1 of the triangle")
        side1 = 0
        continue
    else:
        side1 = int(side1)
        if side1 <= 0:
            print("Side 1 must be greater than 0")
            side1 = 0
            continue
        else:
            break


#Get side 2
side2 = 0
while side2 <= 0:
    side2 = input("What is the value of side 2 of the triangle? ").strip()
    if side2 == '':
        print("Please enter a number for side 2 of the triangle")
        side2 = 0
        continue
    else:
        side2 = int(side2)
        if side2 <= 0:
            print("Side 2 must be greater than 0")
            side2 = 0
            continue
        else:
            break

#Get Side 3
side3 = 0
while side3 <= 0:
    side3 = input("What is the value of side 3 of the triangle? ").strip()
    if side3 == '':
        print("Please enter a number for side 3 of the triangle")
        side3 = 0
        continue
    else:
        side3 = int(side3)
        if side3 <= 0:
            print("Side 3 must be greater than 0")
            side3 = 0
            continue
        else:
            break

#Work out the semi perimeter
s = int(sum([side1, side2, side3]) / 2)

#Work out the area
area = round(math.sqrt( s * (s-side1) * (s-side2) * (s-side3) ), 2)

#Output te area to the console
print(f"The area of the triangle is {area}")