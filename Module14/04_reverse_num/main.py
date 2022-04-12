def mod(number):
    dot = False
    mod_int_part = ""
    mod_frac_part = ""
    for i in number:
        if i == ".":
            dot = True
        elif dot == False :
            mod_int_part = i + mod_int_part
        else:
            mod_frac_part = i + mod_frac_part
    mod_number = mod_int_part + "." + mod_frac_part
    return mod_number

number_1 = input("Введите первое число: ")
number_2 = input("Введите второе число: ")
mod_num_1 = mod(number_1)
mod_num_2 = mod(number_2)
print("\nПервое число наоборот:", mod_num_1)
print("Второе число наоборот:", mod_num_2)
summ = float(mod_num_1) + float(mod_num_2)
print("Сумма:", summ)

# зачет!
