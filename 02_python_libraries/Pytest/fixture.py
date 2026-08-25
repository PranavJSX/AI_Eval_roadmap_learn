import pytest 

@pytest.fixture
def example_fixture():
    return 1

# @pytest.fixture
def format_data_for_display(people):
    print('Printing people array here',people)
    temp = []
    for data in people:
        name = data['given_name']+ ' '+ data['family_name']
        dict1 = f"{name}: {data['title']}"
        temp.append(dict1)

    return temp

@pytest.fixture
def example_people_data():
    return [
        {
            "given_name":"Alfonsa",
            "family_name":"Ruiz",
            "title":"Senior Software Engineer"
        },
        {
            "given_name": "Sayid",
            "family_name": "Khan",
            "title": "Project Manager",
        },
    ]



def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt", action="store", default="type1", help="my option: type1 or type2"
    )


@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--cmdopt")