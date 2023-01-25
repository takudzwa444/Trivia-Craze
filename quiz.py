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

    def print_results(self):
        print("--------------------------------------------\n")
        print("----------------------------------------------")

    def take_quiz(self):
        # initialize the quiz state
        self.score = 0
        self.correct_count = 0
        self
        # print the header
        # execute each question and record the result
        # return the resuts
