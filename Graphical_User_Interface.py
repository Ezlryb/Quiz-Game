from tkinter import *
from tkinter import messagebox
from tkinter import ttk




class GUI:
    def __init__(self, parent):
        self.parent = parent

        self.start_menu_frame = ttk.Frame(parent)
        #self.start_menu_frame.grid(column=0, row=0)

        self.start_menu_start_button = ttk.Button(self.start_menu_frame, text='Start', command=self.start)
        self.start_menu_start_button.grid(column=0, row=0)

        self.start_menu_quit_button = ttk.Button(self.start_menu_frame, text='quit', command=self.quit)
        self.start_menu_quit_button.grid(column=0, row=1)

        self.quiz_select_frame = ttk.Frame(parent)
        #self.quiz_select_frame.grid(column=0, row=0)

        self.quiz_select_title_label = ttk.Label(self.quiz_select_frame, text='Which quiz?')
        self.quiz_select_title_label.grid(column=0, row=0, columnspan=2)

        self.quiz_select_maths_button = ttk.Button(self.quiz_select_frame, text='Maths')
        self.quiz_select_maths_button.grid(column=0, row=1)

        self.quiz_select_trivia_button = ttk.Button(self.quiz_select_frame, text='Trivia')
        self.quiz_select_trivia_button.grid(column=1, row=1)

        self.quiz_select_puzzles_button = ttk.Button(self.quiz_select_frame, text='Puzzles')
        self.quiz_select_puzzles_button.grid(column=0, row=2)

        self.quiz_select_custom_button = ttk.Button(self.quiz_select_frame, text='Custom')
        self.quiz_select_custom_button.grid(column=1, row=2)

        self.options_menu_frame = ttk.Frame(parent)
        self.options_menu_frame.grid(column=0, row=0)

        self.options_menu_difficulty_label = ttk.Label(self.options_menu_frame, text='Difficulty')
        self.options_menu_difficulty_label.grid(column=0,row=0)

        self.options_menu_difficulty_variable = StringVar()
        self.options_menu_easy_radio_button = ttk.Radiobutton(self.options_menu_frame, text='easy', value='easy', variable=self.options_menu_difficulty_variable)
        self.options_menu_easy_radio_button.grid(column=0, row=1)

        self.options_menu_medium_radio_button = ttk.Radiobutton(self.options_menu_frame, text='medium', value='medium', variable=self.options_menu_difficulty_variable)
        self.options_menu_medium_radio_button.grid(column=0, row=2)

        self.options_menu_hard_radio_button = ttk.Radiobutton(self.options_menu_frame, text='hard', value='hard', variable=self.options_menu_difficulty_variable)
        self.options_menu_hard_radio_button.grid(column=0, row=3)

        self.options_menu_subjects_label = ttk.Label(self.options_menu_frame, text='Subjects')
        self.options_menu_subjects_label.grid(column=1, row=0)


    def start(self):
        self.start_menu_frame.grid_forget()
        self.quiz_select_frame.grid(column=0, row=0)

    def quit(self):
        self.parent.destroy()

    def select_maths(self):
        pass

    def select_puzzles(self):
        pass

    def select_trivia(self):
        pass

    def select_custom(self):
        pass

        



if __name__ == "__main__":
    root = Tk()
    window = GUI(root)
    root.mainloop()