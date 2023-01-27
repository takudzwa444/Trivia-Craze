from quizmanager import QuizManager

class QuizApp:
    QUIZ_FOLDER = "Quizzes"

    def __init__(self):
        self.username= " "
        self.qm = QuizManager(QuizApp.QUIZ_FOLDER)

    def startup(self):
        self.greeting()
        
        # make the quiz personal to the user
        self.username = input("What is your name? ")
        print(f" Welcome, {self.username}!")
        print()

    def greeting(self):
        print("---------------------------------------------")
        print("---------Welcome to your Trivia Craze ---------")
        print("---------------------------------------------")

    
    def goodbye(self):
        print("---------------------------------------------------")
        print(f"Thanks for using the Trivia Craze, {self.username}!")
        print("---------------------------------------------------")

    def menu(self):
        self.menu_header()
        # Thus will run until the user exits the application
        selection = " "
        while(True):
            selection = input("Selection: ")

            if len(selection) == 0:
                self.menu_error()
                continue

            selection = selection.capitalize()

            if selection[0] == 'E':
                self.goodbye()
                break 

            elif selection[0] == "M":
                self.menu_header()
                continue

            elif selection[0] == "L":
                print()
                print("Available Quizzes are: ")
                # TO ADD THE LIST OF QUIZZES
                
                self.qm.list_quizzes()
                print("-----------------------------------")
                continue

            elif selection[0] == "T":
                try:
                    quiznum = int(input("Quiz number: "))
                    print(f"You have selected quiz {quiznum}")

                    # start the quiz 
                    self.qm.take_quiz(quiznum, self.username)
                    self.qm.print_results()
                    # ask the user if they want to save the results 
                    to_save = input("Would you like to save the results? (y/n)")
                    to_save = to_save.capitalize()
                    if len(to_save) > 0 and to_save[0] == 'Y':
                        self.qm.save_results()
                except:
                    self.menu_error()



    def menu_header(self):
        print("-----------------------------------")
        print("Please make a Selection below:")
        print("(M): Repeat this menu")
        print("(L): List quizzes")
        print("(T) Take a quiz")
        print("(E): Exit program")

    def menu_error(self):
        print("That is not a valid selection. Please try again ")

    # This is the entry point of the program
    def run(self):
        # Execute the startup routine -ask for the name, print greeting
        self.startup()
        # Start the main program menu and run until user exists 
        self.menu()



if __name__ == "__main__":
    app = QuizApp()
    app.run()