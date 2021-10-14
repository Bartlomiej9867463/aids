# dynamiczne typwoani
#typowanie stale
# METODA MAGICZNA czyli init len, bo niezależnie od jej zadeklarowania czy nie i tak będą obecne
a: str = 23
print(type(a))

class House:
    doors: int
    color: str
    def __init__(self, doors: int, color: str) -> None:
        self.doors = doors
        self.color = color
    def change_color(self, new_color: str) -> None:
        if new_color == self.color:
            print("Kolor nie moze byc ten sam")
            return
        self.color = new_color
    def __len__(self) -> int:
        return 100
    def __str__ (self) -> str:
        # zinterpolowanie
        return f'liczba drzwo: {self.doors}' f'kolor elewacji: {self.color}'
house1: House = House(doors=1, color="blue")
print(house1.doors)
print(house1.color)
print(len(house1))
# print(str(house1))
print(house1)
