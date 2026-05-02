from Data import *

class Question:
    def __init__(self, question, correct_answer, incorrect_answer1 = '', incorrect_answer2 = '', incorrect_answer3 = ''):
        self.question = question # eg. 1 + 1 = | Who is the capital of Middle Earth? | What getes wetter as it dries?
        self.correct_answer = correct_answer # eg. 2 | marvin the martian | a towel
        self.incorrect_answer1 = incorrect_answer1 # eg. 3 | donald duck | a candle
        self.incorrect_answer2 = incorrect_answer2 # eg. 1 | me | the human soul
        self.incorrect_answer3 = incorrect_answer3 # eg. 90 | turn it to eleven | quicksand
        self.all_answers = [correct_answer, incorrect_answer1, incorrect_answer2, incorrect_answer3]
        self.trim()
    
    def trim(self):    
        while '' in self.all_answers:
            self.all_answers.remove('')


class Subject:
    """Contains a subject of quiz question. Groups together the name of the subject with all the questions in that subject
    eg. self.name = trigonometry, self.genre = maths, self.questions = [Question_object1, Question_object2]"""
    def __init__(self, name, genre):
        self.name = name # eg. trigonometry | history | riddles
        self.genre = genre # eg. maths | trivia | puzzles
        self.questions = []
    
    def add_quesiton(self, question, answers):
        while len(answers) != 4:
            answers.append('')
        question_object = Question(question, answers[0], answers[1], answers[2], answers[3])
        self.questions.append(question_object)



def process_data(data, genre_string):
    """Genre is the """
    return_dictionary = {}
    for subject_string, questions_list in data.items():
        subject_object = Subject(subject_string, genre_string)
        for question_items in questions_list:
            subject_object.add_quesiton(question_items.get('question'), [question_items.get('correct_answer'), question_items.get('incorrect_answer1', ''), question_items.get('incorrect_answer2', ''), question_items.get('incorrect_answer3', '')])
        return_dictionary[subject_string] = subject_object
    return return_dictionary

def display_data(genre_dictionary):
    for subject_name_string, subject in genre_dictionary.items():
        print(f"\n\n{subject_name_string.title()} \n")
        for question in subject.questions:
            print(f"{question.question} {question.correct_answer} {question.incorrect_answer1} {question.incorrect_answer2} {question.incorrect_answer3}")


maths_data = process_data(maths, 'maths')
trivia_data = process_data(trivia, 'trivia')
puzzle_data = process_data(puzzles, 'puzzles')
all_data = process_data(maths | trivia | puzzles, 'all')
