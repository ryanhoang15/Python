class Student:

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.num_quiz = 0

    def getName(self):
        return "{}".format(self.name)

    def addQuiz(self, grade):
        self.score = self.score + grade
        self.num_quiz += 1

    def getTotalScore(self):
        return self.score

    def getAverageScore(self):
        return self.score / self.num_quiz


st1 = Student('Jim Black')
print(st1.getName())
st1.addQuiz(10)
st1.addQuiz(20)
print(st1.getTotalScore())
print(st1.getAverageScore())

