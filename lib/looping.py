# 1. Countdown using a while loop
def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")

# 2. Square a list of integers using a for loop or list comprehension
def square_integers(int_list):
    # You can do this with a for loop:
    # squares = []
    # for num in int_list:
    #     squares.append(num ** 2)
    # return squares

    # Or more concisely with a list comprehension:
    return [num ** 2 for num in int_list]

# 3. FizzBuzz from 1 to 100
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
