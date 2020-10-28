# Задание по программированию: Декоратор to_json
import json
import functools

# Декоратор - функция котрая принимает и возвращает функцию
def to_json(func):
    @functools.wraps(
        func
    )  # Ипользуем функцию-декоратор wraps чтобы сохранить название передаваемой функции
    def wrapper(*args, **kwargs):
        return json.dumps(
            func(*args, **kwargs)
        )  # Сериализация возвращаемого значения функции

    return wrapper


@to_json
def get_data():
    return {"data": 42}


print(get_data.__name__)