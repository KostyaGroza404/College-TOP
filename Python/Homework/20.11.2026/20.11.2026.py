
while True:
    task = int(input("\tВыберите задание:\n\t1 -\n\t2 -\n\t3 - \n\t:"))
    if task == 1:
        n1 = int(input("Введите начало диапозона: "))
        n2 = int(input("Введите конец диапозона: "))
        sum_odd = 0
        sum_even = 0
        sum_nine = 0
        odd_num = 0
        even_num = 0
        nine_num = 0
        for i in range(n1,n2+1):
            if i % 2 == 0:
                sum_even += i
                even_num += 1
            else:
                sum_odd += i
                odd_num += 1
        for i in range(n1,n2+1):
            if i % 9 == 0:
                sum_nine += i
                nine_num += 1
            else:
                pass
        if sum_even == 0 or sum_even == 0:
            print("Нет чётных чисел")
        else:
            print("Сумма чётных чисел: ",sum_even,"\tСреднее арифметическое: ", sum_even/even_num)
        if sum_odd == 0 or sum_odd == 0:
            print("Нет нечётных чисел")
        else:
            print("Сумма нечётных чисел: ",sum_odd,"\tСреднее арифметическое: ", sum_odd/odd_num)
        if sum_nine == 0 or sum_nine == 0:
            print("Нет чисел делящихся нацело на 9")
        else:
            print("Сумма чисел делящихся нацело на 9: ",sum_nine,"\tСреднее арифметическое: ", sum_nine/nine_num)
    elif task == 2:
        n = int(input("Введите длинну линии: "))
        for i in range(n):
            print("#")
    elif task == 3:
        while True:
            n = int(input("Введите число[7 для выхода из задания]: "))
            if n == 7:
                print("Good bye!")
                break
            else:
                if n == 0:
                    print("Number is equal to zero")
                else:
                    if n < 0:
                        print("Number is negative")
                    else:
                        print("Number is positive")
    elif task == 4:
        k = 1
        list = []
        while k == 1:
            n = int(input("Введите число[7 для выхода из задания и результатов]: "))
            if n == 7:
                k = 0
            else:
                list.append(n)
        
        print("минимум = ", min(list))
        print("максимум = ", max(list))
        print("сумма = ", sum(list))

        print("Good bye!")
    else:
        print("неизвестное задание")
    end = input("Нажмите любую клавишу чтобы начать заново")
