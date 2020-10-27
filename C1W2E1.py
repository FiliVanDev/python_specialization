# Задание по программированию: Key-value хранилище
import os
import tempfile
import json
import argparse


storage_path = os.path.join(tempfile.gettempdir(), "storage.data")

# Функция для чтнения данных из файла
def get_data():
    if not os.path.exists(storage_path):
        return {}
    with open(storage_path, "r") as f:
        str_data = f.read()
        if str_data:
            return json.loads(str_data)
    return {}


# Функция записи данных в файл
def put(key, value):
    data = get_data()

    if key in data:
        data[key].append(value)
    else:
        data[key] = [value]
    with open(storage_path, "w") as f:
        f.write(json.dumps(data))


# Функция получения значения по ключу
def get(key):
    data = get_data()
    return data[key]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--key")
    parser.add_argument("--value")
    namespace = parser.parse_args()

    if namespace.key and namespace.value:
        put(namespace.key, namespace.value)
    elif namespace.key:
        print(", ".join(get(namespace.key)))
