from data import question_data
from question_model import Question
from quiz_brain import QuizeBrain

question_bank= []


for question in question_data :
    new_question = Question(question['text'], question['answer'])
    question_bank.append(new_question)

the_question = QuizeBrain(question_bank)

while the_question.still_has_question(): 
    the_question.nextQuestion()

print("You Have Completed The Quiz!")
print(f"Your Score is {the_question.score}")
