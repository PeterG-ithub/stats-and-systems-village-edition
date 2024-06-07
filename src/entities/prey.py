from src.entities.animal import Animal


class Prey(Animal):
    def __init__(self, id, species) -> None:
        super().__init__(id, species)

    def evade_predator(self):
        # Do something with chances of getting spotted
        pass

    def flee(self):
        # Do something here base on the chances of fleeing 
        # when getting hunted
        pass

    def update_mortality(self):
        # Mortality based on a rabbit age cycle
        if self.age < 30:  # 1 month
            self.mortality_rate = 80
        elif self.age < 90:  # 3 months
            self.mortality_rate = 50
        else:
            self.mortality_rate = 10
