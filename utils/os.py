import os

def list_files_in_directory(directory):
    """
    Возвращает список названий файлов в указанной директории.

    :param directory: Путь к директории.
    :return: Список названий файлов.
    """
    try:
        files = os.listdir(directory)  # Получаем список всех файлов и папок в директории
        return [f for f in files if os.path.isfile(os.path.join(directory, f))]  # Фильтруем только файлы
    except FileNotFoundError:
        print(f"Директория не найдена: {directory}")
        return []
