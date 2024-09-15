#zadanie 7 chisla fibonachi

debug = False

def fibonachi_numbers(iterations):
    a = 0
    b = 1
    unfull_summ = 0

    if iterations <= 20575: #итоговое число выходит за инт, если выполнить такое колво итераций
        for i in range(iterations):
            unfull_summ += a
            if debug: print("unfullsumm: ", unfull_summ)
            yield unfull_summ
            if debug: print("unfullsumm: ", unfull_summ)
            if debug: print("a and b before: ", a, " ", b)
            a ,b = b, a + b
            if debug: print("a and b after: ", a, " ", b)
            if debug: print("iteration: ", i)
    else:
        print("Слишком большое количество итераций, превышен лимит Int, максимальное значение: 20575")


generator = fibonachi_numbers(int(input("введите число итераций: ")))

for n in generator:
    print(f"Сумма: {n}")

