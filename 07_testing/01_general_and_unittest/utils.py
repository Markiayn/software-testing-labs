"""Допоміжні функції для завдань «Перевірка даних», «Тестування функцій» і mock."""

VOWELS = "aeiouаеєиіїоуюя"  # англійські + українські голосні


def check_number(value: str) -> int:
    """Перевіряє введене число: має бути цілим і більшим за нуль."""
    value = value.strip()
    if not value:
        raise ValueError("Число не може бути порожнім")
    try:
        number = int(value)
    except ValueError:
        raise ValueError(f"'{value}' не є цілим числом")
    if number <= 0:
        raise ValueError("Число має бути більшим за нуль!")
    return number


def create_name(name):
    if not name:
        raise ValueError("Ім'я не може бути порожнім")
    return name


def count_symbols(text: str) -> int:
    return len(text)


def divide(a: float, b: float) -> float:
    return a / b


def count_vowels(text: str) -> int:
    """Рахує голосні літери (латиниця та кирилиця) без урахування регістру."""
    return sum(1 for letter in text.lower() if letter in VOWELS)


def ask_number() -> int:
    """Просить користувача ввести число і повертає перевірене значення."""
    return check_number(input("Введіть додатне число: "))


if __name__ == "__main__":
    # Ручна перевірка check_number для правильного і неправильного введення
    for raw in ["5", " 42 ", "0", "-3", "abc", ""]:
        try:
            print(f"{raw!r} -> {check_number(raw)}")
        except ValueError as error:
            print(f"{raw!r} -> ValueError: {error}")
