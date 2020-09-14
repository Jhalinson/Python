import this


class Student:
    score = 0

    def __init__(self, score):
        this.score = score

    def scoreValue(self):
        grade = []
        x = 0
        self.score = 0
        sum = 0
        while x < 4:
            grades = int(input("Write grade: "))
            x += 1
            grade.append(grades)
            for i in grade:
                sum += i
                self.score += 1
        score = sum / self.score
        if score > 100:
            print("Invalid Score!")
        print("Your score: ",score)



class Arithmetic:

    def add(self, a, b):
        return a + b

    def minus(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b


class Character:
    def moveUp(self):
        pass

    def moveDown(self):
        pass

    def moveRight(self):
        pass

    def moveLeft(self):
        pass


class Mario(Character):
    character = Character()
    character.moveUp()
    character.moveDown()
    character.moveRight()
    character.moveLeft()


class Koopa(Character):
    character = Character()
    character.moveUp()
    character.moveDown()
    character.moveRight()
    character.moveLeft()


class Car:
    fuelQuantity = 0

    def turnOn(self):
        pass


student = Student(100)
student.scoreValue()
arithmetic = Arithmetic()
character = Character()
mario =Mario()
mario.moveUp()
koopa= Koopa()
koopa.moveDown()
