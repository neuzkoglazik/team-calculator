# Team Calculator (Парный проект)

Простой консольный калькулятор для демонстрации командной разработки в Git и GitHub с использованием Pull Request и Канбан-подхода.

## Структура проекта
- `main.py` — основной файл с операциями калькулятора.
- `test_calculator.py` — модульные тесты для проверки функций.

## Запуск проекта
```bash
python3 main.py
```

## Запуск тестов
```bash
python3 -m unittest test_calculator.py
```

---

## Инструкция для напарника (создание Pull Request)

1. Клонировать репозиторий:
   ```bash
   git clone <URL_репозитория>
   cd team-calculator
   ```
2. Создать новую ветку под свою задачу (например, умножение):
   ```bash
   git checkout -b feature/multiply
   ```
3. Добавить функцию `multiply` в `main.py`:
   ```python
   def multiply(a: float, b: float) -> float:
       """Умножение двух чисел."""
       return a * b
   ```
4. Добавить тест для умножения в `test_calculator.py`.
5. Закоммитить и отправить ветку на GitHub:
   ```bash
   git add .
   git commit -m "feat: добавлена функция умножения"
   git push -u origin feature/multiply
   ```
6. На GitHub открыть **Pull Request** из ветки `feature/multiply` в `main`.

---

## Связь с Канбан-доской (Kanban)
- **To Do**: Задача спланирована.
- **In Progress**: Разработчик взял задачу и пишет код в ветке `feature/...`.
- **In Review / Code Review**: Открыт **Pull Request**. Проводится проверка кода и обсуждение.
- **Done**: Pull Request принят (merged) в ветку `main`.
