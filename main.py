"""Простой модульный калькулятор для командной работы."""

def add(a: float, b: float) -> float:
    """Сложение двух чисел."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Вычитание второго числа из первого."""
    return a - b

def divide(a: float, b: float) -> float:
    """Деление первого числа на второе."""
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a / b

if __name__ == "__main__":
    print("=== Командный калькулятор ===")
    print("5 + 3 =", add(5, 3))
    print("10 - 4 =", subtract(10, 4))
    print("20 / 4 =", divide(20, 4))
    print("\nОжидается добавление новых операций через Pull Request!")
