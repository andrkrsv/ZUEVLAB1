#Задание 3 Заменить повторные гласные
def remove_doublewords(set_of_symbols: str):
  dicktionary = {"а":0, "у":0, "э":0, "о":0, "ы":0, "я":0, "ё":0, "ю":0, "е":0, "и":0}
  result = ""
  for i in set_of_symbols:
    try:
        if dicktionary[i] == 1:
            continue
        dicktionary[i]+=1
        result+=i
    except:
        result+=i
  return result


print(remove_doublewords(str(input())))