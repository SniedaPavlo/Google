# Функция для вычисления разницы в днях
def calculate_days_difference(date1, date2):
    date1_str = str(date1)
    date2_str = str(date2)
    # Разбиваем строки на компоненты
    year1, month1, day1 = map(int, date1_str.split('-'))
    year2, month2, day2 = map(int, date2_str.split('-'))
    
    # Преобразуем обе даты в количество дней с начала эпохи
    days1 = year1 * 365 + month1 * 30 + day1  # Простой расчет
    days2 = year2 * 365 + month2 * 30 + day2  # Простой расчет
    
    # Возвращаем абсолютное значение разницы
    return abs(days1 - days2)
