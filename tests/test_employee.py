import pytest
from src.employee import Employee
    
@pytest.fixture
def employee_obj():
    """
    Test Employee Fixture
    """
    obj = Employee(first='Corey', last='Schafer', pay=50000)
    return obj

def test_employee_init(employee_obj):
    employee_obj.first = 'Corey'
    employee_obj.last = 'Schafer'
    employee_obj.pay = 50000

def test_email(employee_obj):
    assert employee_obj.email == 'Corey.Schafer@email.com'

def test_fullname(employee_obj):
    assert employee_obj.fullname == 'Corey Schafer'
   

def test_apply_raise(employee_obj):
    employee_obj.apply_raise()
    assert employee_obj.pay == 52500

def test_monthly_schedule(employee_obj, mocker):
    mock_requests = mocker.patch('requests.get')
    mock_requests.return_value.ok = True
    mock_requests.return_value.text = 'Success'
   

    schedule = employee_obj.monthly_schedule('May')
    mock_requests.assert_called_with('http://company.com/Schafer/May')
    assert schedule == 'Success'

        # mocked_get.return_value.ok = False

        # schedule = emp_2.monthly_schedule('June')
        # mocked_get.assert_called_with('http://company.com/Smith/June')
        # assert schedule == 'Bad Response!'
