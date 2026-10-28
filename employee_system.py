from abc import ABC, abstractmethod

class BonusRule(ABC):
    @abstractmethod
    def calculate(self, base_salary): pass

class Perf2026Rule(BonusRule):
    def calculate(self, base_salary): return base_salary * 0.20

class Senior10Rule(BonusRule):
    def calculate(self, base_salary): return base_salary * 0.10

class Lead2026Rule(BonusRule):
    def calculate(self, base_salary): return base_salary * 0.25

class NoBonusRule(BonusRule):
    def calculate(self, base_salary): return 0

class Employee(ABC):
    def __init__(self, emp_id, name, base_salary, bonus_code):
        self.emp_id = emp_id
        self.name = name
        self.base_salary = base_salary
        self.bonus_code = bonus_code

    @abstractmethod
    def calculate_total_salary(self): pass

    def get_bonus_rule(self):
        rules = {"PERF2026": Perf2026Rule(), "SENIOR10": Senior10Rule(), "LEAD2026": Lead2026Rule()}
        return rules.get(self.bonus_code, NoBonusRule())

class PermanentEmployee(Employee):
    def calculate_total_salary(self):
        return self.base_salary + self.get_bonus_rule().calculate(self.base_salary) + 1000000
    def get_details(self):
        return f"[TETAP] {self.emp_id} - {self.name} | Total: Rp {self.calculate_total_salary():,.0f}"

class ContractEmployee(Employee):
    def calculate_total_salary(self):
        return self.base_salary + self.get_bonus_rule().calculate(self.base_salary)
    def get_details(self):
        return f"[KONTRAK] {self.emp_id} - {self.name} | Total: Rp {self.calculate_total_salary():,.0f}"

def employee_factory(data):
    if data['is_permanent']:
        return PermanentEmployee(data['emp_id'], data['name'], data['base_salary'], data['bonus_code'])
    else:
        return ContractEmployee(data['emp_id'], data['name'], data['base_salary'], data['bonus_code'])