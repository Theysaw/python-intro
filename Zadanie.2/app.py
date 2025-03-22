import re
from datetime import datetime
from typing import List

def is_valid_email(email: str) -> bool:
    """Sprawdza poprawność adresu e-mail."""
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

def calculate_area(shape: str, **kwargs) -> float:
    """Oblicza pole figury geometrycznej (koło, kwadrat, prostokąt)."""
    if shape == "circle":
        return 3.14159 * (kwargs.get("radius", 0) ** 2)
    elif shape == "square":
        return kwargs.get("side", 0) ** 2
    elif shape == "rectangle":
        return kwargs.get("width", 0) * kwargs.get("height", 0)
    else:
        raise ValueError("Nieobsługiwany typ figury.")

def process_list(data: List[int], operation: str) -> List[int]:
    """Przetwarza listę danych: filtruje liczby parzyste lub sortuje."""
    if operation == "filter_even":
        return [x for x in data if x % 2 == 0]
    elif operation == "sort":
        return sorted(data)
    else:
        raise ValueError("Nieznana operacja.")

def convert_date_format(date_str: str, current_format: str, new_format: str) -> str:
    """Konwertuje format daty."""
    try:
        date_obj = datetime.strptime(date_str, current_format)
        return date_obj.strftime(new_format)
    except ValueError:
        raise ValueError("Nieprawidłowy format daty.")

def is_palindrome(text: str) -> bool:
    """Sprawdza, czy tekst jest palindromem."""
    cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', text.lower())
    return cleaned_text == cleaned_text[::-1]

# Przykładowe testy funkcji
if __name__ == "__main__":
    print(is_valid_email("test@example.com"))  # True
    print(calculate_area("circle", radius=5))  # 78.53975
    print(process_list([1, 2, 3, 4, 5], "filter_even"))  # [2, 4]
    print(convert_date_format("15-03-2025", "%d-%m-%Y", "%Y/%m/%d"))  # 2025/03/15
    print(is_palindrome("Ala ma kota"))  # False
