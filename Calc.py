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
        equation = str(input("Введите уравнение\n"))
        equation.replace(" ", "")
        simvols = "1234567890()-+/*%."
        try:
            print(f'{equation} = {(eval(str(equation)))}')
            for i in equation:
                if i not in simvols:
                    pass
        except NameError:
            print("Вы ввели не верное значение ")
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

