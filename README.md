# Effective Unit Testing with Pytest

In this tutorial, you’ll learn:
* What is Unit Testing and Test Pyramid?
* Why do we need Unit Testing?
* What makes a good unit test then?
* How to write Unit Test with PyTest (Basics)?
* How to mock dependencies properly in various scenarios?


## Prerequisite
To follow this tutorial, you would need to install `pytest` and `pytest-mock`.
I provided commands for both python library installation options: pip and poetry.


If you are using pip for installation (default):
```
 python -m pip install pytest
 python -m pip install pytest-mock

```
If you are using poetry for installation:
```
 poetry add pytest
 poetry add pytest-mock

```
## What is Unit Testing and Test Pyramid?

Unit Testing is a software testing method to test the smallest piece of code that can be isolated, i.e. a function (method).

The concept of Test Pyramid as shown below, is introduced by Mike Cohn in his book *Succeeding with Agile*. It's a great visual metaphor telling you to think about different layers of testing and also how much testing to do on each layer.

According to the pyramid, when it is at the bottom it normally means more isolated and faster tests (in other words: cheaper); while moving up the pyramid, it means more integrated and slower tests (in other words: expensive). At the tip of the pyramid could means manual testing. 

![test-automation-pyramid.jpeg](testing-pyramid.png)

## Why do we need Unit Testing?

People would tend to rush the requested feature delivering but ignoring the importance of writing test cases. The ignorance could be due to they see it as a waste of time and not seeing the damage it could cause. However, let me tell you the benefits that writing Unit tests will brings you: 


1. Identify bugs easily and early

    Unit test can help you verify what you want to develop.

    Without unit test, you would end up being caught by fixing random bugs when running entire application. And you may need to spend hours on placing breakpoints and tracing where does it come from.

2. Help you write better code

    If you find it's hard to write a test case for your own code, you probably would think about refactoring your code.

3. Test at low cost

    Unit test is the fastest among all test cases as it removes all the dependencies.

4. Serve as documentation

    People will understand what kind of input/output data type,format is when they look at your unit tests.


## What makes a good unit test then?
Below are the six qualities that will make a good unit test.
How we could achieve the first four qualities are covered in the sections below.
- Independent

    The testing is focusing on the function itself and **NOT** on all the dependencies, which include API call, DB connections, other functions from your application or third party libraries. All dependencies should be properly mocked.

    Multiple assertions are okay as long as they are all testing one feature/behavior. When a test fails, it should pinpoint the location of the problem.

    Tests should be isolated -- **not rely on each other** . No assumptions about order of test execution.

- Fast

    A good unit test's response time should be less than a second. 
    This is also a good and straightfoward way to evaluate its independency. Any unit test taking longer than that should be questioned in terms of it's dependency. And maybe that's no longer unit test but integration test.

- Repeatable

    The tests should produce the same output no matter when and how many time it runs.

- Readable (Consistency)
    
    The test case serves part of the function documentation and it's frequently read during debugging processes. Thus, it's important to be understood easily. Try to stick to one naming convention for naming test file, test case, sequence of assertion (`assert output == expect`) and the way of writing mocks.

- Automatic

    The process of running the unit tests should be integrated into CI/CD tool such as Jenkins, so the code quality can be continously ensured with every new change.

	This is not detailly explained in this article. Feel free to read more about Jenkins, GitHub Actions or any CI/CD tools.

- Thorough (Coverage)

    As mentioned in the Test Pyramid, we should get more unit tests as they are cheaper and faster. Coverage is the key metric to evaluate the degree of which source code has been tested. Any uncovered lines could result to a corner case bug one day with more expensive identification and resolving process.

    Here is the formula to calculate code coverage, which is also called line coverage. This is mostly used.

    ```
    Code Coverage = (Number of lines of code executed)/(Total Number of lines of code in a system component) * 100
    ```

    There is no ideal code coverage number that universally applies to all products. I would recommend to first reach 80% and make sure the coverage can be maintained with every single change, then continously work on improving the code coverage towards 90%.  
    Efforts needed from 90% to 100% could be logarithmic, therefore usually taget won't go to as high as 100%.

## How to write Unit Test with PyTest (Basics)?
Here are some basics to help you get started with PyTest.

Below is a typical folder structure for a Python project/application, where you have a `tests` folder that is outside of your `src` folder.

