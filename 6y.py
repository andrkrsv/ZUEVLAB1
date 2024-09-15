def complex_numbers_from_nested_list(nested_list):
    complex_numbers = []
    
    for sublist in nested_list:
        for elem in sublist:
            if isinstance(elem, complex):
                complex_numbers.append(elem)
    
    return tuple(complex_numbers)

nested_list = [
    [1, 2.5, 3 + 4j, 7, 3 - 3j, 5.5, 5.5, 3 + 6j, 12, 2323, 2 + 2j],
    [1.1, 2.2, 6 + 1j, 23, 32 - 8j, 52.4, 5 + 3j, 5.9, 3, 2, 23, 56 + 5j],
    [6, 2, 6 + 3j, 7.4, 23 - 8j, 3.5, 5, 323, 1.2, 3, 5 + 3j]
]

result = complex_numbers_from_nested_list(nested_list)
print(result)
