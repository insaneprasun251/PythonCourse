from dataclasses import dataclass, field


@dataclass(order=True)
class Country:
    name: str
    population: int
    # repr False causes not showing in the str function, when you print contents of the whole object
    area: float = field(repr=False, compare=False)
    coastline: float = 0

    def beach_person(self):
        """
        Meters of coastline per person
        :return: Returns meters of coastline per person
        """

        return (self.coastline * 1000) / self.population


norway = Country("Norway", 5320045, 323802, 58133)

print(norway)
print(norway.name)
print(norway.area)
print(norway.beach_person())

