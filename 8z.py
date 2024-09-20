debug = False

def fibonachi_numbers(iterations):
    a = 0
    b = 1
    unfull_summ = 0

    if iterations <= 20575: 
        for i in range(iterations):
            unfull_summ += a
            if debug: print("unfullsumm: ", unfull_summ)
            yield unfull_summ
            if debug: print("unfullsumm: ", unfull_summ)
            if debug: print("a and b before: ", a, " ", b)
            a, b = b, a + b
            if debug: print("a and b after: ", a, " ", b)
            if debug: print("iteration: ", i)
    else:
        print("Слишком большое количество итераций, превышен лимит Int, максимальное значение: 20575")


iterations = int(input("введите число итераций: "))
min_digits = int(input("Введите минимальное количество значащих цифр: "))


generator = fibonachi_numbers(iterations)

index = 0

for n in generator:
    if len(str(n)) > min_digits:
        print(f"Первое число с более чем {min_digits} цифрами: {n}, на индексе: {index}")
        break 
    index += 1 
