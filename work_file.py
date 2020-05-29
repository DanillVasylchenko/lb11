'''
2-й Варіант


а) Дан двійковий файл f, компоненти якого є цілими числами. Отримати в файлі g
всі компоненти файлу f, що діляться на 3 і не діляться на 5.
б) Дан текстовий файл f. Отримати файл g, утворений з файлу f заміною символів
- цифр на поєднання букв, що позначають відповідну цифру (наприклад, '1' - 'один').

Васильченко Даниїл 122 А
'''
from random import randint


def task_a():
    # а)
    f = open('f.txt', 'wb')
    f.write(bytearray([randint(0, 255) for i in range(int(input("Скільки цілих чисел Ви хочете ввести: ")))]))
    f.close()

    f = open('f.txt', 'rb')
    x = f.read()
    f.close()

    print("Дані файлу f: ", x)

    nums = ''
    for el in x:
        if el % 3 == 0 and el % 5 != 0:
            print(f"Компонента ({bytes([el])} = {el}) задовільняє умову ділення на 3 без остачі і на 5 - з остачею.")
            nums += str(el) + '\n'

    g = open('g.txt', 'w')
    g.write(nums)
    g.close()


# б)
def task_b():
    f = open('f.txt', 'w')
    start, end = int(input("Мінімальне можливе число: ")), int(input("Введіть максимальне можливе число: "))
    nums = ''.join([str(randint(start, end))
                    for i in range(int(input("Введіть кількість чисел: ")))])
    f.write(nums)
    f.close()
    f = open('f.txt', 'r')
    x = f.read()
    f.close()

    dictionary = {0: "нуль", 1: "один", 2: "два", 3: "три", 4: "чотири", 5: "п\'ять", 6: "шість", 7: "сім", 8: "вісім",
                  9: "дев'ять"}

    nums_str = ''
    for i in x:
        if i == '-':
            nums_str += '-'
        else:
            value = dictionary.get(int(i))
            nums_str += value
            print(f"{i} - {value}")

    g = open('g.txt', 'w')
    g.write(nums_str)
    g.close()


question = input("Введіть 'a' - завдання A\n"
                 "Введіть 'b' - завдання B\n"
                 "Введіть що-небудь інше для завершення.\n")
if question == 'a':
    task_a()
elif question == 'b':
    task_b()