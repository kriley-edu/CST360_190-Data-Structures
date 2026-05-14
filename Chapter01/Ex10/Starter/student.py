# Write your code below:
import random

class Student:
    def __init__(self, name, numScores):
        self._name = name
        self._scores = [0] * numScores

    def getName(self):
        return self._name

    def getScore(self, index):
        return self._scores[index]

    def setScore(self, index, value):
        self._scores[index] = value

    def getNumScores(self):
        return len(self._scores)

    def getHighScore(self):
        return max(self._scores)

    def getAverage(self):
        return sum(self._scores) / len(self._scores)

    def __str__(self):
        result = f"Name: {self._name}\n"
        for i, score in enumerate(self._scores, start=1):
            result += f"Score {i}: {score}\n"
        return result.strip()

def main(numScores = 3):
    """Tests sorting."""
    # Create the list and put 5 students into it
    students = list()
    names = ("Juan", "Bill", "Stacy", "Maria", "Charley")
    for name in names:
        s = Student(name, numScores)
        for index in range(numScores):
            s.setScore(index, randint(70, 100))
        students.append(s)
    # Print the contents
    print("The list of students:")
    for s in students:
        print(s)
        
if __name__ == "__main__":
    main()
