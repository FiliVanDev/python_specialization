# Задание по программированию: Классы и наследование
import os
import csv


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "car"
        self.passenger_seats_count = passenger_seats_count


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        try:
            self.body_width, self.body_height, self.body_length = [
                float(whl) for whl in body_whl.split("x")
            ]
        except:
            self.body_width, self.body_height, self.body_length = [0, 0, 0]
        self.car_type = "truck"

    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra
        self.car_type = "spec_machine"


def get_cat_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=";")
        next(reader)  # пропускаем заголовок
        for row in reader:
            try:
                if os.path.splitext(row[3])[1] in [".jpg", ".jpeg", ".png", "gif"]:
                    if row[0] == "car":
                        if row[1] and row[2] and row[3] and row[5]:
                            car_list.append(Car(row[1], row[3], row[5], row[2]))
                    elif row[0] == "truck":
                        if row[1] and row[3] and row[5]:
                            car_list.append(Truck(row[1], row[3], row[5], row[4]))
                    elif row[0] == "spec_machine":
                        if row[1] and row[3] and row[5] and row[6]:
                            car_list.append(SpecMachine(row[1], row[3], row[5], row[6]))
            except:
                pass
    return car_list