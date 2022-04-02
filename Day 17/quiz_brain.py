class QuizeBrain:
    
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score= 0
    
    
    def nextQuestion(self):
        user_answer = input(f"Q.{self.question_number + 1} : {self.question_list[self.question_number].text} (true/false)?: ")
        self.checkAnswer(user_answer, self.question_list[self.question_number].answer)
        self.question_number +=1
    
    def still_has_question(self):
        if self.question_number > len(self.question_list) - 1:
            return False
        return True
    
    
    def checkAnswer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            print("You got it right")
            self.score += 1
        else:
            print("you got it wrong !!")
        print(f"The Correct Answer is {correct_answer}")
        print(f"Your score is {self.score}/{self.question_number + 1}")
            

        