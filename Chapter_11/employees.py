# 11.3 Funcionário

class Employee:
    """Cria uma classe de empregados"""
    def __init__(self, first_name, last_name, annual_salary=''):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_rise(self, rise=5000):
        self.annual_salary = rise
        