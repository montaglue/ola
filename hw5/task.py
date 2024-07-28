import random

class AnimalKind:
    kind: str
    size: int
    food: list[str]
    habitat: str
    lifespan: int

    def __init__(self, kind: str, size: int, food: list[str], habitat: str, lifespan: int) -> None:
        self.kind = kind
        self.size = size
        self.food = food
        self.habitat = habitat
        self.lifespan = lifespan
    
    def reproduce(self, male, female):
        if self.habitat == 'earth':
            pass
        elif self.habitat == 'air':
            pass
        else:
            pass
        

class Animal:
    kind: AnimalKind
    id: int
    age: int
    sex: str
    satiation: int

    def __init__(self, id: int, kind: AnimalKind, sex: str) -> None:
        self.id = id
        self.kind = kind
        self.sex = sex
        self.age = 0
        self.satiation = 100

    def die(self, planet) -> None:
        if self.kind.habitat == 'earth':
            planet.earth.remove(self)
        elif self.kind.habitat == 'air':
            planet.air.remove(self)
        else:
            planet.water.remove(self)
        planet.add_plant_food(self.kind.size)

    def time_step(self, planet) -> None:
        self.age += 1
        if self.age >= self.kind.lifespan:
            self.die(planet)
            return

        if len(self.kind.food) == 0:
            if planet.plant_food > 0:
                self.satiation += 26
                planet.add_plant_food(-1)
        
        if random.randint(0, 1) == 0:
            # create random shuffle
            # go 1 by 1 and eat random from first not empty
            pass
        else:
            self.satiation -= 16
        self.satiation -= 9

        if self.satiation < 10:
            self.die(planet)
            return

def generate_name() -> str:
    syllables = ['ha', 'la', 'ma', 'na', 'pa', 'ra', 'sa', 'ta', 'va', 'za', 'he', 'le', 'me', 'ne', 'pe', 're', 'se', 'te', 've', 'ze']
    name = ''
    for i in range(3):
        name += syllables[random.randint(0, len(syllables) - 1)]
    return name


def generate_kinds(n: int) -> Animal:
    names = {}
    while len(names) < n:
        name = generate_name()
        names.insert(name)
    
    habitats = ['earth', 'air', 'water']
    kinds = []
    for name in names:
        size = random.randint(1, 10)
        habitat = habitats[random.randint(0, 2)]
        lifespan = random.randint(1, 10)

        if random.randint(0, 1) == 0:
            kinds.append(AnimalKind(name, size, [], habitat, lifespan))
        else:
            food = []
            for i in range(random.randint(1, 5)):
                food.insert(names[random.randint(0, len(names) - 1)])
            kinds.append(AnimalKind(name, size, list(food), habitat, lifespan))

    return kinds

class Planet:
    animal_kinds: list[AnimalKind]
    earth: list[Animal]
    air: list[Animal]
    water: list[Animal]
    counter: int
    plant_food: int
    
    def __init__(self) -> None:
        self.animal_kinds = generate_kinds(10)
        self.earth = []
        self.air = []
        self.water = []
        self.counter = 0
        self.plant_food = 10

    def show_kinds(self) -> None:
        print('Animal kinds:')
        print('Name | Size | Food | Habitat | Lifespan')
        for i, kind in enumerate(self.animal_kinds):
            print(f'{kind.kind} | {kind.size} | {kind.food} | {kind.habitat} | {kind.lifespan}')


    def add_animal(self, kind: str, sex: str) -> None:
        animal_kind = [k for k in self.animal_kinds if k.kind == kind][0]
        self.counter += 1
        id = self.counter
        animal = Animal(id, animal_kind, sex)
        if animal_kind.habitat == 'earth':
            self.earth.append(animal)
        elif animal_kind.habitat == 'air':
            self.air.append(animal)
        else:
            self.water.append(animal)

    def add_plant_food(self, amount: int) -> None:
        self.plant_food += amount   

    def show_animals(self) -> None:
        print('Animals:')
        print('ID | Kind | Age | Sex | Satiation')
        
        print('Earth:')
        for animal in self.earth:
            print(f'{animal.id} | {animal.kind.kind} | {animal.age} | {animal.sex} | {animal.satiation}')
        
        print('Air:')
        for animal in self.air:
            print(f'{animal.id} | {animal.kind.kind} | {animal.age} | {animal.sex} | {animal.satiation}')

        print('Water:')
        for animal in self.water:
            print(f'{animal.id} | {animal.kind.kind} | {animal.age} | {animal.sex} | {animal.satiation}')

    def reproduction(self, parent1: int, parent2: int) -> None:
        animals = self.earth + self.air + self.water
        parent1 = [a for a in animals if a.id == parent1][0]
        parent2 = [a for a in animals if a.id == parent2][0]
        if parent1.kind.kind != parent2.kind.kind:
            return
        if parent1.sex == parent2.sex:
            return
        kind = parent1.kind
        if kind.habitat == 'earth':
            self.earth.extend(kind.reproduce(parent1, parent2))
        elif kind.habitat == 'air':
            self.air.extend(kind.reproduce(parent1, parent2))
        else:
            self.water.extend(kind.reproduce(parent1, parent2))
            
    def time_step(self) -> None:
        for animal in self.earth:
            animal.time_step(self)
        for animal in self.air:
            animal.time_step(self)
        for animal in self.water:
            animal.time_step(self)




def main():
    planet = Planet()
    exit_loop = False

    while not exit_loop:
        pass


if __name__ == '__main__':
    main()