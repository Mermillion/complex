import math
class Complex:
    def __init__(self, real=1.0, imag=0.0):
        self.real = real
        self.imag = imag

    def calculate_magnitude(self):
        return math.hypot(self.real, self.imag)

    def calculate_phase(self):
        return math.atan2(self.imag, self.real)

    def get_conjugate(self):
        return Complex(self.real, -self.imag)

    def raise_to_power(self, degree: int):
        if degree == 0:
            return Complex(1, 0)
        magnitude = self.calculate_magnitude() ** abs(degree)
        angle = self.calculate_phase() * degree
        real = magnitude * math.cos(angle)
        imag = magnitude * math.sin(angle)
        if degree > 0:
            return Complex(real, imag)
        else:
            reciprocal_magnitude = 1 / magnitude
            return Complex(reciprocal_magnitude * math.cos(-angle), reciprocal_magnitude * math.sin(-angle))

    def calculate_roots(self, n: int):
        if n <= 0:
            raise ValueError("Степень корня должна быть положительным числом.")
        roots = []
        magnitude = self.calculate_magnitude() ** (1 / n)
        base_angle = self.calculate_phase()
        for k in range(n):
            angle = (base_angle + 2 * math.pi * k) / n
            real = magnitude * math.cos(angle)
            imag = magnitude * math.sin(angle)
            roots.append(Complex(real, imag))
        return roots

    def add(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def subtract(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def multiply(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Complex(real, imag)

    def divide(self, other):
        denom = other.real ** 2 + other.imag ** 2
        real = (self.real * other.real + self.imag * other.imag) / denom
        imag = (self.imag * other.real - self.real * other.imag) / denom
        return Complex(real, imag)

    def is_equal_to(self, other):
        return math.isclose(self.real, other.real) and math.isclose(self.imag, other.imag)

    def display(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {abs(self.imag)}i"


def main():
    numbers = []  # Список для хранения всех созданных чисел
    current_index = None  # Индекс текущего выбранного числа

    while True:
        print("\n=== Работа с комплексными числами ===")
        if current_index is not None:
            print(f"Текущее выбранное число: {numbers[current_index].display()}")
        else:
            print("Текущее выбранное число: не выбрано")
        
        print("1. Ввести новое комплексное число")
        print("2. Выбрать другое число из списка")
        print("3. Показать модуль числа (|z|)")
        print("4. Найти аргумент числа (Arg(z))")
        print("5. Возвести в степень z^n")
        print("6. Найти корни n-й степени √z")
        print("7. Найти сопряжённое число z̅")
        print("8. Сложить два числа (z1 + z2)")
        print("9. Вычесть одно число из другого (z1 - z2)")
        print("10. Умножить два числа (z1 * z2)")
        print("11. Разделить одно число на другое (z1 / z2)")
        print("12. Показать список всех чисел")
        print("13. Выйти из программы")

        choice = input("Выберите действие (1-13): ")

        if choice == '1':
            try:
                real = float(input("Введите действительную часть: "))
                imag = float(input("Введите мнимую часть: "))
                new_number = Complex(real, imag)
                numbers.append(new_number)
                current_index = len(numbers) - 1
                print(f"Комплексное число успешно введено: {new_number.display()}")
            except ValueError:
                print("Ошибка: введите корректное число.")

        elif choice == '2':
            if numbers:
                print("Список доступных чисел:")
                for i, num in enumerate(numbers):
                    print(f"{i + 1}. {num.display()}")
                try:
                    selected_index = int(input("Введите номер числа для выбора: ")) - 1
                    if 0 <= selected_index < len(numbers):
                        current_index = selected_index
                        print(f"Вы выбрали число: {numbers[current_index].display()}")
                    else:
                        print("Ошибка: номер вне диапазона.")
                except ValueError:
                    print("Ошибка: введите корректное число.")
            else:
                print("Список чисел пуст. Сначала введите число (выберите пункт 1).")

        elif choice == '3':
            if current_index is not None:
                print(f"Модуль числа {numbers[current_index].display()} равен {numbers[current_index].calculate_magnitude()}")
            else:
                print("Сначала выберите или введите число (пункты 1 или 2).")

        elif choice == '4':
            if current_index is not None:
                print(f"Аргумент числа {numbers[current_index].display()} равен {numbers[current_index].calculate_phase()} радиан.")
            else:
                print("Сначала выберите или введите число (пункты 1 или 2).")

        elif choice == '5':
            if current_index is not None:
                try:
                    degree = int(input("Введите степень: "))
                    result = numbers[current_index].raise_to_power(degree)
                    numbers.append(result)
                    current_index = len(numbers) - 1
                    print(f"{numbers[current_index - 1].display()} в степени {degree}: {result.display()}")
                except ValueError:
                    print("Ошибка: введите корректную степень (целое число).")
            else:
                print("Сначала выберите или введите число (пункты 1 или 2).")

        elif choice == '6':
            if current_index is not None:
                try:
                    root_degree = int(input("Введите степень корня: "))
                    roots = numbers[current_index].calculate_roots(root_degree)
                    print(f"Корни {root_degree}-й степени из числа {numbers[current_index].display()}:")
                    for i, root in enumerate(roots):
                        print(f"Корень {i + 1}: {root.display()}")
                        numbers.append(root)
                except ValueError:
                    print("Ошибка: введите корректную степень (целое число).")
            else:
                print("Сначала выберите или введите число (пункты 1 или 2).")

        elif choice == '7':
            if current_index is not None:
                conjugate = numbers[current_index].get_conjugate()
                numbers.append(conjugate)
                current_index = len(numbers) - 1
                print(f"Сопряжённое число: {conjugate.display()}")
            else:
                print("Сначала выберите или введите число (пункты 1 или 2).")

        elif choice == '8':
            if current_index is not None and len(numbers) > 1:
                try:
                    other_index = int(input("Введите номер второго числа для сложения: ")) - 1
                    if 0 <= other_index < len(numbers):
                        result = numbers[current_index].add(numbers[other_index])
                        numbers.append(result)
                        current_index = len(numbers) - 1
                        print(f"Результат сложения: {result.display()}")
                    else:
                        print("Ошибка: номер вне диапазона.")
                except ValueError:
                    print("Ошибка: введите корректное число.")
            else:
                print("Сначала выберите два числа для операции (пункты 1 и 2).")

        elif choice == '12':
            if numbers:
                print("Список всех чисел:")
                for i, num in enumerate(numbers):
                    print(f"{i + 1}. {num.display()}")
            else:
                print("Список чисел пуст. Введите новое число (выберите пункт 1).")

        elif choice == '13':
            print("Выход из программы. До свидания!")
            break

        else:
            print("Некорректный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
