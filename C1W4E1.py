import os
import tempfile
import random


class File:
    def __init__(self, path):
        self.path = path
        if not os.path.exists(self.path):
            open(self.path, "w").close()

    def __add__(self, obj):
        try:
            temp_path = os.path.join(
                tempfile.gettempdir(), f"tempfile{random.randint(1, 1000)}.txt"
            )
            with open(temp_path, "w") as f:
                f.write(self.read() + obj.read())
            return File(temp_path)
        except:
            print("Somthing wrong")

    def __str__(self):
        return self.path

    def __iter__(self):
        self.text = open(self.path)
        return self

    def __next__(self):
        return next(self.text)

    def read(self):
        with open(self.path, "r") as f:
            return f.read()

    def write(self, data):
        with open(self.path, "w") as f:
            f.write(data)
