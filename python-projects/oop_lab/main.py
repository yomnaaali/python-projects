from oop.car import Car
from oop.employee import Employee
from oop.office import Office


def main():
    print("===== OOP LAB RUN =====")

    fiat = Car("Fiat128", fuelRate=80, velocity=0)
    samy = Employee(
        name="Samy",
        money=500,
        emp_id=1,
        email="samy@iti.gov.eg",
        salary=3000,
        distanceToWork=20,
        car=fiat
    )

    iti = Office("ITI Smart Village")
    iti.hire(samy)

    samy.sleep(7)
    samy.eat(3)
    samy.buy(2)
    print("Samy:", samy.mood, samy.healthRate, samy.money)

    samy.work(8)
    print("Mood after work:", samy.mood)

    print("Fuel before drive:", samy.car.fuelRate)
    samy.drive(distance=samy.distanceToWork, velocity=60)
    print("Fuel after drive:", samy.car.fuelRate)

    samy.refuel(30)
    print("Fuel after refuel:", samy.car.fuelRate)

    late = iti.check_lateness(empId=1, moveHour=8.5, velocity=60, targetHour=9.0)
    print("Late?", late)
    print("Salary:", samy.salary)

    samy.send_mail("hr@iti.gov.eg", "Attendance", "I arrived on time today.")
    print("EmployeesNum:", Office.employeesNum)

    print("===== END =====")


if __name__ == "__main__":
    main()
