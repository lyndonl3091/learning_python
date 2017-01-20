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
