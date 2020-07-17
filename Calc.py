"""ДЗ 2. Реализация калькуляции"""

def Y_or_N():
    while True:
        replay = str(input("Хотите ли вы повторить вычисление, если да Y если нет N\n"))
        if replay.lower() == "y":
            return "y"
        if replay.lower() == "n":
            return "n"
        else:
            print("Введите Y или N")
            continue


def Calculator():
    """Функция для вычисления арифметической операции"""
    while True:
        c = ""
        result = []
        equation = input("Введите уравнение\n")
        equation.replace(" ", "")
        simbols = "1234567890()-+/*%."
        try:
            for i in equation:
                if i in simbols:
                    result.append(i)
            print(result,"----")
            print((eval((c.join(result)))))


        except OverflowError:
            print("Результат арифметической операции слишком велик для представления")
        except ZeroDivisionError:
            print("Деление на ноль, не возможно")
        except SyntaxError:
            print("Возможно вы ввели синтаксически не верное условие")

        finally:

            replay = Y_or_N()
            if replay == "y":
                continue
            elif replay == "n":
                return print("Хорошего дня")

Calculator()

