# Задание по программированию: Создание декоратора класса


class Hero:
    def __init__(self):
        self.positive_effects = []
        self.negative_effects = []
        self.stats = {
            "HP": 128,  # health points
            "MP": 42,  # magic points,
            "SP": 100,  # skill points
            "Strength": 15,  # сила
            "Perception": 4,  # восприятие
            "Endurance": 8,  # выносливость
            "Charisma": 2,  # харизма
            "Intelligence": 3,  # интеллект
            "Agility": 8,  # ловкость
            "Luck": 1,  # удача
        }

    def get_positive_effects(self):
        return self.positive_effects.copy()

    def get_negative_effects(self):
        return self.negative_effects.copy()

    def get_stats(self):
        return self.stats.copy()


class AbstractEffect(Hero):
    def __init__(self, base):
        self.base = base
        self.changing_stats = {}
        self.effect_name = ""

    def get_positive_effects(self):
        return self.base.get_positive_effects()

    def get_negative_effects(self):
        return self.base.get_negative_effects()

    def get_stats(self):
        return self.base.get_stats()


class AbstractPositive(AbstractEffect):
    def get_positive_effects(self):
        return self.base.get_positive_effects() + [self.effect_name]

    def get_stats(self):
        stats = self.base.get_stats()
        for key in self.changing_stats:
            stats[key] += self.changing_stats[key]
        return stats


class AbstractNegative(AbstractEffect):
    def get_negative_effects(self):
        return self.base.get_negative_effects() + [self.effect_name]

    def get_stats(self):
        stats = self.base.get_stats()
        for key in self.changing_stats:
            stats[key] -= self.changing_stats[key]
        return stats


class Berserk(AbstractPositive):
    def __init__(self, base):
        self.base = base
        self.changing_stats = {
            "HP": 50,  # health points
            "Strength": 7,  # сила
            "Perception": -3,  # восприятие
            "Endurance": 7,  # выносливость
            "Charisma": -3,  # харизма
            "Intelligence": -3,  # интеллект
            "Agility": 7,  # ловкость
            "Luck": 7,  # удача
        }
        self.effect_name = "Berserk"


class Blessing(AbstractPositive):
    def __init__(self, base):
        self.base = base
        self.changing_stats = {
            "Strength": 2,  # сила
            "Perception": 2,  # восприятие
            "Endurance": 2,  # выносливость
            "Charisma": 2,  # харизма
            "Intelligence": 2,  # интеллект
            "Agility": 2,  # ловкость
            "Luck": 2,  # удача
        }
        self.effect_name = "Blessing"


class Weakness(AbstractNegative):
    def __init__(self, base):
        self.base = base
        self.changing_stats = {
            "Strength": 4,  # сила
            "Endurance": 4,  # выносливость
            "Agility": 4,  # ловкость
        }
        self.effect_name = "Weakness"


class EvilEye(AbstractNegative):
    def __init__(self, base):
        self.base = base
        self.changing_stats = {
            "Luck": 10,  # удача
        }
        self.effect_name = "EvilEye"


class Curse(AbstractNegative):
    def __init__(self, base):
        self.base = base
        self.changing_stats = {
            "Strength": 2,  # сила
            "Perception": 2,  # восприятие
            "Endurance": 2,  # выносливость
            "Charisma": 2,  # харизма
            "Intelligence": 2,  # интеллект
            "Agility": 2,  # ловкость
            "Luck": 2,  # удача
        }
        self.effect_name = "Curse"


hero = Hero()
print(hero.get_stats())
brs1 = Berserk(hero)
print(brs1.get_stats())
print(brs1.get_positive_effects())
brs2 = Berserk(brs1)
cur1 = Curse(brs2)
print(cur1.get_stats())
print(cur1.get_positive_effects())
print(cur1.get_negative_effects())
cur1.base = brs1
print(cur1.get_stats())
print(cur1.get_positive_effects())
print(cur1.get_negative_effects())
