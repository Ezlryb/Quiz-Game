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
        self.quiz_answer_entry.grid_forget()
        self.quiz_answer_radiobutton1.grid_forget()
        self.quiz_answer_radiobutton2.grid_forget()
        self.quiz_answer_radiobutton3.grid_forget()
        self.quiz_answer_radiobutton4.grid_forget()
        self.quiz_question_label.configure(text=question.question)
        if question.number_of_answers == 1:
            self.quiz_answer_entry.grid(column=2, row=0)
        elif question.number_of_answers >= 2:

            self.quiz_answer_radiobutton1.grid(column=0, row=1)
            self.quiz_answer_radiobutton2.grid(column=1, row=1)
            if question.number_of_answers == 3:
                self.quiz_answer_radiobutton3.grid(column=0, row=2, columnspan=2)
            elif question.number_of_answers == 4:
                self.quiz_answer_radiobutton3.grid(column=0, row=2)
                self.quiz_answer_radiobutton4.grid(column=1, row=2)

    def choose_question(self, subjects):
        if self.options_menu_difficulty_variable == 1:
            pass


    def start_quiz(self):
        self.subjects_selected_list = []
        all_quiz_questions = {}
        for button in self.options_menu_subject_check_button_list:
            if str(button.var.get()) != '':
                self.subjects_selected_list.append(button.var.get()) # A list of all selected subjects.
        for subject in self.subjects_selected_list:
            startvar = int(self.options_menu_difficulty_variable.get()*self.QUESTIONS_PER_TOPIC/3)
            endvar = int(self.options_menu_difficulty_variable.get()*self.QUESTIONS_PER_TOPIC/3+self.QUESTIONS_PER_TOPIC/3)
            all_quiz_questions[self.genre[subject].name] = self.genre[subject].questions[startvar:endvar]

        for type, questions in all_quiz_questions.items():
            for question in questions:
                print(type + ": " + question.question + " " + str(question.correct_answer))
        
        
        self.options_menu_frame.grid_forget()


        self.quiz_frame.grid(column=0, row=0)


if __name__ == "__main__":
    root = Tk()
    window = GUI(root)
    root.mainloop()