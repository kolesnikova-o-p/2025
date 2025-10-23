class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __str__(self):
        return f"{self.name} ({self.species})"


class Owner:
    def __init__(self, name):
        self.name = name
        self.pets = []

    def add_pet(self, pet):
        self.pets.append(pet)

    def __str__(self):
        pets_list = ", ".join(str(pet) for pet in self.pets)
        return f"{self.name} питомцы: {pets_list}"


if __name__ == "__main__":
    owner = Owner("Наташа")
    cat = Pet("Мурка", "Кошка")
    dog = Pet("Бобик", "Собака")
    owner.add_pet(cat)
    owner.add_pet(dog)
    print(owner)