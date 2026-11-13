import random #библеотебка на рандом 

print("-- homework --")
task = int(input("Выберите задание:\n1 - Ужас\n2 - Попроще\n: "))


if task == 1:
    #----------------------------------
    numbers = []
    for i in range(10):
        number = random.randint(-100, 100)
        numbers.append(number)
        
    print("Cписок: ", numbers)
    ###
    Nega_sum = 0
    Posi_sum = 0
    Odd_sum = 0
    null = 0
    Three_mul = 1
    middle_mul = 1
    post = 0
    post1 = 0
    post2 = 0
    post_done1 = 0
    sum_posi_mid = 0
    poster = 0
    Tree_post1 = 0
    Tree_post2 = 0
    Jonkler = 0
    ##
    for num in numbers:
        if num < 0:
            Nega_sum += num
        elif num > 0:
            Posi_sum += num
            if post_done1 == 0:
                post1 += post
                post_done1 += 1
            else:
                post2 = post
        else:
            null += 0
        #
        if num %2 == 1:
            Odd_sum += num
        else:
            null += 0
        #
        if post %3 == 0:
            Three_mul *= num
        else:
            null += 0
        #
        if num == min(numbers):
            Tree_post1 = post
        else:
            null += 0
        if num == max(numbers):
            Tree_post2 = post
        else:
            null += 0
        #
        post += 1
    ##
    for numb in numbers:
        if post2 - post1 >= 2:
            if poster > post1 and poster < post2:
                sum_posi_mid += numb
        else:
            null += 0
        poster += 1
    ##
    for numb in numbers:
        if Tree_post2 - Tree_post1 >= 2:
            if Jonkler > Tree_post1 and Jonkler < Tree_post2:
                middle_mul *= numb
        elif Tree_post2 - Tree_post1 <= -2:
            if Jonkler < Tree_post1 and Jonkler > Tree_post2:
                middle_mul *= numb
        else:
            middle_mul = 0
        Jonkler += 1
    ###
    print("\n\tСумма отрицательных чисел =", Nega_sum,"\n\tСумма положительных чисел =", Posi_sum,"\n\tСумма нечётных чисел =", Odd_sum)
    print("\tПроизведение элементов с индексами кратными трём =", Three_mul)
    print("\tПроизведение элементов между минимальным и максимальным элементом =", middle_mul)
    print("\tСумму элементов, находящихся между первым и последним положительными элементами =", sum_posi_mid)
    #----------------------------------
elif task == 2:
    #----------------------------------
    numbers = []
    for i in range(10):
        number = random.randint(-100, 100)
        numbers.append(number)
        
    print("Cписок: ", numbers)
    ###
    even_num = []
    odd_num = []
    posi_num = []
    nega_num = []
    null = 0
    ##
    for num in numbers:
        if num % 2 == 0:
            even_num.append(num)
        else:
            odd_num.append(num)
        if num > 0:
            posi_num.append(num)
        elif num < 0:
            nega_num.append(num)
        else:
            null += 0
    ###
    print("Список чётных: ",even_num)
    print("Список нечётных: ",odd_num)
    print("Список положительных: ",posi_num)
    print("Список отрицательных: ",nega_num)
    #----------------------------------
else:
    print("Неизвестное задание")
    #--#

    # - PS
    # Не спрашивайте как я сделал первую часть я знаю это ужас    








        
    
