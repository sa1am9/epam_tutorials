
def check(string1: str) -> int:  # А иногда может и ошибку

    # Поймёшь дальше зачем это
    # А вообще мы просто упрощаем жизнь, конвертируя два знака в один.
    flags = {"+-": "-", "-+": "-", "++": "+", "--": "+",
             "+": "+", "-": "-"}

    """Проверка на коректность

    Что бы в начале не было 2 символов. И в конце вообще символа.

    """
    assert all(string1[:2] != x for x in ("++", "+-", "--", "-+")),\
        "Incorrect input"
    assert all(string1[-2:] != x for x in ("++", "+-", "--", "-+")),\
        "Incorrect input"


        # Опять же можно оставить плюс и минус
        # только как последние елементы, но мне лень.

    """Проверка на коректность

    Что бы небыло 3 символа и более подряд.

    """
    flags_list = []  # Попутно будем запоминать какие у нас знаки
    sign = ""    # Сюда будем запихивать знак
    for i in string1:
        if not i.isdigit():
            sign += i
            assert len(sign) < 3, "Incorrect input"
        else:
            if sign !="": flags_list.append(sign)
            sign = ""

    """Разделяй и властвуй

    Записываем цифры в масив. 
    Можно было и в прошлом цикле, но мне лень переделывать.

    """
    digits =[]  # Сюда складываем наши числа
    digit = ""  # Это наше число
    for i in string1:
        if i.isdigit():
            digit += i
        else:
            if digit != "": digits.append(digit)
            digit = ""
    digits.append(digit)

    # Переделываем знаки согласно нашему словарю.
    flags_list = [flags[k] for k in flags_list]

    # Вдруг первый елемент со знаком
    if string1[0] == "-":
        result = -1*int(digits[0])
    else:
        result = 1 * int(digits[0])

    # Складываем всё во единно
    for i in range(1, len(digits)):
        result += int(flags_list[i-1]+digits[i])

    print("result of formula = ", result)
    return result


string1 = "1+-3+11"
check(string1)
