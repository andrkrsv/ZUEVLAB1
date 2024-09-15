#zadanie 7 chisla fibonachi

debug = True

def fibonachi_numbers(iterations):
    a = 0
    b = 1
    unfull_summ = 0

    for _ in range(iterations):
        if debug: print("iteration: ", iterations)
        unfull_summ += a
        if debug: print("unfullsumm: ", unfull_summ)
        yield unfull_summ
        if debug: print("unfullsumm: ", unfull_summ)

        a = b
        b = a + b


print(fibonachi_numbers(int(input("введите число итераций: "))))