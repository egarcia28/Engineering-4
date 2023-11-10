import time
import board

def total_area (set1, set2, set3):
    try:
        set1 = set1.split(',')                  #splits each ordered pair at the comma
        set2 = set2.split(',')
        set3 = set3.split(',')

        x1 = float(set1[0])                     #assigns each x and y value to its own separate float
        y1 = float(set1[1])
        x2 = float(set1[0])
        y2 = float(set1[1])
        x3 = float(set1[0])
        y3 = float(set1[1])

        area = abs((x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/2)        #formula for area of ordered pair triangle

        return area

    except:                                                     #if invalid
        print("These points are invalid, try again")
        area = 0
        return area

while True:
    in1 = input("Enter the first (x,y) coordinate")
    in2 = input("Enter the second (x,y) coordinate")
    in3 = input("Enter the third (x,y) coordinate")

    area = total_area(in1, in2, in3)

    if area == 0:
        continue
    else:
        print(f"The area of the triangle with verticies ({in1}), ({in2}), ({in3}) is {area} square km.")