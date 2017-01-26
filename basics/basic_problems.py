print("Hello")
print(5 * 25)


# sum two

def sum_two(num1, num2):
    return num1 + num2

print(sum_two(1, 3))
print(sum_two(100, 325))

# square

def square_num(num):
    return num * num

print(square_num(5))
print(square_num(10))

# check if even

def check_even(num):
    return num % 2 == 0

print check_even(2)
print check_even(5)

# check if odd

def check_odd(num):
    return num % 2 != 0

print check_odd(3)
print check_odd(6)

# string length

def str_len(my_string):
    return len(my_string)

def str_len2(my_string):
    count = 0
    for letter in my_string:
        count += 1
    return count

print str_len("Lyndon")
print str_len("Lawrence")
print str_len2("Lyndon")
print str_len2("Lawrence")

# check last letter

def last_letter(my_string):
    return my_string[-1]

print last_letter("Lyndon")
print last_letter("Pikachu")

# find max of 2 numbers

def max_number(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

print(max_number(2, 5))
print(max_number(15, 4))

# find max of 3 numbers

def max_of_3(num1, num2, num3):
    return max_number(max_number(num1, num2), num3)

def using_max(num1, num2, num3):
    return max(num1, num2, num3)

print(max_of_3(3, 5, 7))
