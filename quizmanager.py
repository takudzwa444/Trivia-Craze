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
