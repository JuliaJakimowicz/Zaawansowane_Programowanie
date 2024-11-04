def display_even_numbers(numbers):
    for number in numbers:
        if number % 2 == 0:
            print(number)


lista = list(range(10))
display_even_numbers(lista)