```
.
├── docs                    # Documentation files (alternatively `doc`)
├── src                     # Source files (alternatively `lib` or `app`)
├── tests                    # Automated tests (alternatively `test`)
└── README.md
```

 1. Let's assume we are testing the simple `add` function of `calc.py` file under `src` folder

	```
	# src/calc.py

	def add(x, y):
	    """Add Function"""
	    return x + y
	```
 2. Create a file named `test_calc.py` inside the `tests` folder.

	The test file name should always start or end with `test`. I prefer to keep the structure consistent as `test_xxx.py` where `xxx` where be py file name you are testing.
	You may read more about [documentation on how test discovery works for pytest](https://docs.pytest.org/en/6.2.x/goodpractices.html).

 3. Write the test case `test_add`

	When writing the test cases, just define a function starting with `test` in the name. Similar as the file name, I prefer to keep it consistent as `test_xxx` where `xxx` is the function you are testing. This provides a very clear understanding for others.

	And this follows **Arrange-Act-Assert** pattern to structure the test content.
Though this example is very simple and straightforward and we could replace it with one line assertion, but let's just use it for illustration purpose.
	* **Arrange** the input and targets: Does the test needs some special settings? Does it needs to prepare the database? Most of the time, we need to get the inputs ready and also mockup the dependencies before we proceed with the *Act* step.
	* **Act** on the targets: This usually refers to calling the function or method in the Unit Testing scenario.
	* **Assert** expected outcomes: We will receive certain responses from *Act* step. And *Assert* step verifies the goodness or badness of that response. This could be checking whether numbers/strings are correct, whether particular type of Exception was triggered or certain function was being triggered.
	 Assertions will ultimately determine if the test passes or fails.

	 For assertion statments (referring to `output == expected` part), generally, you could use any of logical conditions you would put similar as you write `if` statment. You could find the [detailed list of python assertion statements](https://understandingdata.com/list-of-python-assert-statements-for-unit-tests/) here and play around with them.

	I didn't always follow strictly **Arrange-Act-Assert** pattern to put each of them into a block. Sometimes I would combine Act and Assert just to save one line. But following this sequence always makes it looks neat and tidy.

	```
	import pytest
	from src.calc import add

	def test_add():
		# Arrange
		a = 2
		b = 5
		expected = 7

		# Act
		output = add(a, b)

		# Assert
		assert output == expected
	```

	**Note**: We should consistently put output at the left handside and expected output at the right handside, meaning `assert output == expected` not `assert expected == output`. This doesn't make a difference in Terminal/CMD. But PyCharm will display it wrongly if we did it reversely.

 4. How to run PyTest

	You could run PyTest test cases with any of the below commands.

	```
	# run all tests
	python -m pytest tests

	# run single test file
	python -m pytest tests/test_calc.py

	# run single test case
	python -m pytest tests/test_calc.py::test_add
	```
	**Note**: If you are using poetry environment, you need to add `poetry run` before any of the testing command.

5. Try to think more situations where the function should be tested, so that you cover every aspect of it.

### Parametrizing
Here, let me introduce the pytest **parametrizing** decorator, which checks whether multiple inputs lead to expected output. It's a little bit similar as looping through each of the 3 input set (a+b), however, the testing result will let you know whether each of them has passed.
But writing a loop of asserting each of them would stop at the middle once it failed.

This example tests when a=10, b=5, whether expected is 15; and similar for the other two cases.

```
import pytest
from src.calc import add


@pytest.mark.parametrize("a,b,expected",
							[(10, 5, 15),
							(-1, 1, 0),
							(-1, -1, -2)])
def test_add(a, b, expected):
	assert add(a, b) == expected
```
And here, we try to cover different scenarios of adding two positives, two negatives or one positive and one negative numbers. You may also add floating points test cases (which usually should be considered for testing division).

We have covered how to write a test case with pytest and parametrizing.
Let's look at another concept in PyTest, which is **fixture**.

### Fixture

Fixture is a function with decorator that creates a resource and returns it.
If you need the same test input for multiple test cases, you can use *fixture* to prepare the *arrange* step, just as the example below. 

This reduces code duplications.
```
@pytest.fixture
def employee_obj_helper():
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

```


## How to mock dependencies properly in various scenarios

We have learnt what makes a good Unit Test in the previous sections.
And mocking is exactly the technique can help us writing independent, fast, repeatable test cases.

The purpose of mocking is to isolate and focus on the code being tested and not on the behavior or state of external dependencies. In mocking, the dependencies are replaced by closely controlled replacements objects that simulate the behavior of the real ones.


Let's start with a simple mocking example.
### Example 1:
We have a function sleep for couple of seconds. Let's assume we have some other processing steps after the sleep.
```
def sleep_awhile(duration):
    """sleep for couple of seconds"""
    time.sleep(duration)
    # some other processing steps    
```
And here is the test case.
```
def test_sleep_awhile(mocker):
    m = mocker.patch("src.example.time.sleep", return_value=None)
    sleep_awhile(3)
    m.assert_called_once_with(3)
```
1. We need to use `mocker` as part of test case inputs so we can call `mocker.patch`.
2. We creates a mock object that replaces the `time` module with a fake object that do nothing, by specifying the target as "src.example.time.sleep", meaning the `time.sleep` function inside `src/example.py`.
	Here comes the rule of thumb for mocking:

	> Mock where it is used, and not where it's defined (source)

	 Here, `sleep` function doesn't return anything so we just define `return_value` as `None`.
3. For this function `sleep_awhile` there is no output provided so we can't verify that. So how do we know the test case is written properly?

	Thus, we check whether the mock object has been called with correct input using `assert_called_once_with`.  And the test time should not be as long as 3 seconds.(should be <1s)

	Note, this function `assert_called_once_with` is already an assertion function so we don't use `assert` keyword again in front of it.

	Assertion functions for mock objects can also be `assert_called(), assert_any_call(), assert_not_called()` etc, referring to the [documentation](https://docs.python.org/3/library/unittest.mock.html).

### Example 2:
We have function `get_time_of_day` in `src/example.py` as following to tell us what time of day it is now.
It will return us the string of Night/Morning/Afternoon/Evening, depending on the hour range.

```
# src/example.py

from datetime import datetime

def get_time_of_day():
    """return string Night/Morning/Afternoon/Evening depending on the hours range"""
    time = datetime.now()
    if 0 <= time.hour <6:
        return "Night"
    if 6 <= time.hour < 12:
        return "Morning"
    if 12 <= time.hour <18:
        return "Afternoon"
    return "Evening"

```
How would you test this?

If we just define a test case at 10 am, it will not be valid in the afternoon. The test result would highly depend on when you run the test. And the test case would be not repeatable no matter when you write it.

Therefore, we needs to fix the time whenever the test cases runs.
And let's see how we do this with mocking.

1. Mock the `datetime` object and the returns of `now` function

	We need to include `mocker` as the function input.
	And we use `mocker.patch` where `"src.example.datetime"` refers to the object needs mocking. You may wonderly why it's not purely just `"datetime.datetime"`.



	So "src.example" here refers to the file path, and ".datetime" refers to the library/the part being used within the `get_time_of_day` function.

	And we use `mock_obj.function.return_value` to define what kind of return we want to replace for the function. It could be many layers other than one like `mock_obj.another_obj.function.return_value`.

	Here we fix the value return for `datetime.now()` function to be 2pm, therefore, we are expecting an output of `"Afternoon"`.

	```
	import pytest
	from datetime import datetime
	from src.example import get_time_of_day

	def test_get_time_of_day(mocker):
	    mock_now = mocker.patch("src.example.datetime")
	    mock_now.now.return_value = datetime(2016, 5, 20, 14, 10, 0)

	    assert get_time_of_day() == "Afternoon"
	```

2. Combine the mocking with parametrizing

	We can actually combine the two. Just need to make sure input of the test function here starts with the inputs of parametrizing followed by `mocker` as the `def test_get_time_of_day(datetime_obj, expect, mocker):`.

	And for input `datetime_obj`, I try to cover every scenario of Night/Morning/Afternoon/Evening and particularly for the boundry conditions (0/6/12/18 hour).

	```
	import pytest
	from datetime import datetime
	from src.example import get_time_of_day

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
	```

Now, you have learnt about the ways we use to mock third-party libraries.
Let's look at some other examples with different scenarios.

### More Examples
 - #### Function from another file
	Here, we have a `load_data` function loads the data and returns the data. We use `time.sleep` to mimic the time taken e.g. loading data from database.
	```
	# src/dataset.py
	import time

	def load_data():
	    time.sleep(4)
	    # loading data...
	    return {"key1":"val1", "key2":"val2"}
	```
	Here, we have a `process_data()` function that loads the dataset and process it with certain steps (which were skipped here). Then we returns a processed result, here, assuming it as `data["key1"]`.

	```
	def process_data():
	    data = load_data()
	    # process the data in certain ways ...
	    processed_data = data["key1"]
	    return processed_data
	```
	Remember the rule?
	> Mock where it is used, and not where it's defined (source)

	To test this, we need to mock `"src.example.load_data"`  and not `"src.dataset.load_data"`.

    ```
	def test_process_data(mocker):
	    mocker.patch("src.example.load_data", return_value={"key1": "valy", "key2": "val2"})
	    assert process_data() == "valy"
    ```

- #### Function in a class (even **init funciton)**
	We have a `DBConnector` that initializes the connection to the database in `__init__` and `get` data from db based on the `id`.
	```
	# src/db_connection.py
	import time

	class DBConnector:
	    def __init__(self):
	        # setup some db connection
	        time.sleep(3)
	        pass

	    def get(self, id):
	        time.sleep(5)
	        return 'some data'
	```
	We have an `Engine` that includes the DBConnector as its attribute.
	```
	class Engine:
	    def __init__(self):
	        self.connector = DBConnector()

	    def load_data(self):
	        data = self.connector.get(123)
	        print(data)
	        # do some processing
	        data = data + "xxx"
	        return data
	```
	How can we test `Engine.load_data`?
    When mock `__init__` function, we must put `return_value` with `None`.
	```
	def test_engine_load_data(mocker):
	    mocker.patch("src.example.DBConnector.__init__",return_value = None)
	    mocker.patch("src.example.DBConnector.get",return_value = 'xyz')
	    output = Engine().load_data()
	    assert output == 'xyzxxx'
	```

- #### API
	This is an example of doing a `GET` request through `requests` library.
	```
	#src/employee.py

	class Employee:
	    """A sample Employee class"""


	    def __init__(self, first, last, pay):
	        self.first = first
	        self.last = last
	        self.pay = pay

	    def monthly_schedule(self, month):
	        response = requests.get(f'http://company.com/{self.last}/{month}')
	        if response.ok:
	            return response.text
	        else:
	            return 'Bad Response!'
	```

	Let's mock the response object attributes being used:  `ok` and `text` as following.

	```
	# test_employee.py

	import pytest
	from src.employee import Employee

	emp_1 = Employee("Corey", "Schafer", 50000)

	def test_mock_api_call(mocker):
	    mock_requests = mocker.patch("requests.get")
	    mock_requests.return_value.ok = True
	    mock_requests.return_value.text = "Success"

	    schedule = emp_1.monthly_schedule("May")
	    mock_requests.assert_called_with("http://company.com/Schafer/May")
	    assert schedule == "Success"
	```

- #### Environment Variable (monkeypatch.setenv)

    Sometimes tests need to invoke functionality which depends on global settings or which invokes code which cannot be easily tested such as network access. The `monkeypatch` fixture helps you to safely set/delete an attribute, dictionary item or environment variable, or to modify `sys.path` for importing.

    [https://docs.pytest.org/en/6.2.x/monkeypatch.html](https://docs.pytest.org/en/6.2.x/monkeypatch.html)

    ```
    def use_env_var():
	    contract_class = os.environ['CONTRACT_CLASS']
	    if contract_class == 'en_cloud':
	        # do some processing
	        return "this is en_cloud"
	    if contract_class == 'en_onprem':
	        # do some processing
	        return "this is en_onprem"
	    raise ValueError(f"contract class {contract_class} not found")
    ```
	We can use `mockeypatch.setenv` to set the environment variable.
    ```
    @pytest.mark.parametrize(
    	"mock_contract_class,expect", [("en_cloud", "this is en_cloud"), ("en_onprem", "this is en_onprem")]
	)
	def test_mock_env_var(mock_contract_class, expect, monkeypatch):
	    # more about monkeypatch
	    # https://docs.pytest.org/en/6.2.x/monkeypatch.html
	    monkeypatch.setenv("CONTRACT_CLASS", mock_contract_class)
	    assert use_env_var() == expect
    ```

- #### Exception
    Let's test the same `use_env_var` example, which was just used to demo for Environment Variable, but focusing on the exception scenario.

	Here, we use *pytest.raises* as a context manager to capture the exception of the given type *ValueError*. Here, we could:
	* specify the particular type of the Exception, e.g. ZeroDivisionError, KeyError.
	* specify the value message meets certain format following regular expression.
	
	```
	def test_exception(monkeypatch):
		monkeypatch.setenv("CONTRACT_CLASS", "something not existed")
		with pytest.raises(ValueError, match=r"contract class something not existed not found"):
			use_env_var()
	```


### Key Takeaways
In this tutorial, you've learnt the importance of unit testing, how to use PyTest with parametrizing & fixture and mocking techniques for different scenarios.

And I hope you can still remember the key takeways.

1. Unit Test is the most cheapest and fastest testing strategy within the Test Pyramid.
2. Wirte unit test that is independent, fast, repeatable.
3. Mock where it is used, and not where it's defined (source)

Here is the GitHub with the test cases: https://github.com/trancyquan/how-to-write-unit-test
