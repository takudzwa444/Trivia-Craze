import datetime
import sys


class Quiz:
    def __init__(self):
        self.name = ""
        self.description = ""
        self.questions = []
        self.score = 0
        self.correct_count = 0
        self.total_points = 0

    
    def print_header(self):
        print("\n\n----------------------------------------")
        print(f"QUIZ NAME: {self.name}")
        print(f"DESCRIPTION: {self.description}")
        print(f"QUESTIONS: {len(self.questions)}")
        print(f"TOTAL POINTS : {self.total_points}")
        print("--------------------------------------------")

    def print_results(self, quiztaker, thefile=sys.stdout):
        print("--------------------------------------------", file=thefile, flush=True)
        # print the results 
        print(f"RESULTS for {quiztaker}",file=thefile, flush=True)
        print(f"DATE: {datetime.datetime.today()}",file=thefile, flush=True)
        print(f"QUESTIONS: {self.correct_count} out of {len(self.questions)} correct", file=thefile, flush=True)
        print(f"SCORE: {self.score} points out of possible {self.total_points}", file=thefile, flush=True)
        print("----------------------------------------------\n", file=thefile, flush=True)

    def take_quiz(self):
        # initialize the quiz state
        self.score = 0
        self.correct_count = 0
        for q in self.questions:
            q.is_correct = False
        # print the header
        self.print_header()
        # execute each question and record the result
        for q in self.questions:
            q.ask()
            if (q.is_correct):
                self.correct_count +=1 
                self.score += q.points
            
        print("---------------------------------------------------\n")
        # return the resuts
        return (self.score, self.correct_count, self.total_points)

 # Creating Question and Answer classes 
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

    qz = Quiz()
    qz.name = "Test Quiz"
    qz.description= "This is the Test Case"

    q1 = QuestonTF()
    q1.text = "Fastest car is here?"
    q1.points = 5
    q1.correct_answer = "t"
    qz.questions.append(q1)
    # q1.ask()

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
    qz.questions.append(q2)
   #  q2.ask()

    qz.total_points = q1.points + q2.points
    result = qz.take_quiz()
    print(result)
