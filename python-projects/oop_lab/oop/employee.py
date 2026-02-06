from oop.person import Person, ValidationError, clamp
from oop.car import Car


class Employee(Person):
    def __init__(self, name, money, emp_id, email, salary, distanceToWork, car: Car):
        super().__init__(name, money)
        self.id = int(emp_id)
        self.email = str(email).strip()
        self.salary = float(salary)
        self.distanceToWork = float(distanceToWork)

        if not isinstance(car, Car):
            raise ValidationError("car must be an instance of Car")
        self.car = car

    def work(self, hours: int):
        hours = int(hours)
        if hours == 8:
            self.mood = "happy"
        elif hours > 8:
            self.mood = "tired"
        else:
            self.mood = "lazy"

    def drive(self, distance: float, velocity: float):
        self.car.run(velocity=velocity, distance=distance)

    def refuel(self, gasAmount: float = 100):
        gasAmount = float(gasAmount)
        if gasAmount < 0:
            raise ValidationError("gasAmount must be >= 0")
        self.car.fuelRate = clamp(self.car.fuelRate + gasAmount, 0, 100)

    def send_mail(self, to: str, subject: str, body: str):
        print(f"\n[MAIL]\nTo: {to}\nSubject: {subject}\n{body}\n")
