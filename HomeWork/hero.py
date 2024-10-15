class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase
        self.damage = damage
        self.fly = False

    def nameprint(self):
        print('Имя героя:', self.name)

    def умножить_здоровье_на_2(self):
        self.health_points **= 2
        self.fly = True

    def true_phrase(self):
        print("True in the True_phrase")

    def __len__(self):
        return len(self.catchphrase)

class AirHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, air_speed):
        super().__init__(name, nickname, superpower, health_points, catchphrase, damage)
        self.air_speed = air_speed

class EarthHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, ground_strength):
        super().__init__(name, nickname, superpower, health_points, catchphrase, damage)
        self.ground_strength = ground_strength  # Специфическое свойство для земного героя

air_hero = AirHero('Clark Kent', 'Superman', 'flight', 200, 'Up, up and away!', 70, air_speed=900)
earth_hero = EarthHero('Bruce Wayne', 'Batman', 'super strength', 150, 'I am vengeance!', 50, ground_strength=100)

air_hero.умножить_здоровье_на_2()
earth_hero.умножить_здоровье_на_2()
air_hero.true_phrase()
earth_hero.true_phrase()

print(f"{air_hero.nickname} health points after transformation: {air_hero.health_points}, can fly: {air_hero.fly}")
print(f"{earth_hero.nickname} health points after transformation: {earth_hero.health_points}, can fly: {earth_hero.fly}")

class Villain(EarthHero):
    people = 'monster'

    def gen_x(self):
        pass

    def crit(self, target):
        target.damage **= 2

villain = Villain('Lex Luthor', 'Luthor', 'genius intellect', 100, 'Knowledge is power.', 60, ground_strength=80)

print(f"{villain.nickname} initial damage: {villain.damage}")
villain.crit(earth_hero)
print(f"{villain.nickname} damage after crit: {villain.damage}")
print(f"{earth_hero.nickname} damage after crit applied by villain: {earth_hero.damage}")