"""
Project 2: High-Score Leaderboard & Medal Unpacker
This project tests list sorting and top-element unpacking.

Scenario: A game tracks scores as a list of player tuples: (player_name, score).

Python
scores = [
    ("Maya", 450),
    ("Liam", 820),
    ("Sophia", 610),
    ("Jackson", 950),
    ("Ethan", 730)
]
Requirements:

Sort the scores list from highest score to lowest score using Python's built-in sorted() or .sort() (Hint: look at the key or reverse parameters).

Take the top 3 scores from the list.

Unpack the top 3 player tuples into three variables: gold, silver, and bronze.

Unpack each medal winner's tuple to announce the results:

Plaintext
🥇 Gold Medal: Jackson with 950 points!
🥈 Silver Medal: Liam with 820 points!
🥉 Bronze Medal: Ethan with 730 points!"""

scores = [
    ("Maya", 450),
    ("Liam", 820),
    ("Sophia", 610),
    ("Jackson", 950),
    ("Ethan", 730)
]


def main():
    scores.sort(key= lambda score:score[1], reverse=True)
    print(scores)
    gold, silver, bronze = scores[:3]
    print(f"Gold Medal: {gold[0]} with {gold[1]} points!")
    print(f"Silver Medal: {silver[0]} with {silver[1]} points!")
    print(f"Bronze Medal: {bronze[0]} with {bronze[1]} points!")    

main()
