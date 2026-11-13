import random #библеотебка на рандом 

print("-- homework --")















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
Posinumbers = []
post = 1
post1 = 0
post2 = 0
post_done1 = 0
sum_posi_mid = 0
poster = 1
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
    if num %3 == 0:
        Three_mul *= num
    else:
        null += 0
    #
    if num == min(numbers):
        null += 0
    else:
        if num == max(numbers):
            null += 0
        else:
            middle_mul *= num
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
###
print("\n\tСумма отрицательных чисел =", Nega_sum,"\n\tСумма положительных чисел =", Posi_sum,"\n\tСумма нечётных чисел =", Odd_sum)
print("\tПроизведение элементов с индексами кратными трём =", Three_mul)
print("\tПроизведение элементов между минимальным и максимальным элементом =", middle_mul)
print("\tПСумму элементов, находящихся между первым и последним положительными элементами =", sum_posi_mid)













        
    
