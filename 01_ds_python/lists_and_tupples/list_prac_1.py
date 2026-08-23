def main():
    colors = [25, "red", "green", "blue", "yellow"]
    print("Original list:", colors)
    person = ("Jane Doe", 25, "Python Developer", "Canada")
    # print("Person:", person)

    # Creating a list using range function
    integersList = list(range(24, 12, -2))
    # print("Integers list:", integersList)

    # creating list of even numbers only
    integerList = list(i for i in range(24, 12, -1) if i % 2 == 0)
    # print("Even integers list:", integerList)

    # print("Accessing 2nd element of colors list:", colors[1])
    # print("Accessing 2nd last element of the list using negative indexing:", colors[-2])
    # print("Slicing the list from 2nd to 4th element:", colors[1:4])

    characterList = ["a", "b", "c", "d", "e"]
    print("Character list:", characterList)
    characterList[3] = "G"
    print("Updated character list:", characterList)

    # Delete operation on list
    del characterList[2]
    print("Character list after deleting 3rd element:", characterList)

    # Slicing + updating the list
    characterList[1:3] = ["X", "Y"]
    print("Character list after slicing and updating:", characterList)

    # Appending elements to the list
    x = characterList.append("Z")
    print("Character list after appending an element:", characterList)
    print(x)
    # Append method updates the list in its place, does not create anything new

    # Appending a list of charachter to the existing list
    characterList.extend(["j", "k"])
    print("Character list after extending", characterList)
    print("characterList current length", len(characterList))

    # Inserting an element to the list
    characterList.insert(3, "I")
    print("Characer list after inserting an element", characterList)

    # Removing an element from the list
    # characterList.remove('I')
    # print("Character List after removing the inserted element", characterList)

    # Popping an element from the list, it removes the element from the list and returns the element
    temp = characterList.pop(3)
    print("Character List after removing the inserted element", characterList)
    print("Popped off element", temp)

    # Conditional operators in python
    print('Does character "I" is present in the list ?', "I" in characterList)

    # Packing and unpacking in tupples
    tupple1 = ("Foo", "Bar", "See", "Doc")
    (a1, a2, a3, a4) = tupple1
    print(a1)


main()
