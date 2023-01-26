import os
import os.path
import Quizparser
import datetime


class QuizManager:
    def __init__(self, quizfolder):
        self.quizfolder = quizfolder
        # the most recently selected quiz
        self.the_quiz = None
        # inialize the collection of quizzes
        self.quizzes = dict()
        # stores the results of the most recent quiz
        self.results =None
        # the name of the person taking the quiz
        self.quiztaker = ""
        # make sure that the quiz folder exists 
        if (os.path.exists(quizfolder) == False):
            raise FileNotFoundError("The quiz folder does not exist in the location ")
        
        # build the list of quizzes
        self._build_quiz_list()
    def _build_quiz_list(self):
        dircontents = os.scandir(self.quizfolder)
        # parse the xml files in the directory 
        for i, f in enumerate(dircontents):
            if f.is_file():
                parser = Quizparser.QuizParser()
                self.quizzes[i+1] = parser.parse_quiz(f)

    # print a list of the currently installed quizzes 
    def list_quizzes(self):
        for k, v in self.quizzes.items():
            print(f"({k}): {v.name}")

    # start the given quiz for a user and return the results
    def take_quiz(self, quizid, username):
        self.quiztaker = username
        self.the_quiz = self.quizzes[quizid]
        self.results = self.the_quiz.take_quiz()

    # print the results of the most recently taken quiz
    def print_results(self):
        self.the_quiz.print_results(self.quiztaker)

    # save the results of the most recent quiz to the file
    # the file is named using the current date as 
    # QuizResults _YYYY_MM_DD_N (N is incremented until unique)

    def save_results(self):
        pass


if __name__ == "__main__":
    qm = QuizManager("QUIZZES")
    qm.list_quizzes()




