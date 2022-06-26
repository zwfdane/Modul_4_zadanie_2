# Kalkulator
import sys
import logging
logging.basicConfig(level=logging.DEBUG)

print("Ten program jest prostym kalkulatorem. Wybierz opcję.")

def addition(a, b):
    return a+b

def substraction(a, b):
    return a-b

def multiplication(a, b):
    return a*b
def division(a, b):
    if b == 0: 
      print("Nie dzieli się przez zero! Kończymy program.")
      quit()
    else:
      return a/b

while True:
    print("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")
    operation = input("Wybierz działanie:")
    if operation in ('1', '2', '3', '4'):
        value_1 = float(input("Podaj pierwszą liczbę:"))
        value_2 = float(input("Podaj drugą liczbę:"))
        if operation == '1':
            logging.info(f"Dodaję {value_1} do {value_2}")
            print(f"Wynik to: {addition(value_1, value_2)}")
        elif operation == '2':
            logging.info(f"Od {value_1} odejmuję {value_2}")
            print(f"Wynik to:  {substraction(value_1, value_2)}")
        elif operation == '3':
            logging.info(f"Mnożę {value_1} przez {value_2}")
            print(f"Wynik to: {multiplication(value_1,value_2)}")
        elif operation == '4':
            print(f"Wynik to:  {division(value_1, value_2)}")
            logging.info(f"Dzielę {value_1} przez {value_2}")
        next_calculation = input("Czy kontynuować?? (wpisz: *n* dla *nie*): ")
        if next_calculation == "n":
          break
    else: 
        print("Błędne dane. Kończymy program.")
        quit()


    
    
    

