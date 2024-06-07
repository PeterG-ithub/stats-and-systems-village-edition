from src.entities.animal import Animal


class Prey(Animal):
    def __init__(self, id, species) -> None:
        super().__init__(id, species)
        self.flee_rate = 1  # Chances of fleeing when detected. Ex: 100% of escaping
        self.detection_rate = 0  # Chances of getting detected. Ex: 0% of getting detected
        self.detected = False 

    def check_detection(self) -> bool:
        if self.roll() < self.detection_rate:
            # Prey is detected
            self.detected = True
            return True
        else:
            self.detected = False
            return False
    
    def check_flee(self) -> bool:
        if self.roll() < self.flee_rate:
            self.escape()
            return True
        return False

    def escape(self):
        print(f"Rabbit#{self.id} escaped.")
        self.detected = False

    def is_dead_today(self) -> bool:
        #  return super().is_dead_today()
        if self.check_detection():
            if self.check_flee():
                self.die()
                return True
        return False

    def update_flee_rate(self):
        if self.age < 30:  # 1 month
            self.flee_rate = 1 - (1 - 0.95)**(1 / 30)  # (1 - D)^30 = 1 - M where D is daily mortality rate and M is monthly mortality rate 
        elif self.age < 90:  # 3 months
            self.flee_Rate = 1 - (1 - 0.5)**(1 / 60)
        else:
            self.flee_Rate = 1 - (1 - 0.1)**(1 / 90)

    def update_detection_rate(self):
        if self.age < 30:  # 1 month
            self.detection_rate = 1 - (1 - 0.9)**(1 / 10)  # (1 - D)^30 = 1 - M where D is daily mortality rate and M is monthly mortality rate 
        elif self.age < 90:  # 3 months
            self.detection_rate = 1 - (1 - 0.5)**(1 / 10)
        else:
            self.detection_rate = 1 - (1 - 0.3)**(1 / 10)