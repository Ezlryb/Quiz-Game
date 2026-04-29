from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from Data_process import *
from random import *


class GUI:
    def __init__(self, parent):
        self.QUESTIONS_PER_TOPIC = 21
        self.parent = parent
        self.genre = ''
        self.subjects_list = ''

        self.start_menu_frame = ttk.Frame(parent)
        self.start_menu_frame.grid(column=0, row=0)
  
        self.start_menu_start_button = ttk.Button(self.start_menu_frame, text='Start', command=self.start)
        self.start_menu_start_button.grid(column=0, row=0)

        self.start_menu_quit_button = ttk.Button(self.start_menu_frame, text='quit', command=self.quit)
        self.start_menu_quit_button.grid(column=0, row=1)

        self.quiz_select_frame = ttk.Frame(parent)
        #self.quiz_select_frame.grid(column=0, row=0)

        self.quiz_select_title_label = ttk.Label(self.quiz_select_frame, text='Which quiz?')
        self.quiz_select_title_label.grid(column=0, row=0, columnspan=2)

        self.quiz_select_maths_button = ttk.Button(self.quiz_select_frame, text='Maths', command=lambda: self.select_genre(maths_data))
        self.quiz_select_maths_button.grid(column=0, row=1)

        self.quiz_select_trivia_button = ttk.Button(self.quiz_select_frame, text='Trivia', command=lambda: self.select_genre(trivia_data))
        self.quiz_select_trivia_button.grid(column=1, row=1)

        self.quiz_select_puzzles_button = ttk.Button(self.quiz_select_frame, text='Puzzles', command=lambda: self.select_genre(puzzle_data))
        self.quiz_select_puzzles_button.grid(column=0, row=2)

        self.quiz_select_custom_button = ttk.Button(self.quiz_select_frame, text='Custom', command=lambda: self.select_genre(all_data))
        self.quiz_select_custom_button.grid(column=1, row=2)

        self.options_menu_frame = ttk.Frame(parent)
        #self.options_menu_frame.grid(column=0, row=0)

        self.options_menu_difficulty_label = ttk.Label(self.options_menu_frame, text='Difficulty')
        self.options_menu_difficulty_label.grid(column=0,row=0)

        self.options_menu_difficulty_frame = ttk.Frame(self.options_menu_frame)
        self.options_menu_difficulty_frame.grid(column=0, row=1)

        self.options_menu_difficulty_variable = IntVar()
        self.options_menu_easy_radio_button = ttk.Radiobutton(self.options_menu_difficulty_frame, text='easy', value=0, variable=self.options_menu_difficulty_variable)
        self.options_menu_easy_radio_button.grid(column=0, row=0)

        self.options_menu_medium_radio_button = ttk.Radiobutton(self.options_menu_difficulty_frame, text='medium', value=1, variable=self.options_menu_difficulty_variable)
        self.options_menu_medium_radio_button.grid(column=0, row=1)

        self.options_menu_hard_radio_button = ttk.Radiobutton(self.options_menu_difficulty_frame, text='hard', value=2, variable=self.options_menu_difficulty_variable)
        self.options_menu_hard_radio_button.grid(column=0, row=2)

        self.options_menu_subjects_label = ttk.Label(self.options_menu_frame, text='Subjects')
        self.options_menu_subjects_label.grid(column=1, row=0)
        
        self.options_menu_subject_check_button_list = []

        self.options_menu_subject_check_button_frame = ttk.Frame(self.options_menu_frame)
        self.options_menu_subject_check_button_frame.grid(column=1, row=1)

        self.options_menu_start_button = ttk.Button(self.options_menu_frame, text='Start', command=self.start_quiz)
        self.options_menu_start_button.grid(column=0, row=4, columnspan=2)

        self.question_pick_frame = ttk.Frame(parent)
        
        self.questions_pick_button1 = ttk.Button(self.question_pick_frame)
        self.questions_pick_button2 = ttk.Button(self.question_pick_frame)
        self.questions_pick_button3 = ttk.Button(self.question_pick_frame)
        self.questions_pick_button4 = ttk.Button(self.question_pick_frame)



        self.quiz_frame = ttk.Frame(parent)
        # self.quiz_frame.grid(column=0, row=0)

        self.quiz_question_label = ttk.Label(self.quiz_frame, text='test')
        self.quiz_question_label.grid(column=0, row=0, columnspan=2)

        self.quiz_answer_variable = StringVar()
        self.quiz_answer_entry = ttk.Entry(self.quiz_frame)
        
        self.quiz_answer_radiobutton1 = ttk.Radiobutton(self.quiz_frame, variable=self.quiz_answer_variable)
        self.quiz_answer_radiobutton2 = ttk.Radiobutton(self.quiz_frame, variable=self.quiz_answer_variable)
        self.quiz_answer_radiobutton3 = ttk.Radiobutton(self.quiz_frame, variable=self.quiz_answer_variable)
        self.quiz_answer_radiobutton4 = ttk.Radiobutton(self.quiz_frame, variable=self.quiz_answer_variable)

        self.quiz_check_right_answer_button = ttk.Button(self.quiz_frame, text='Check')
        self.quiz_check_right_answer_button.grid(column=0, row=3)
        
        self.quiz_next_button = ttk.Button(self.quiz_frame, text='Next >', state=DISABLED)
        self.quiz_next_button.grid(column=1, row=3)

    def start(self):
        self.start_menu_frame.grid_forget()
        self.quiz_select_frame.grid(column=0, row=0)

    def quit(self):
        self.parent.destroy()

    def create_subject_checkbuttons(self):
        return_list = []
        for subject_string in self.genre.keys():
            var = StringVar()
            temp_button = ttk.Checkbutton(self.options_menu_subject_check_button_frame, variable=var, text=subject_string, onvalue=subject_string, offvalue='')
            temp_button.var = var
            temp_button.pack()
            temp_button
            return_list.append(subject_string)
            self.options_menu_subject_check_button_list.append(temp_button)
        return return_list

    def select_genre(self, genre):
        self.genre = genre
        self.subjects_list = []
        self.subjects_list = self.create_subject_checkbuttons()
        self.quiz_select_frame.grid_forget()
        self.options_menu_frame.grid(column=0, row=0)

    def quiz_entry_button_setup(self, question):
        answers = question.all_answers
        shuffle(answers)
        self.quiz_answer_entry.grid_forget()
        self.quiz_answer_radiobutton1.grid_forget()
        self.quiz_answer_radiobutton2.grid_forget()
        self.quiz_answer_radiobutton3.grid_forget()
        self.quiz_answer_radiobutton4.grid_forget()
        self.quiz_question_label.configure(text=question.question)
        if len(question.all_answers) == 1:
            self.quiz_answer_entry.grid(column=2, row=0)
        elif len(question.all_answers) >= 2:
            self.quiz_answer_radiobutton1.configure(text=answers[0], value=answers[0])
            self.quiz_answer_radiobutton2.configure(text=answers[1], value=answers[1])
            self.quiz_answer_radiobutton1.grid(column=0, row=1)
            self.quiz_answer_radiobutton2.grid(column=1, row=1)
            if len(question.all_answers) == 3:
                self.quiz_answer_radiobutton3.configure(text=answers[2], value=answers[2])
                self.quiz_answer_radiobutton3.grid(column=0, row=2, columnspan=2)
            elif len(question.all_answers) == 4:
                self.quiz_answer_radiobutton3.configure(text=answers[2], value=answers[2])
                self.quiz_answer_radiobutton4.configure(text=answers[3], value=answers[3])
                self.quiz_answer_radiobutton3.grid(column=0, row=2)
                self.quiz_answer_radiobutton4.grid(column=1, row=2)

    def begin_question(self, subject):
        self.question_pick_frame.grid_forget()
        self.currect_question = self.all_quiz_questions[subject].pop(randrange(len(self.all_quiz_questions[subject])))
        self.quiz_entry_button_setup(self.currect_question)
        self.quiz_frame.grid(column=0, row=0)   

    def choose_question(self):
        if len(self.all_quiz_questions.keys()) >= 4:
            subjects = sample(list(self.all_quiz_questions.keys()), 4)
            self.questions_pick_button3.configure(text=subjects[2], command=lambda: self.begin_question(subjects[2]), state=NORMAL)
            self.questions_pick_button4.configure(text=subjects[3], command=lambda: self.begin_question(subjects[3]), state=NORMAL)
            self.questions_pick_button3.grid(column=0, row=2)
            self.questions_pick_button4.grid(column=1, row=2)
        else:
            subjects = list(self.all_quiz_questions.keys())
        if len(self.all_quiz_questions.keys()) == 1:
            self.begin_question(subjects[0])
        elif len(self.all_quiz_questions.keys()) >= 2:
            self.questions_pick_button1.configure(text=subjects[0], command=lambda: self.begin_question(subjects[0]), state=NORMAL)
            self.questions_pick_button2.configure(text=subjects[1], command=lambda: self.begin_question(subjects[1]), state=NORMAL)
            self.questions_pick_button1.grid(column=0, row=1)
            self.questions_pick_button2.grid(column=1, row=1)
        if len(self.all_quiz_questions.keys()) == 3:
            self.questions_pick_button3.configure(text=subjects[2], command=lambda: self.begin_question(subjects[2]), state=NORMAL)
            self.questions_pick_button3.grid(column=0, row=2, columnspan=2)
        self.question_pick_frame.grid(column=0, row=0)

    def start_quiz(self):
        self.subjects_selected_list = []
        self.all_quiz_questions = {}
        for button in self.options_menu_subject_check_button_list:
            if str(button.var.get()) != '':
                self.subjects_selected_list.append(button.var.get()) # A list of all selected subjects.
        for subject in self.subjects_selected_list:
            startvar = int(self.options_menu_difficulty_variable.get()*self.QUESTIONS_PER_TOPIC/3) # gets the first value in the subject list of questions to pull from
            endvar = int(self.options_menu_difficulty_variable.get()*self.QUESTIONS_PER_TOPIC/3+self.QUESTIONS_PER_TOPIC/3) # gets the last ^^^
            self.all_quiz_questions[self.genre[subject].name] = self.genre[subject].questions[startvar:endvar] 
        self.options_menu_frame.grid_forget()
        self.choose_question()

    def check_answer(self):
        if self.quiz_answer_variable == self.currect_question:
            pass
        else:
            pass
        self.quiz_check_right_answer_button['state'] = DISABLED
        self.quiz_answer_radiobutton1['state'] = DISABLED
        self.quiz_answer_radiobutton2['state'] = DISABLED
        self.quiz_answer_radiobutton3['state'] = DISABLED
        self.quiz_answer_radiobutton4['state'] = DISABLED
        self.quiz_next_button['state'] = NORMAL



if __name__ == "__main__":
    root = Tk()
    window = GUI(root)
    root.mainloop()