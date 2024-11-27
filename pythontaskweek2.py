side1 = float(input("Enter the first side: "))
side2 = float(input("Enter the second side: "))
side3 = float(input("Enter the third side: "))

if side1==side2==side3:
    print("Equilateral")
else:    
     if side1==side2 or side3==side2 or side1==side3 :
        print('Isosceles')
     else:
         if side1+side2 > side3 and side2+side1 > side3 and side3+side1 > side2:
               print("Scalene")
         else:   
            print("Invalid Triangle")