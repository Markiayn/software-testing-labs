# Робота №07. Тестування

Poetry-проєкт для всіх чотирьох частин роботи. Python 3.14, Poetry.

## Частини
1. [Загальне тестування та юніт-тести](01_general_and_unittest/README.md)
2. Тестування з бібліотекою pytest — _в процесі_
3. Покриття коду — _в процесі_
4. Інтеграційне тестування — _в процесі_

## Запуск
```bash
poetry install
poetry run pytest -v
```
Або через `Makefile`: `make install`, `make test`, `make unit`, `make integration`, `make coverage`, `make html`, `make clean`.
