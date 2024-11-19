from helper.converter_helper import *


def main():
    print("Конвертер величин: імперські <-> метричні")
    print("1. Дюйми в сантиметри")
    print("2. Фути в метри")
    print("3. Фунти в кілограми")
    print("4. Сантиметри в дюйми")
    print("5. Метри в фути")
    print("6. Кілограми в фунти")
    choice = input("Оберіть тип конвертації (1-6): ")

    if choice == "1":
        value = float(input("Введіть кількість дюймів: "))
        print(f"{value} дюймів = {inches_to_centimeters(value):.2f} см")
    elif choice == "2":
        value = float(input("Введіть кількість футів: "))
        print(f"{value} футів = {feet_to_meters(value):.2f} м")
    elif choice == "3":
        value = float(input("Введіть кількість фунтів: "))
        print(f"{value} фунтів = {pounds_to_kilograms(value):.2f} кг")
    elif choice == "4":
        value = float(input("Введіть кількість сантиметрів: "))
        print(f"{value} см = {centimeters_to_inches(value):.2f} дюймів")
    elif choice == "5":
        value = float(input("Введіть кількість метрів: "))
        print(f"{value} м = {meters_to_feet(value):.2f} футів")
    elif choice == "6":
        value = float(input("Введіть кількість кілограмів: "))
        print(f"{value} кг = {kilograms_to_pounds(value):.2f} фунтів")
    else:
        print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
