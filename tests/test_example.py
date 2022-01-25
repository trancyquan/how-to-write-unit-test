import pytest
from datetime import datetime

from src.employee import Employee
from src.example import get_time_of_day, use_env_var, sleep_awhile, Engine, process_data

def test_sleep_awhile(mocker):
    m = mocker.patch("src.example.time.sleep", return_value=None)
    sleep_awhile(3)
    m.assert_called_once_with(3)

@pytest.mark.parametrize(
    "datetime_obj, expect",
    [
        (datetime(2016, 5, 20, 0, 0, 0), "Night"),
        (datetime(2016, 5, 20, 1, 10, 0), "Night"),
        (datetime(2016, 5, 20, 6, 10, 0), "Morning"),
        (datetime(2016, 5, 20, 12, 0, 0), "Afternoon"),
        (datetime(2016, 5, 20, 14, 10, 0), "Afternoon"),
        (datetime(2016, 5, 20, 18, 0, 0), "Evening"),
        (datetime(2016, 5, 20, 19, 10, 0), "Evening"),
    ],
)
def test_get_time_of_day(datetime_obj, expect, mocker):
    mock_now = mocker.patch("src.example.datetime")
    mock_now.now.return_value = datetime_obj

    assert get_time_of_day() == expect

def test_process_data(mocker):
    mocker.patch("src.example.load_data", return_value={"key1": "valy", "key2": "val2"})
    assert process_data() == "valy"

def test_engine_load_data(mocker):
    mocker.patch("src.example.DBConnector.__init__",return_value = None)
    mocker.patch("src.example.DBConnector.get",return_value = 'xyz')
    output = Engine().load_data()
    assert output == 'xyzxxx'

emp_1 = Employee("Corey", "Schafer", 50000)

def test_mock_api_call(mocker):
    mock_requests = mocker.patch("requests.get")
    mock_requests.return_value.ok = True
    mock_requests.return_value.text = "Success"

    schedule = emp_1.monthly_schedule("May")
    mock_requests.assert_called_with("http://company.com/Schafer/May")
    assert schedule == "Success"

@pytest.mark.parametrize(
    	"mock_contract_class,expect", [("en_cloud", "this is en_cloud"), ("en_onprem", "this is en_onprem")]
	)
def test_mock_env_var(mock_contract_class, expect, monkeypatch):
    # more about monkeypatch
    # https://docs.pytest.org/en/6.2.x/monkeypatch.html
    monkeypatch.setenv("CONTRACT_CLASS", mock_contract_class)
    assert use_env_var() == expect


def test_exception(monkeypatch):
    monkeypatch.setenv("CONTRACT_CLASS", "something not existed")
    with pytest.raises(ValueError, match=r"contract class something not existed not found"):
        use_env_var()


# def test_mock_constant(mocker):
#     # Tips: value is mocked where it is used, and not where it's defined (source)
#     mocker.patch("src.employee.PAY_RAISE_RATE", 2)

#     emp_1.apply_raise()
#     assert emp_1.pay == 100000
