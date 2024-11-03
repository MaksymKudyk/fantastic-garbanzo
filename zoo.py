import random

class Keeper:
    def __init__(self, name):
        self.name = name

    def clean_enclosure(self, enclosure):
        if enclosure.is_clean:
            print(f"{self.name}:{enclosure.name} вже чистий.")
        else:
            enclosure.is_clean = True
            print(f"{self.name} прибрав {enclosure.name}.")

    def feed_animal(self, animal):
        if animal.is_hungry:
            animal.is_hungry = False
            print(f"{self.name} нагодував {animal.species} {animal.name}.")
        else:
            print(f"{animal.species} {animal.name} не голодний.")

class Enclosure:
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.is_clean = random.choice([True, False])
        self.is_open = False

    def add_animal(self, animal):
        self.animals.append(animal)

    def open(self):
        self.is_open = True
        print(f"{self.name} відкрито для відвідувачів.")

    def close(self):
        self.is_open = False
        print(f"{self.name} закрито для відвідувачів.")

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.is_hungry = random.choice([True, False])
        self.is_happy = False

    def update_happiness(self, enclosure):
        self.is_happy = not self.is_hungry and enclosure.is_clean
        state = "щасливий" if self.is_happy else "нещасливий"
        print(f"{self.species} {self.name} зараз {state}.")

class Lion(Animal):
    def __init__(self, name):
        super().__init__(name, "Лев")

class Monkey(Animal):
    def __init__(self, name):
        super().__init__(name, "Мавпа")

class Elephant(Animal):
    def __init__(self, name):
        super().__init__(name, "Слон")

def zoo_day():
    keeper = Keeper("Олексій")

    lion_enclosure = Enclosure("Лев'ячий вольєр")
    monkey_enclosure = Enclosure("Мавп'ячий вольєр")
    elephant_enclosure = Enclosure("Слонячий вольєр")

    simba = Lion("Сімба")
    bobo = Monkey("Бобо")
    dumbo = Elephant("Дамбо")

    lion_enclosure.add_animal(simba)
    monkey_enclosure.add_animal(bobo)
    elephant_enclosure.add_animal(dumbo)

    print("\nРанок у зоопарку:")
    for enclosure in [lion_enclosure, monkey_enclosure, elephant_enclosure]:
        keeper.clean_enclosure(enclosure)

    print("\nЧас годування:")
    for animal in [simba, bobo, dumbo]:
        keeper.feed_animal(animal)

    print("\nСтан тварин:")
    for enclosure in [lion_enclosure, monkey_enclosure, elephant_enclosure]:
        for animal in enclosure.animals:
            animal.update_happiness(enclosure)

    print("\nВідкриття вольєрів:")
    for enclosure in [lion_enclosure, monkey_enclosure, elephant_enclosure]:
        enclosure.open()

zoo_day()