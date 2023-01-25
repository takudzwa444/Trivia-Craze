class Question:
    def __init__(self):
        self.points = 0
        self.correct_answer = ""
        self.text = ""
        self.is_correct = False

    
class QuestonTF(Question):
    def __init__(self):
        super().__init__()
        # TODO: define the ask method 

    def ask(self):
        while(True):
            print(f"(T)rue or (F)alse: {self.text}")
            response = input("? ")
            # check if response was added
            if len(response) == 0:
                print("Sorry, thats not a valid response. Please try again")
                continue
            # check to see if T or F was given
            response = response.lower()
            if response[0] != "t" and response[0]!= "f":
                print("Sorry, thats not a valid response. Please try again")
                continue
            # mark this question as correct
            if response[0] == self.correct_answer:
                self.is_correct = True
            break


class QuestioncMC(Question):
    def __init__(self):
        super().__init__()
        # define the answers for this question
        self.answers = []

    def ask(self):
        while True:
            # Present the question and possible answers
            print(self.text)
            for a in self.answers:
                print(f"({a.name}) {a.text}")
            response = input("?")

            if len(response) == 0:
                print("Sorry, thats not a valid response. Please try again")
                continue
            # Mark this question as correct if answered correctly
            response = response.lower()
            if response[0] == self.correct_answer:
                self.is_correct = True
            break


class Answer:
    def __init__(self):
        # the answer fields
        self.text = ""
        self.name = ""


if __name__ == "__main__":
    q1 = QuestonTF()
    q1.text = "Fastest car is here?"
    q1.points = 5
    q1.correct_answer = "t"
    q1.ask()

    q2 = QuestioncMC()
    q2.text = "what is 3+3"
    q2.points = 10
    q2.correct_answer = "b"
    ans = Answer()
    ans.name = "a"
    ans.text = "3"
    q2.answers.append(ans)
    ans = Answer()
    ans.name = "b"
    ans.text = "6"
    q2.answers.append(ans)
    q2.ask()

    print(q1.is_correct)
    print(q2.is_correct)