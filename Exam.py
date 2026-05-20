class Question:

    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

class QuizSystem:
    def __init__(self):
        self.questions = []
        self.score = 0

    def add_question(self, question):
        self.questions.append(question)

    def start_quiz(self):

        print("\n===== ONLINE QUIZ SYSTEM =====")

        for i in range(len(self.questions)):

            q = self.questions[i]

            print("\nQuestion", i + 1)
            print(q.question)

            for option in q.options:
                print(option)

            user_answer = input("Enter Your Answer: ")

            if user_answer.upper() == q.answer.upper():
                print("Correct Answer!")
                self.score += 1
            else:
                print("Wrong Answer!")
                print("Correct Answer is:", q.answer)

    def show_result(self):

        print("\n===== QUIZ RESULT =====")
        print("Total Score:", self.score)

        if self.score == len(self.questions):
            print("Excellent Performance!")

        elif self.score >= 2:
            print("Good Job!")

        else:
            print("Need More Practice!")


quiz = QuizSystem()

q1 = Question(
    "Which language is used for AI?",
    ["A. Python", "B. HTML", "C. CSS", "D. SQL"],
    "A"
)

q2 = Question(
    "Which keyword is used to create a function in Python?",
    ["A. function", "B. define", "C. def", "D. fun"],
    "C"
)

q3 = Question(
    "Which symbol is used for comments in Python?",
    ["A. //", "B. #", "C. <!-- -->", "D. **"],
    "B"
)

quiz.add_question(q1)
quiz.add_question(q2)
quiz.add_question(q3)

quiz.start_quiz()

quiz.show_result()
