def display_every_second_element(numbers):
    for i in range(0, len(numbers), 2):
        print(numbers[i])

lista = list(range(10))
display_every_second_element(lista)
