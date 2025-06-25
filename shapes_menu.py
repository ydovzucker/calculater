from circle import Circle
from general_triangle import GeneralTriangle
from hexagon import RegularHexagon
from rectangle import Rectangle
from right_triangle import RightTriangle
from square import Square

def main():
    while True:
        print("\n=== Shape Menu ===")
        print("1. Create Rectangle")
        print("2. Create Square")
        print("3. Create Circle")
        print("4. Create Right Triangle")
        print("5. Create General Triangle")
        print("6. Create Regular Hexagon")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        try:
            match choice:
                case "1":
                    w = float(input("Enter width: "))
                    h = float(input("Enter height: "))
                    shape = Rectangle(w, h)

                case "2":
                    s = float(input("Enter side length: "))
                    shape = Square(s)

                case "3":
                    r = float(input("Enter radius: "))
                    shape = Circle(r)

                case "4":
                    b = float(input("Enter base: "))
                    h = float(input("Enter height: "))
                    shape = RightTriangle(b, h)

                case "5":
                    a = float(input("Enter side 1: "))
                    b = float(input("Enter side 2: "))
                    c = float(input("Enter side 3: "))
                    shape = GeneralTriangle(a, b, c)

                case "6":
                    s = float(input("Enter side length: "))
                    shape = RegularHexagon(s)

                case "7":
                    print("Goodbye!")
                    break

                case _:
                    print("Invalid choice.")
                    continue

            print("\n--- Shape Info ---")
            print("Shape:", shape)
            print("Area:", round(shape.get_area(), 2))
            print("Perimeter:", round(shape.get_perimeter(), 2))

        except ValueError as ve:
            print("Error:", ve)