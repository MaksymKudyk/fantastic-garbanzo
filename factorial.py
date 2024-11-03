class FactorialCalculator:
    cache = {}

    @staticmethod
    def factorial(n):
        if n in FactorialCalculator.cache:
            return FactorialCalculator.cache[n]
        if n == 0 or n == 1:
            FactorialCalculator.cache[n] = 1
            return 1
        result = n * FactorialCalculator.factorial(n - 1)
        FactorialCalculator.cache[n] = result
        return result

    @staticmethod
    def input_number():
        while True:
            try:
                n = int(input("Введіть ціле додатне число для обчислення факторіала: "))
                if n < 0:
                    print("Число має бути додатним. Спробуйте ще раз.")
                else:
                    return n
            except ValueError:
                print("Будь ласка, введіть ціле число.")

    @staticmethod
    def calculate_from_input():
        while True:
            n = FactorialCalculator.input_number()
            result = FactorialCalculator.factorial(n)
            print(f"Факторіал числа {n} дорівнює: {result}")

            repeat = input("Бажаєте обчислити ще одне число? (так/ні): ").strip().lower()
            if repeat != "так":
                print("Програма завершена.")
                break


FactorialCalculator.calculate_from_input()