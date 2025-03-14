import math 

# Tworzymy dwie listy do połączenia za pomocą funkcji zip()
numbers = [1, 2, 3, 4]
letters = ['a', 'b', 'c', 'd']

# Łączymy listy w pary
zipped = list(zip(numbers, letters)) #Funkcja zipped zwraca połączone listy
print("Połączone listy:", zipped)  

try:
    value = -9  # Liczba ujemna, dla której sqrt() zwraca ValueError
    result = math.sqrt(value)  # Funkcja sqrt() zwraca pierwiastek kwadratowy liczby
    print("Pierwiastek kwadratowy:", result)
except ValueError as e:
    print("Błąd:", e)  # Obsługa błędu ValueError

# Link do dokumentacji zip(): https://docs.python.org/3/library/functions.html#zip
# Link do dokumentacji math.sqrt(): https://docs.python.org/3/library/math.html#math.sqrt
# Link do dokumentacji ValueError: https://docs.python.org/3/library/exceptions.html#ValueError
