class ValidationError(ValueError):
    pass


def clamp(x, lo, hi):
    return max(lo, min(hi, x))


class Person:
    def __init__(self, name: str, money: float, mood: str = "neutral", healthRate: int = 100):
        name = str(name).strip() if name is not None else ""
        if not name:
            raise ValidationError("Name cannot be empty")

        self.name = name
        self.money = max(0.0, float(money))
        self.mood = str(mood)
        self.healthRate = clamp(int(healthRate), 0, 100)

    def sleep(self, hours: int):
        hours = int(hours)
        if hours == 7:
            self.mood = "happy"
        elif hours < 7:
            self.mood = "tired"
        else:
            self.mood = "lazy"

    def eat(self, meals: int):
        meals = int(meals)
        mapping = {1: 50, 2: 75, 3: 100}
        if meals not in mapping:
            raise ValidationError("meals must be 1, 2, or 3")
        self.healthRate = mapping[meals]

    def buy(self, items: int):
        items = int(items)
        if items < 0:
            raise ValidationError("items must be >= 0")
        self.money = max(0.0, self.money - items * 10)
