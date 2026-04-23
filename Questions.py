class Question:
    def __init__(self, question, correct_answer, incorrect_answer1, incorrect_answer2, incorrect_answer3):
        self.question = question
        self.correct_answer = correct_answer
        self.incorrect_answer = incorrect_answer1
        self.incorrect_answer = incorrect_answer2
        self.incorrect_answer = incorrect_answer3
        self.number_of_answers = 0
        self.count_answers()
    
    def count_answers(self):
        if self.correct_answer != '':
            self.number_of_answers += 1
        elif self.incorrect_answer1 != '':
            self.number_of_answers += 1
        elif self.incorrect_answer2 != '':
            self.number_of_answers += 1
        elif self.incorrect_answer3 != '':
            self.number_of_answers += 1


class Subject:
    def __init__(self, name, genre):
        self.genre = genre
        self.name = name
        self.questions = []
    
    def add_quesiton(self, question, answers):
        while len(answers) != 4:
            answers.append('')
        question_and_answers = Question(question, answers[0], answers[1], answers[2], answers[3])
        self.questions.append(question_and_answers)




maths = {
    'arithmetic': [
        {'question': '1 + 1 =', 'correct_answer': 2},
        {'question': '10 - 4 =', 'correct_answer': 6},
        {'question': '5 + 7 =', 'correct_answer': 12},
        {'question': '12 - 5 =', 'correct_answer': 7},
        {'question': '3 * 4 =', 'correct_answer': 12},
        {'question': '18 / 3 =', 'correct_answer': 6},
        {'question': '25 + 16 =', 'correct_answer': 41},
        {'question': '50 - 22 =', 'correct_answer': 28},
        {'question': '9 * 6 =', 'correct_answer': 54},
        {'question': '64 / 8 =', 'correct_answer': 8},
        {'question': '12 * 11 =', 'correct_answer': 132},
        {'question': '144 / 12 =', 'correct_answer': 12},
        {'question': '125 + 375 =', 'correct_answer': 500},
        {'question': '1000 - 455 =', 'correct_answer': 545},
        {'question': '15 * 15 =', 'correct_answer': 225},
        {'question': '400 / 25 =', 'correct_answer': 16},
        {'question': '2^5 =', 'correct_answer': 32},
        {'question': 'sqrt(169) =', 'correct_answer': 13},
        {'question': '1.2 * 0.5 =', 'correct_answer': 0.6},
        {'question': '3/4 of 80 =', 'correct_answer': 60}
    ],
    'algebra': [
        {'question': 'x + 5 = 10 | x =', 'correct_answer': 5},
        {'question': 'x - 3 = 7 | x =', 'correct_answer': 10},
        {'question': '2x = 12 | x =', 'correct_answer': 6},
        {'question': 'x / 4 = 5 | x =', 'correct_answer': 20},
        {'question': '3x + 2 = 11 | x =', 'correct_answer': 3},
        {'question': '5x - 10 = 15 | x =', 'correct_answer': 5},
        {'question': 'x/2 + 4 = 9 | x =', 'correct_answer': 10},
        {'question': '2(x + 3) = 14 | x =', 'correct_answer': 4},
        {'question': '7x = 3x + 12 | x =', 'correct_answer': 3},
        {'question': 'x^2 = 16 (positive root) | x =', 'correct_answer': 4},
        {'question': '3x + 4 = 0 | x =', 'correct_answer': -1.333},
        {'question': '10 - 2x = 4 | x =', 'correct_answer': 3},
        {'question': '4x + 7 = 2x + 15 | x =', 'correct_answer': 4},
        {'question': 'x/3 - 1 = 2 | x =', 'correct_answer': 9},
        {'question': '5(2x - 1) = 25 | x =', 'correct_answer': 3},
        {'question': 'x^2 - 9 = 0 (positive root) | x =', 'correct_answer': 3},
        {'question': '2x^2 = 50 (positive root) | x =', 'correct_answer': 5},
        {'question': '3(x - 4) = 2(x + 1) | x =', 'correct_answer': 14},
        {'question': 'sqrt(x + 5) = 4 | x =', 'correct_answer': 11},
        {'question': 'x^2 + 5x + 6 = 0 (largest root) | x =', 'correct_answer': -2}
    ],
    'geometry': [
        {'question': 'Sides in a triangle =', 'correct_answer': 3},
        {'question': 'Interior angles of a triangle sum (degrees) =', 'correct_answer': 180},
        {'question': 'Area of a square with side 4 =', 'correct_answer': 16},
        {'question': 'Perimeter of a rectangle (length 5, width 3) =', 'correct_answer': 16},
        {'question': 'Interior angles of a quadrilateral sum (degrees) =', 'correct_answer': 360},
        {'question': 'Area of a triangle (base 10, height 5) =', 'correct_answer': 25},
        {'question': 'Radius of a circle with diameter 14 =', 'correct_answer': 7},
        {'question': 'Hypotenuse of a right triangle (sides 3 and 4) =', 'correct_answer': 5},
        {'question': 'Volume of a cube with side 3 =', 'correct_answer': 27},
        {'question': 'Surface area of a cube with side 2 =', 'correct_answer': 24},
        {'question': 'Area of a circle with radius 7 (use pi=22/7) =', 'correct_answer': 154},
        {'question': 'Complementary angle of 30 degrees =', 'correct_answer': 60},
        {'question': 'Supplementary angle of 110 degrees =', 'correct_answer': 70},
        {'question': 'Number of diagonals in a pentagon =', 'correct_answer': 5},
        {'question': 'Exterior angle of a regular hexagon (degrees) =', 'correct_answer': 60},
        {'question': 'Volume of a cylinder (r=3, h=7, use pi=22/7) =', 'correct_answer': 198},
        {'question': 'Area of a trapezoid (bases 4 & 6, height 5) =', 'correct_answer': 25},
        {'question': 'Slant height of a cone (r=5, h=12) =', 'correct_answer': 13},
        {'question': 'Internal angle of a regular octagon (degrees) =', 'correct_answer': 135},
        {'question': 'Total degrees in an octagon =', 'correct_answer': 1080}
    ]
}

maths_subjects = []
for i, subject in enumerate(maths):
    pass


    





trivia = {'history': [], 
        'mythology': [], 
        'internet': [],
        'geography': [{}],
        }

puzzles = {'riddles': [],
        'anagrams': [],
        'fill in the blank': []}