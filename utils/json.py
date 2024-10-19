import json

def load_json(file_path):
    """
    Загружает JSON файл и возвращает объект.

    :param file_path: Путь к JSON файлу.
    :return: Объект, представленный в JSON файле (обычно словарь).
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Файл не найден: {file_path}")
    except json.JSONDecodeError:
        print(f"Ошибка декодирования JSON в файле: {file_path}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# ! Обновляет существующий обьект 
def update_json_value(file_path, key_to_update, new_value):
    """
    Обновляет значение указанного ключа в JSON файле.

    :param file_path: Путь к JSON файлу.
    :param key_to_update: Ключ, значение которого нужно изменить.
    :param new_value: Новое значение для указанного ключа.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        def recursive_update(obj):
            if isinstance(obj, dict):
                for key, value in obj.items():
                    if key == key_to_update:
                        obj[key] = new_value
                    recursive_update(value)
            elif isinstance(obj, list):
                for item in obj:
                    recursive_update(item)

        recursive_update(data)

        # Сохранение обновленного объекта обратно в файл
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    except FileNotFoundError:
        print(f"Файл не найден: {file_path}")
    except json.JSONDecodeError:
        print(f"Ошибка декодирования JSON в файле: {file_path}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
