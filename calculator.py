# kalkulator
import sys
import logging
logging.basicConfig(level=logging.DEBUG)

print("Ten program jest prostym kalkulatorem. Wybierz opcję.")


def addition(a, b):
    logging.info(f"Dodaję {a} do {b}")
    return a+b

def substraction(a, b):
    logging.info(f"Od {a} odejmuję {b}")
    return a-b

def multiplication(a, b):
    logging.info(f"Mnożę {a} przez {b}")
    return a*b
def division(a, b):
    if b == 0: 
      print("Nie dzieli się przez zero! Kończymy program.")
      quit()
    else:
      logging.info(f"Dzielę {a} przez {b}")
      return a/b


def get_data(): # operation, value_1, value_2)
    print("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")
    operation = input("Wybierz działanie:")
    if operation in ('1', '2', '3', '4'):
        value_1 = float(input("Podaj pierwszą liczbę:"))
        value_2 = float(input("Podaj drugą liczbę:"))
    else: 
        print("Błędne dane. Kończymy program.")
        quit()
    return operation, value_1, value_2

operations = {
'1': addition,
'2': substraction,
'3': multiplication,
'4': division
}


# result = operation[value](value_1, value_2)

""" -- wersja z ifami
if __name__ == "__main__":
    while True:
        data = get_data()
        if  data[0] == '1':
                print(f"Wynik to: {addition(data[1], data[2])}")
        elif data[0] == '2':
                print(f"Wynik to:  {substraction(data[1], data[2])}")
        elif data[0] == '3':
                print(f"Wynik to: {multiplication(data[1], data[2])}")
        elif data[0] == '4':
                print(f"Wynik to:  {division(data[1], data[2])}")
        next_calculation = input("Czy kontynuować?? (wpisz: *n* dla *nie*): ")
        if next_calculation == "n":
            break    
"""
# https://stackoverflow.com/questions/21962763/using-a-dictionary-as-a-switch-statement-in-python
if __name__ == "__main__":
 while True:
    data = get_data()
    results = operations[data[0]](data[1],data[2])
    print(f"Wynik to {results}")
    next_calculation = input("Czy kontynuować?? (wpisz: *n* dla *nie*): ")
    if next_calculation == "n":
        break
    
    
    

