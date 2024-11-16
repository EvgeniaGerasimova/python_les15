from datetime import datetime, timedelta


def get_future_date(days_ahead):
    # Получаем текущую дату
    current_date = datetime.now()

    # Создаем объект timedelta
    future_date = current_date + timedelta(days=days_ahead)

    # Форматируем дату в нужный формат
    formatted_future_date = future_date.strftime('%Y-%m-%d')

    return formatted_future_date


# Пример использования функции
days = 10  # Количество дней
result_date = get_future_date(days)
print(f'Дата через {days} дней будет: {result_date}')

