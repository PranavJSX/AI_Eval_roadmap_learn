"""
3. List Reverser & Middle Extractor (Slicing)
Goal: Practice advanced list slicing.

Scenario: Given a list of numbers from 1 to 10.

Requirements:

Slice out the middle 6 numbers (from 3 to 8).

Reverse that sliced sub-list using step slicing ([::-1]).

Print both the original list and the reversed sub-list."""

def main():
    mylist = [i for i in range(1,10)]
    slicedList = mylist[2:8]
    reversedList = slicedList[::-1]

    print("Original ", slicedList)
    print("Reversed ",reversedList)

main()