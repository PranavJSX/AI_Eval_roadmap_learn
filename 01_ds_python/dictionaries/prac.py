def main():
    config = {
        "color":"green",
        "width":42,
        "height":100,
        "font":"Courier"
    }

    print(f"Print width {config['width']}")

    print("Printing the complete dictionary", config)

    config["font"] = "Helvetica"

    print("Printing the complete dictionary after update", config)

    places = ["Colorado", "Chicago", "Boston"]
    teams = ["Rockies", "White Sox", "Red Sox"]

    teamsDictionary = dict(zip(places,teams))
    print(teamsDictionary)

    fruitsList = ["apple", "orange", "banana", "mango"]
    fruitsDictionary = dict.fromkeys(fruitsList,0)
    print(fruitsDictionary)

    #Complex multi layered dictionaries
    person = {
        "first_name": "John",
        "last_name": "Doe",
        "age": 35,
        "spouse": "Jane",
        "children": ["Ralph", "Betty", "Bob"],
        "pets": {"dog": "Frieda", "cat": "Sox"},
    }
    print(person)

    # to iterate chhildren and pets use below
    print("Print 2nd children:", person["children"][1])
    # to iterate through the nested dictionary
    print("Printing name of the cat: ", person["pets"]["cat"])

    # Using a for loop to populate a dictionary
    squares = {}

    for i in range(0,9):
        squares[i] = i**2

    print("Printing the squares dictionary", squares)

    # Dictionary access methods
    orangeCount = fruitsDictionary.get('orange')
    print(orangeCount)

    print(fruitsDictionary.values())

    # Items method
    print(fruitsDictionary.items())

    # .setDefault method
    inventory = {'orange':100,'banana':80,'pinepple':120}
    inventory.setdefault('mango')

    print(inventory)
    print(inventory.setdefault('mango'))
    inventory.setdefault('mango',55)
    #The below will still print None as value for mango key ? because the .setdefault method works only if the key does not exist in the dictionary
    #else it always returns the current value, it does not udpate it
    print(inventory)

    # .update method - use to merge 1 dictionary with another or any other iterable

    print(fruitsDictionary)
    print(inventory)

    # Updating fruitsDictionary with inventory
    fruitsDictionary.update(inventory)
    print(fruitsDictionary)

    # .pop method, it is used to remove an element from the dictionary if the key exists if it doesn't then an optional default value is returned else
    # key error is thrown

    print("Inventory Dictionary before pop : ", inventory)
    poppedValue = inventory.pop('banana')
    print('poppedValue :', poppedValue)
    print("Inventory Dictionary after popping value", inventory)
    # If below line is included now then we will see a key error
    # inventory.pop('banana')

    # .popitem method, removes an item from the dictionary in the order of LIFO and returns key value pairs of the dictionary

    fruitName, fruitCount = inventory.popitem()
    print(f"fruit name: {fruitName}, fruit count: {fruitCount}")
    print("Dictionary after poping the item off", inventory)

    # operators
    check = ("orange",100) in inventory.items()
    print("Check: ", check)

main()