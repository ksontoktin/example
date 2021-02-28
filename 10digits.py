%%time

# попробуем сделать грубый поиск, потому что это не должно быть сверхзатратно
# сразу можно отметить, что можно искать не 10-значные числа, а 8-значные, так как на 9 место подойдёт любое число не ноль
# а на 10-м месте стоит ноль, как и на 5-ом стоит 5

cool = []

for i in range(12345678, 98765432):
    
    # проверим, что все цифры должны быть разными
    digits = [int(d) for d in str(i)]
    
    if len(set(digits)) >= 8:
        if 0 not in digits:
            if digits[4] == 5:
                if digits[1] % 2 == 0:
                    if (digits[0] + digits[1] + digits[2]) % 3 == 0:
                        if (digits[2] * 10 + digits[3]) % 4 == 0:
                            if (digits[3] + digits[4] + digits[5]) % 3 == 0:
                                if digits[5] % 2 == 0:
                                    if (digits[0] * 1000000 + digits[1] * 100000 + digits[2] * 10000 + digits[3] * 1000 + digits[4] * 100 + digits[5] * 10 + digits[6]) % 7 == 0:
                                        if (digits[5] * 100 + digits[6] * 10 + digits[7]) % 8 == 0:
                                            cool.append(i)
                                           
print(cool)                                           
