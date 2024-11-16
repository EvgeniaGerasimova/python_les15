import argparse


def main():
    # Создаем парсер аргументов
    parser = argparse.ArgumentParser(description='Обработка числа и строки с опциями.')

    # Добавляем обязательные аргументы
    parser.add_argument('number', type=int, help='Целое число')
    parser.add_argument('text', type=str, help='Строка для вывода')

    # Добавляем опции
    parser.add_argument('--verbose', action='store_true', help='Выводить дополнительную информацию')
    parser.add_argument('--repeat', type=int, default=1, help='Количество повторений строки (по умолчанию 1)')

    # Парсим аргументы
    args = parser.parse_args()

    # Обработка аргументов
    if args.verbose:
        print(f'Получено число: {args.number}')
        print(f'Получена строка: "{args.text}"')
        print(f'Количество повторений: {args.repeat}')

    # Вывод строки указанное количество раз
    for _ in range(args.repeat):
        print(args.text)


# Запуск основной функции
if __name__ == '__main__':
    main()

