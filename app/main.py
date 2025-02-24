class Animal:
    alive = []

    def __init__(
            self, name: str, health: int = 100, hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        Animal.alive = []
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden

    def bited(self, bite_power: int) -> None:
        self.health -= bite_power
        if self.health <= 0:
            self.health = 0
            Animal.alive.remove(self)


class Carnivore(Animal):
    def bite(self, beast: Herbivore) -> None:
        if isinstance(beast, Herbivore) and not beast.hidden:
            beast.bited(50)


pantera = Carnivore("Bagira")
snake = Carnivore("Kaa")
print(Animal.alive)
print(len(Animal.alive))
foo = Herbivore("foo")
print(len(Animal.alive))

snake.bite(foo)
pantera.bite(foo)
print(Animal.alive)
print(len(Animal.alive))
