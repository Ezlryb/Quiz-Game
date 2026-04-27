from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from Data_store import *


class Quiz:
    def __init__(self, type, questions):
        pass


class GUI:
    def __init__(self, parent):
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

        self.quiz_select_custom_button = ttk.Button(self.quiz_select_frame, text='Custom', command=lambda: self.select_genre([maths_data, trivia_data, puzzle_data]))
        self.quiz_select_custom_button.grid(column=1, row=2)

        self.options_menu_frame = ttk.Frame(parent)
        #self.options_menu_frame.grid(column=0, row=0)

        self.options_menu_difficulty_label = ttk.Label(self.options_menu_frame, text='Difficulty')
        self.options_menu_difficulty_label.grid(column=0,row=0)

        self.options_menu_difficulty_frame = ttk.Frame(self.options_menu_frame)
        self.options_menu_difficulty_frame.grid(column=0, row=1)

        self.options_menu_difficulty_variable = StringVar()
        self.options_menu_easy_radio_button = ttk.Radiobutton(self.options_menu_difficulty_frame, text='easy', value='easy', variable=self.options_menu_difficulty_variable)
        self.options_menu_easy_radio_button.grid(column=0, row=0)

        self.options_menu_medium_radio_button = ttk.Radiobutton(self.options_menu_difficulty_frame, text='medium', value='medium', variable=self.options_menu_difficulty_variable)
        self.options_menu_medium_radio_button.grid(column=0, row=1)

        self.options_menu_hard_radio_button = ttk.Radiobutton(self.options_menu_difficulty_frame, text='hard', value='hard', variable=self.options_menu_difficulty_variable)
        self.options_menu_hard_radio_button.grid(column=0, row=2)

        self.options_menu_subjects_label = ttk.Label(self.options_menu_frame, text='Subjects')
        self.options_menu_subjects_label.grid(column=1, row=0)
        
        self.options_menu_subject_check_button_list = []
        self.options_menu_subject_check_button_frame = ttk.Frame(self.options_menu_frame)
        self.options_menu_subject_check_button_frame.grid(column=1, row=1)

        self.options_menu_start_button = ttk.Button(self.options_menu_frame, text='Start', command=self.start_quiz)
        self.options_menu_start_button.grid(column=0, row=4, columnspan=2)

        self.quiz_frame = ttk.Frame(parent)
        self.quiz_frame.grid(column=0, row=0)

        self.quiz_question_label = ttk.Label(self.quiz_frame)
        self.quiz_question_label.grid(column=0, row=1)



    def start(self):
        self.start_menu_frame.grid_forget()
        self.quiz_select_frame.grid(column=0, row=0)

    def quit(self):
        self.parent.destroy()

    def create_subject_checkbuttons(self, genre):
        return_list = []
        for subject_string in genre.keys():
            temp_variable = StringVar()
            temp_button = ttk.Checkbutton(self.options_menu_subject_check_button_frame, variable=temp_variable, text=subject_string, onvalue=subject_string, offvalue='off')
            temp_button.var = temp_variable
            temp_button.pack()
            temp_button
            return_list.append(subject_string)
            self.options_menu_subject_check_button_list.append(temp_button)
        return return_list

    def select_genre(self, genre):
        self.genre = genre
        self.subjects_list = []
        if type(self.genre) == list:
            for item in genre:
                self.subjects_list += self.create_subject_checkbuttons(item)
        else:
            self.subjects_list = self.create_subject_checkbuttons(genre)
        
        self.options_menu_subject_check_button_list = [self.create_subject_checkbuttons]

        self.quiz_select_frame.grid_forget()
        self.options_menu_frame.grid(column=0, row=0)
        
    def start_quiz(self):
        pass


if __name__ == "__main__":
    root = Tk()
    window = GUI(root)
    root.mainloop()