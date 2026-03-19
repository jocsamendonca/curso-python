from employees import Employee
import pytest

@pytest.fixture
def employee():
    """Cria um empregado que estará disponível para todas as funções de teste"""
    employee_1 = Employee('Jorge', 'Mendonça')
    return employee_1

def test_give_default_rise(employee):
    employee.give_rise()
    assert employee.annual_salary == 5000
    
def test_give_custom_rise(employee):
    employee.give_rise(120000)
    assert employee.annual_salary == 120000
