from oop.employee import Employee


class Office:
    employeesNum = 0

    def __init__(self, name: str):
        self.name = str(name).strip()
        self.employees = []

    def get_all_employees(self):
        return self.employees

    def get_employee(self, empId: int):
        empId = int(empId)
        for e in self.employees:
            if e.id == empId:
                return e
        return None

    def hire(self, employee: Employee):
        if self.get_employee(employee.id) is not None:
            raise ValueError("Employee id already exists")
        self.employees.append(employee)
        Office.employeesNum += 1

    def fire(self, empId: int):
        emp = self.get_employee(empId)
        if emp:
            self.employees.remove(emp)
            Office.employeesNum -= 1

    def deduct(self, empId: int, deduction: float):
        emp = self.get_employee(empId)
        if emp:
            emp.salary = max(0, emp.salary - float(deduction))

    def reward(self, empId: int, reward: float):
        emp = self.get_employee(empId)
        if emp:
            emp.salary += float(reward)

    def check_lateness(self, empId: int, moveHour: float, velocity: float, targetHour: float = 9.0):
        emp = self.get_employee(empId)
        if not emp:
            raise ValueError("Employee not found")

        late = Office.calculate_lateness(targetHour, moveHour, emp.distanceToWork, velocity)
        if late:
            self.deduct(empId, 10)
            return True
        else:
            self.reward(empId, 10)
            return False

    @staticmethod
    def calculate_lateness(targetHour: float, moveHour: float, distance: float, velocity: float):
        if float(velocity) <= 0:
            return True
        time_hours = float(distance) / float(velocity)
        arrival = float(moveHour) + time_hours
        return arrival > float(targetHour)

    @classmethod
    def change_emps_num(cls, num: int):
        cls.employeesNum = int(num)
