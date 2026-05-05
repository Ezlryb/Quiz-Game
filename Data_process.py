"""Processes data from 'Data.py' to be used in 'Graphical_User_Interface.py'"""
from Data import *


class Question:
    """Store data for each question."""

    def __init__(self, question, correct_answer, incorrect_answer1='', incorrect_answer2='', incorrect_answer3=''):
        """Set up all variables to be referenceable when the object is used."""
        self.question = question  # eg. 1 + 1 = | Who is the capital of Middle Earth? | What getes wetter as it dries?
        self.correct_answer = str(correct_answer)  # eg. 2 | marvin the martian | a towel
        self.incorrect_answer1 = str(incorrect_answer1)  # eg. 3 | donald duck | a candle
        self.incorrect_answer2 = str(incorrect_answer2)  # eg. 1 | me | the human soul
        self.incorrect_answer3 = str(incorrect_answer3)  # eg. 90 | turn it to eleven | quicksand
        self.all_answers = [str(correct_answer), str(incorrect_answer1), str(incorrect_answer2), str(incorrect_answer3)]
        self.trim()
    
    def trim(self):
        """If there are any blank answers, remove them from 'self.all_answers'."""
        while '' in self.all_answers:
            self.all_answers.remove('')


class Subject:
    """Contains a subject of quiz question. Groups together the name of the subject with all the questions in that subject
    eg. self.name = trigonometry, self.genre = maths, self.questions = [Question_object1, Question_object2]
    """

    def __init__(self, name, genre):
        """Set up all variables to be referenceable when the object is used."""
        self.name = name  # eg. trigonometry | history | riddles
        self.genre = genre  # eg. maths | trivia | puzzles
        self.questions = []
    
    def add_quesiton(self, question, answers):
        """Append instance of question object to 'self.questions'. 
        Takes answers as list with correct answer stored in index 0 and any incorrect answers up to 3 in other indexes. 
        If there are not enough incorrect answers input blank string.
        """
        while len(answers) != 4:
            answers.append('')
        question_object = Question(question, answers[0], answers[1], answers[2], answers[3])
        self.questions.append(question_object)



def process_data(data, genre_string):
    """Convert data from 'Data.py' into dictionary used by 'Graphical_User_Interface.py'. 
    If using data from different source thatn Chat GPT (eg. different data structure) change this code.
    """

    return_dictionary = {}
    for subject_string, questions_list in data.items():
        subject_object = Subject(subject_string, genre_string)
        for question_items in questions_list:
            subject_object.add_quesiton(question_items.get('question'), 
                                        [question_items.get('correct_answer'), 
                                        question_items.get('incorrect_answer1', ''), 
                                        question_items.get('incorrect_answer2', ''), 
                                        question_items.get('incorrect_answer3', '')])
        return_dictionary[subject_string] = subject_object
    return return_dictionary

def display_data(genre_dictionary):
    """Testing function. When run displays data with print statments."""

    for subject_name_string, subject in genre_dictionary.items():
        print(f"\n\n{subject_name_string.title()} \n")
        for question in subject.questions:
            print(f"{question.question} {question.correct_answer} {question.incorrect_answer1} {question.incorrect_answer2} {question.incorrect_answer3}")


maths_data = process_data(maths, 'maths') 
trivia_data = process_data(trivia, 'trivia')
puzzle_data = process_data(puzzles, 'puzzles')
all_data = process_data(maths | trivia | puzzles, 'all')  # conjoins the dictionaries of maths trivia and puzzles to be processed in the same way as the other data.
