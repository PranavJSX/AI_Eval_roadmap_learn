from fixture import *

def test_always_passes():
    assert True


def test_always_fails():
    assert False


def test_uppercase():
    assert "loud noises".upper() == "LOUD NOISES"


def test_reversed():
    assert list(reversed([1, 2, 3, 4])) == [4, 3, 2, 1]

def test_some_prime():
    assert 37 in {
        num for num in range(2, 50) if not any(num % div == 0 for div in range(2, num))
    }

def main():
    pass


def test_with_fixture(example_fixture):
    assert example_fixture == 1


# TDD, writing a test to verify if an api returns user data as expected

def test_format_data_for_display(example_people_data):
    assert format_data_for_display(example_people_data) == [
        "Alfonsa Ruiz: Senior Software Engineer",
        "Sayid Khan: Project Manager",
    ]


@pytest.mark.skip()
def test_wtr_command_line_option(cmdopt):
    if cmdopt == "type1":
        print("first")
    elif cmdopt == "type2":
        print("second")