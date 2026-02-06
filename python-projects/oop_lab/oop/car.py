import math
from oop.person import ValidationError


class Car:
    def __init__(self, name: str, fuelRate: float = 100, velocity: float = 0):
        name = str(name).strip() if name is not None else ""
        if not name:
            raise ValidationError("Car name cannot be empty")

        self.name = name
        self.fuelRate = fuelRate
        self.velocity = velocity

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, v):
        v = float(v)
        if not (0 <= v <= 200):
            raise ValidationError("velocity must be between 0 and 200")
        self._velocity = v

    @property
    def fuelRate(self):
        return self._fuelRate

    @fuelRate.setter
    def fuelRate(self, f):
        f = float(f)
        if not (0 <= f <= 100):
            raise ValidationError("fuelRate must be between 0 and 100")
        self._fuelRate = f

    def run(self, velocity: float, distance: float):
        distance = float(distance)
        if distance < 0:
            raise ValidationError("distance must be >= 0")

        self.velocity = float(velocity)

        # 10 fuel points per 10 km (discrete steps)
        required = math.ceil(distance / 10) * 10

        if self.fuelRate >= required:
            self.fuelRate -= required
            self.stop(0)
        else:
            possible_distance = (self.fuelRate / 10) * 10
            remaining = distance - possible_distance
            self.fuelRate = 0
            self.stop(remaining)

    def stop(self, remainingDistance: float):
        self.velocity = 0
        if remainingDistance <= 0:
            print("Car: Arrived ✅")
        else:
            print(f"Car: Stopped early ⛽ Remaining = {remainingDistance:.2f} km")
