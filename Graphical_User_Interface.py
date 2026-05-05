"""Create the GUI run the main routine."""

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from Data_process import *
from random import *
from pathlib import Path


class GUI:
    """Run the logic and control the elements of the GUI."""

    def __init__(self, parent):
        """Run when GUI created, create a gobal variable to access the root node then run the Create UI funcion."""
        self.parent = parent
        self.create_ui()

    def create_ui(self):
        """Initialize all widgets and variables and reset them when run more than once."""
        parent = self.parent
        self.button_colours = ["#DFDFDF", "#c1c0c0", "#eaeaea", "#d4d2d2"]
        self.background_colours = ['white', 'grey']
        self.MATHS_BACKGROUND_COLOURS = ["#a7c0e5", "#DAE6F8"]
        self.TRIVIA_BACKGROUND_COLOURS = ['#afdead', "#B7F1B7"]
        self.PUZZLES_BACKGROUND_COLOURS = ["#deadb2", "#fbcfd2"]
        self.CUSTOM_BACKGROUND_COLOURS = ["#ebeab3", "#F2F2C8"]
        self.path = Path(__file__).parent
        self.photo_path = self.path / 'image_files' / 'quiz_logo.gif'
        self.QUESTIONS_PER_TOPIC = 21
        self.questions_left = self.QUESTIONS_PER_TOPIC//3
        self.parent = parent
        self.genre = ''
        self.subjects_list = ''

        self.gui_style = ttk.Style()
        self.gui_style.theme_use('clam')

        self.gui_style.configure("quiz_colour.TFrame", background=self.background_colours[0])
        self.start_menu_frame = ttk.Frame(parent, style="quiz_colour.TFrame")
        self.start_menu_frame.columnconfigure(0, weight=1)
        self.start_menu_frame.columnconfigure(1, weight=1)
        self.start_menu_frame.rowconfigure(0, weight=1)
        self.start_menu_frame.rowconfigure(1, weight=1)
        self.start_menu_frame.grid(column=0, row=0, sticky=NSEW)

        self.start_menu_image = PhotoImage(file=self.photo_path)
        self.gui_style.configure("start_menu_image_label.TLabel", borderwidth = 0)
        self.start_menu_image_label = ttk.Label(self.start_menu_frame, image=self.start_menu_image, style="start_menu_image_label.TLabel")
        self.start_menu_image_label.grid(column=0, row=0, rowspan=2)

        self.gui_style.configure("start_menu_start_button.TButton")
        self.start_menu_start_button = ttk.Button(self.start_menu_frame, text='Start', command=self.start, style="start_menu_start_button.TButton")
        self.start_menu_start_button.grid(column=1, row=0, sticky='SEW', padx=(10, 50), pady=10, ipadx=10, ipady=10)

        self.start_menu_quit_button = ttk.Button(self.start_menu_frame, text='Quit', command=self.quit)
        self.start_menu_quit_button.grid(column=1, row=1, sticky='NEW', padx=(10, 50), pady=10, ipadx=10, ipady=10)

        self.quiz_select_frame = ttk.Frame(parent, style="quiz_colour.TFrame")
        self.quiz_select_frame.columnconfigure(0, weight=1)
        self.quiz_select_frame.columnconfigure(1, weight=1)
        self.quiz_select_frame.rowconfigure(0, weight=1)
        self.quiz_select_frame.rowconfigure(1, weight=1)
        self.quiz_select_frame.rowconfigure(2, weight=1)
        #self.quiz_select_frame.grid(column=0, row=0, sticky=NSEW)

        self.gui_style.configure("quiz_select_title_label.TLabel", font=('Arial', 50), background='white')
        self.quiz_select_title_label = ttk.Label(self.quiz_select_frame, text='Choose Your topic:', style="quiz_select_title_label.TLabel")
        self.quiz_select_title_label.grid(column=0, row=0, columnspan=2, pady=30)

        self.gui_style.configure('quiz_select_maths_button.TButton', font=('Arial', 30))
        self.gui_style.map("quiz_select_maths_button.TButton", background=[('!active', self.MATHS_BACKGROUND_COLOURS[0],), ('active', self.MATHS_BACKGROUND_COLOURS[1])])
        self.quiz_select_maths_button = ttk.Button(self.quiz_select_frame, text='Maths', command=lambda: self.select_genre(maths_data, self.MATHS_BACKGROUND_COLOURS), style="quiz_select_maths_button.TButton")
        self.quiz_select_maths_button.grid(column=0, row=1, sticky='sew', ipadx=10, ipady=50, padx=(20, 5), pady=5)

        self.gui_style.configure('quiz_select_trivia_button.TButton', font=('Arial', 30))
        self.gui_style.map("quiz_select_trivia_button.TButton", background=[('!active', self.TRIVIA_BACKGROUND_COLOURS[0],), ('active', self.TRIVIA_BACKGROUND_COLOURS[1])])
        self.quiz_select_trivia_button = ttk.Button(self.quiz_select_frame, text='Trivia', command=lambda: self.select_genre(trivia_data, self.TRIVIA_BACKGROUND_COLOURS), style="quiz_select_trivia_button.TButton")
        self.quiz_select_trivia_button.grid(column=1, row=1, sticky='sew', ipadx=10, ipady=50, padx=(5, 20), pady=5)

        self.gui_style.configure("quiz_select_puzzles_button.TButton", font=('Arial', 30))
        self.gui_style.map("quiz_select_puzzles_button.TButton", background=[('!active', self.PUZZLES_BACKGROUND_COLOURS[0],), ('active', self.PUZZLES_BACKGROUND_COLOURS[1])])
        self.quiz_select_puzzles_button = ttk.Button(self.quiz_select_frame, text='Puzzles', command=lambda: self.select_genre(puzzle_data, self.PUZZLES_BACKGROUND_COLOURS), style="quiz_select_puzzles_button.TButton")
        self.quiz_select_puzzles_button.grid(column=0, row=2, sticky='new', ipadx=10, ipady=50, padx=(20, 5), pady=5)

        self.gui_style.configure("quiz_select_custom_button.TButton", font=('Arial', 30))
        self.gui_style.map("quiz_select_custom_button.TButton", background=[('!active', self.CUSTOM_BACKGROUND_COLOURS[0],), ('active', self.CUSTOM_BACKGROUND_COLOURS[1])])
        self.quiz_select_custom_button = ttk.Button(self.quiz_select_frame, text='Custom', command=lambda: self.select_genre(all_data, self.CUSTOM_BACKGROUND_COLOURS), style="quiz_select_custom_button.TButton")
        self.quiz_select_custom_button.grid(column=1, row=2, sticky='new', ipadx=10, ipady=50, padx=(5, 20), pady=5)

        self.options_menu_frame = ttk.Frame(parent, style='quiz_colour.TFrame')
        self.options_menu_frame.columnconfigure(0, weight=1)
        self.options_menu_frame.columnconfigure(1, weight=1)
        self.options_menu_frame.rowconfigure(0, weight=1)
        self.options_menu_frame.rowconfigure(1, weight=1)
        self.options_menu_frame.rowconfigure(2, weight=2)
        
        self.gui_style.configure('options_menu_labels.TLabel', background='white', font=('Arial', 30))
        self.options_menu_difficulty_label = ttk.Label(self.options_menu_frame, text='Choose Your Difficulty: ', style='options_menu_labels.TLabel')
        self.options_menu_difficulty_label.grid(column=0,row=0)

        self.options_menu_difficulty_frame = ttk.Frame(self.options_menu_frame, style='quiz_colour.TFrame')
        self.options_menu_difficulty_frame.columnconfigure(0, weight=1)
        self.options_menu_difficulty_frame.grid(column=0, row=1)

        self.gui_style.configure('difficulty_radio_buttons.TRadiobutton', background='white', relief=FLAT, anchor='center', font=('Arial', 30))
        self.gui_style.layout('difficulty_radio_buttons.TRadiobutton', [('Radiobutton.border', {'sticky': 'nsew', 'children': [('Radiobutton.focus', {'sticky': 'nsew', 'children': [('Radiobutton.label', {'sticky': 'nsew'})]})], 'sticky': 'nsew'})])
        self.gui_style.map('difficulty_radio_buttons.TRadiobutton', background=[('active selected', self.button_colours[3]), ('active', self.button_colours[2]), ('selected', self.button_colours[1]), ('!selected', self.button_colours[0])], relief=[('selected', 'sunken'), ('!selected', 'raised')])
        self.options_menu_difficulty_variable = IntVar()
        self.options_menu_difficulty_variable.set(-1)
        self.options_menu_easy_radio_button = ttk.Radiobutton(self.options_menu_difficulty_frame, text='Easy', value=0, variable=self.options_menu_difficulty_variable, style='difficulty_radio_buttons.TRadiobutton')
        self.options_menu_easy_radio_button.grid(column=0, row=0, padx=10, pady=10, ipadx=50, ipady=10, sticky='nsew')

        self.options_menu_medium_radio_button = ttk.Radiobutton(self.options_menu_difficulty_frame, text='Medium', value=1, variable=self.options_menu_difficulty_variable, style='difficulty_radio_buttons.TRadiobutton')
        self.options_menu_medium_radio_button.grid(column=0, row=1, padx=10, pady=10, ipadx=50, ipady=10, sticky='nsew')

        self.options_menu_hard_radio_button = ttk.Radiobutton(self.options_menu_difficulty_frame, text='Hard', value=2, variable=self.options_menu_difficulty_variable, style='difficulty_radio_buttons.TRadiobutton')
        self.options_menu_hard_radio_button.grid(column=0, row=2, padx=10, pady=10, ipadx=50, ipady=10, sticky='nsew')

        
        self.options_menu_subjects_label = ttk.Label(self.options_menu_frame, text='Choose Your Subjects: ', style='options_menu_labels.TLabel')
        self.options_menu_subjects_label.grid(column=1, row=0)
        
        self.options_menu_subject_check_button_list = []

        self.options_menu_subject_check_button_frame = ttk.Frame(self.options_menu_frame, style="quiz_colour.TFrame")
        self.options_menu_subject_check_button_frame.grid(column=1, row=1, ipadx=20, ipady=20)

        self.options_menu_start_button = ttk.Button(self.options_menu_frame, text='Start', command=self.start_quiz)
        self.options_menu_start_button.grid(column=0, row=2, columnspan=2)

        self.question_pick_frame = ttk.Frame(parent, style='quiz_colour.TFrame')
        self.question_pick_frame.columnconfigure(0, weight=1)
        self.question_pick_frame.columnconfigure(1, weight=1)
        self.question_pick_frame.rowconfigure(0, weight=1)
        self.question_pick_frame.rowconfigure(1, weight=1)
        self.question_pick_frame.rowconfigure(2, weight=1)
    
        self.gui_style.configure('question_pick_title_label.TLabel', font=('Arial', 30))
        self.question_pick_title_label = ttk.Label(self.question_pick_frame, text="Select Your Next Question's Topic: ", style='question_pick_title_label.TLabel')
        self.question_pick_title_label.grid(column=0, row=0, columnspan=2)
        
        self.gui_style.configure('questions_pick_button.TButton', font=('Arial', 20))
        self.questions_pick_button1 = ttk.Button(self.question_pick_frame, style='questions_pick_button.TButton')
        self.questions_pick_button2 = ttk.Button(self.question_pick_frame, style='questions_pick_button.TButton')
        self.questions_pick_button3 = ttk.Button(self.question_pick_frame, style='questions_pick_button.TButton')
        self.questions_pick_button4 = ttk.Button(self.question_pick_frame, style='questions_pick_button.TButton')

        self.quiz_frame = ttk.Frame(parent, style="quiz_colour.TFrame")
        self.quiz_frame.columnconfigure(0, weight=1)
        self.quiz_frame.columnconfigure(1, weight=1)
        self.quiz_frame.rowconfigure(0, weight=1)
        self.quiz_frame.rowconfigure(1, weight=1)
        self.quiz_frame.rowconfigure(2, weight=1)
        self.quiz_frame.rowconfigure(3, weight=1)
        self.quiz_frame.rowconfigure(4, weight=1)

        self.gui_style.configure('quiz_question_label.TLabel', background=self.background_colours[0], font=('Arial', 20), relief='raised')
        self.quiz_question_label = ttk.Label(self.quiz_frame, text='', style='quiz_question_label.TLabel', anchor=CENTER)
        self.quiz_question_label.grid(column=0, row=0, columnspan=2, sticky=NSEW, ipadx=20, ipady=20, padx=20, pady=20)

        self.quiz_answer_variable = StringVar()
        self.quiz_answer_entry = ttk.Entry(self.quiz_frame, textvariable=self.quiz_answer_variable)
        
        self.gui_style.configure('quiz_answer_radiobutton.TRadiobutton', background='white', font=('Arial', 20), anchor=CENTER)
        self.gui_style.layout('quiz_answer_radiobutton.TRadiobutton', [('Radiobutton.border', {'sticky': 'nsew', 'children': [('Radiobutton.focus', {'sticky': 'nsew', 'children': [('Radiobutton.label', {'sticky': 'nsew'})]})], 'sticky': 'nsew'})])
        self.gui_style.map('quiz_answer_radiobutton.TRadiobutton', background=[('active selected', self.button_colours[3]), ('active', self.button_colours[2]), ('!selected', self.button_colours[0]), ('selected', self.button_colours[1])], relief=[('!selected', 'raised'), ('selected', 'sunken')])
        self.quiz_answer_radiobutton1 = ttk.Radiobutton(self.quiz_frame, variable=self.quiz_answer_variable, style='quiz_answer_radiobutton.TRadiobutton')
        self.quiz_answer_radiobutton2 = ttk.Radiobutton(self.quiz_frame, variable=self.quiz_answer_variable, style='quiz_answer_radiobutton.TRadiobutton')
        self.quiz_answer_radiobutton3 = ttk.Radiobutton(self.quiz_frame, variable=self.quiz_answer_variable, style='quiz_answer_radiobutton.TRadiobutton')
        self.quiz_answer_radiobutton4 = ttk.Radiobutton(self.quiz_frame, variable=self.quiz_answer_variable, style='quiz_answer_radiobutton.TRadiobutton')

        self.gui_style.configure('quiz_correct_incorrect_label.TLabel', background=self.background_colours, font=('Arial', 20), relief='raised')
        self.quiz_correct_incorrect_label = ttk.Label(self.quiz_frame, text='', style='quiz_correct_incorrect_label.TLabel', anchor=CENTER)
        
        self.quiz_check_answer_button = ttk.Button(self.quiz_frame, text='Check', command=self.check_answer)
        self.quiz_check_answer_button.grid(column=0, row=4)
        
        self.quiz_next_button = ttk.Button(self.quiz_frame, text='Next >', state=DISABLED, command=self.choose_question)
        self.quiz_next_button.grid(column=1, row=4)

        self.end_frame = ttk.Frame(parent, style='quiz_colour.TFrame')
        self.end_frame.columnconfigure(0, weight=1)
        self.end_frame.columnconfigure(1, weight=1)
        self.end_frame.rowconfigure(0, weight=1)
        self.end_frame.rowconfigure(1, weight=1)
        self.end_frame.rowconfigure(2, weight=1)

        self.end_stats_correct_questions_counter_variable = 0
        self.end_stats_incorrect_questions_counter_variable = 0

        self.gui_style.configure('end_title_label.TLabel', font=('Arial', 30))
        self.end_title_label = ttk.Label(self.end_frame, text='Quiz Complete', style='end_title_label.TLabel')
        self.end_title_label.grid(column=0, row=0, columnspan=2)
        
        self.gui_style.configure('end_stats_label.TLabel', font=('Arial', 20))
        self.end_stats_label = ttk.Label(self.end_frame, text='Questions Answered: \n\nQuestions Correct: \n\nQuestions Incorrect: \n\nScore:', style='end_stats_label.TLabel')
        self.end_stats_label.grid(column=0, row=1)

        self.end_stats_display_label = ttk.Label(self.end_frame, text='', style='end_stats_label.TLabel')
        self.end_stats_display_label.grid(column=1, row=1)

        self.end_return_to_start_button = ttk.Button(self.end_frame, text='Home >', command=self.return_home)
        self.end_return_to_start_button.grid(column=0, row=2, columnspan=2)

    def start(self):
        """Trigger when start button pressed, switches frames from 'start_menu_frame' to 'quiz_select_frame.'"""
        self.start_menu_frame.grid_forget()
        self.quiz_select_frame.grid(column=0, row=0, sticky=NSEW)

    def quit(self):
        """Trigger when quit button pressed, closes the window."""
        self.parent.destroy()

    def create_subject_checkbuttons(self):
        """Trigger when genre of quiz selected (from 'select_genre()'), creates a list of checkbuttons with the subject options (eg. history, algebra) and packs them into a frame. 
        The checkbuttons change size depending on how many of them there are. Their size is capped between font size 25 and 10."""
        return_list = []
        self.gui_style.configure('temp_button.TCheckbutton', background=self.background_colours[0])
        for i, subject_string in enumerate(self.genre.keys()):
            var = StringVar()
            size = 100//(i//2+3)
            if size > 25:
                size = 25
            elif size < 10:
                size = 10
            self.gui_style.configure('temp_button.TCheckbutton', font=('Arial', size))
            temp_button = ttk.Checkbutton(self.options_menu_subject_check_button_frame, variable=var, text=subject_string.title(), onvalue=subject_string, offvalue='', style='temp_button.TCheckbutton')
            temp_button.var = var
            temp_button.pack(padx=size//5, pady=size//5, ipadx=size//10, ipady=2, anchor='w')
            temp_button
            return_list.append(subject_string)
            self.options_menu_subject_check_button_list.append(temp_button)
            self.options_menu_subject_check_button_frame.rowconfigure(i, weight=1)
        return return_list

    def select_genre(self, genre, colour):
        """Trigger when genre of quiz is selected, update visuals to be themed of 'options_menu_frame' and childeren based on which genre was selected (eg. Maths: blue, Custom: yellow).
        Run 'create_subject_checkbuttons()' and switch frames from 'quiz_select_frame' to 'options_menu_frame'"""
        self.background_colours = colour
        self.gui_style.configure('quiz_colour.TFrame', background=colour[0])
        self.gui_style.configure('options_menu_labels.TLabel', background=colour[0])
        self.gui_style.configure('question_pick_title_label.TLabel', background=colour[0])
        self.options_menu_frame.configure(style='quiz_colour.TFrame')
        self.genre = genre
        self.subjects_list = []
        self.subjects_list = self.create_subject_checkbuttons()
        self.quiz_select_frame.grid_forget()
        self.options_menu_frame.configure()
        self.options_menu_frame.grid(column=0, row=0, sticky=NSEW)

    def quiz_entry_button_setup(self, question):
        """Trigger when starting a question (from 'begin_question()' function), set up buttons or entery in the 
        correct configuration depending on how many answers to a question there are."""
        answers = question.all_answers
        shuffle(answers)
        self.quiz_answer_entry.grid_forget()
        self.quiz_answer_radiobutton1.grid_forget()
        self.quiz_answer_radiobutton2.grid_forget()
        self.quiz_answer_radiobutton3.grid_forget()
        self.quiz_answer_radiobutton4.grid_forget()
        self.quiz_question_label.configure(text=question.question.title())
        if len(question.all_answers) == 1:
            self.quiz_answer_entry.configure(state=NORMAL)
            self.quiz_answer_entry.delete(0, END)
            self.quiz_answer_entry.focus()
            self.quiz_answer_entry.grid(column=0, row=1, ipadx=100, columnspan=2)
        elif len(question.all_answers) >= 2:
            self.quiz_answer_radiobutton1.configure(text=answers[0].title(), value=answers[0], state=NORMAL)
            self.quiz_answer_radiobutton2.configure(text=answers[1].title(), value=answers[1], state=NORMAL)
            self.quiz_answer_radiobutton1.grid(column=0, row=1, sticky='sew', ipadx=10, ipady=10, padx=(20, 5), pady=5)
            self.quiz_answer_radiobutton2.grid(column=1, row=1, sticky='sew', ipadx=10, ipady=10, padx=(5, 20), pady=5)
            if len(question.all_answers) == 3:
                self.quiz_answer_radiobutton3.configure(text=answers[2].title(), value=answers[2], state=NORMAL)
                self.quiz_answer_radiobutton3.grid(column=0, row=2, columnspan=2, sticky='new', ipadx=10, ipady=10, padx=20, pady=5)
            elif len(question.all_answers) == 4:
                self.quiz_answer_radiobutton3.configure(text=answers[2].title(), value=answers[2], state=NORMAL)
                self.quiz_answer_radiobutton4.configure(text=answers[3].title(), value=answers[3], state=NORMAL)
                self.quiz_answer_radiobutton3.grid(column=0, row=2, sticky='new', ipadx=10, ipady=10, padx=(20, 5), pady=5)
                self.quiz_answer_radiobutton4.grid(column=1, row=2, sticky='new', ipadx=10, ipady=10, padx=(5, 20), pady=5)

    def begin_question(self, subject):
        """Trigger when 'questions_pick_button1' 2, 3, 4 buttons are pressed, 
        choose a random question and swap from 'question_pick_frame' to 'quiz_frame' and reset all the labels on 'quiz_frame' ready for the question."""
        self.gui_style.configure('quiz_correct_incorrect_label.TLabel', background=self.background_colours[0])
        self.quiz_correct_incorrect_label.grid_forget()
        self.question_pick_frame.grid_forget()
        self.quiz_check_answer_button.configure(state=NORMAL)
        self.quiz_next_button.configure(state=DISABLED)
        self.currect_question = self.all_quiz_questions[subject].pop(randrange(len(self.all_quiz_questions[subject])))
        self.quiz_entry_button_setup(self.currect_question)
        self.quiz_frame.grid(column=0, row=0, sticky='nsew')   

    def choose_question(self):
        """Trigger before each quiz question, if there are no questions left go to end screen, 
        if there is only one question subject to pick, run 'begin_question' else set up buttons
        to choose which subject of question to be asked next."""
        self.quiz_frame.grid_forget()
        if self.questions_left == 0:
            self.gui_style.configure('end_title_label.TLabel', background=self.background_colours[0])
            self.gui_style.configure('end_stats_label.TLabel', background=self.background_colours[0])
            score = round(100-self.end_stats_incorrect_questions_counter_variable/(self.QUESTIONS_PER_TOPIC//3)*100, 2)
            self.end_stats_display_label.configure(text=f"""  {self.QUESTIONS_PER_TOPIC//3}\n\n  {self.end_stats_correct_questions_counter_variable}\n\n  {self.end_stats_incorrect_questions_counter_variable}\n\n{score}%""")
            self.end_frame.grid(column=0, row=0, sticky='nsew')
        else:
            if len(self.all_quiz_questions.keys()) >= 4:
                subjects = sample(list(self.all_quiz_questions.keys()), 4)
                self.questions_pick_button3.configure(text=subjects[2].title(), command=lambda: self.begin_question(subjects[2]), state=NORMAL)
                self.questions_pick_button4.configure(text=subjects[3].title(), command=lambda: self.begin_question(subjects[3]), state=NORMAL)
                self.questions_pick_button3.grid(column=0, row=2, ipadx=10, ipady=50, sticky='new', padx=(20, 5), pady=5)
                self.questions_pick_button4.grid(column=1, row=2, ipadx=10, ipady=50, sticky='new', padx=(5, 20), pady=5)
            else:
                subjects = list(self.all_quiz_questions.keys())
            if len(self.all_quiz_questions.keys()) == 1:
                self.begin_question(subjects[0])
            elif len(self.all_quiz_questions.keys()) >= 2:
                self.questions_pick_button1.configure(text=subjects[0].title(), command=lambda: self.begin_question(subjects[0]), state=NORMAL)
                self.questions_pick_button2.configure(text=subjects[1].title(), command=lambda: self.begin_question(subjects[1]), state=NORMAL)
                self.questions_pick_button1.grid(column=0, row=1, ipadx=10, ipady=50, sticky='sew', padx=(20, 5), pady=5)
                self.questions_pick_button2.grid(column=1, row=1, ipadx=10, ipady=50, sticky='sew', padx=(5, 20), pady=5)
            if len(self.all_quiz_questions.keys()) == 3:
                self.questions_pick_button3.configure(text=subjects[2].title(), command=lambda: self.begin_question(subjects[2]), state=NORMAL)
                self.questions_pick_button3.grid(column=0, row=2, columnspan=2, ipadx=10, ipady=50, sticky='new', padx=(20, 20), pady=5)
            self.question_pick_frame.grid(column=0, row=0, sticky=NSEW)
            self.questions_left -= 1

    def start_quiz(self):
        """Trigger when pressing the start button on the option menu, 
        check if options have been selected and if so run 'choose_question() function.'"""
        self.subjects_selected_list = []
        self.all_quiz_questions = {}
        for button in self.options_menu_subject_check_button_list:
            if str(button.var.get()) != '':
                self.subjects_selected_list.append(button.var.get()) # A list of all selected subjects.
        if len(self.subjects_selected_list) == 0:
            messagebox.showwarning('Invalid Input', 'Please select one or more subjects')
            self.options_menu_subject_check_button_list[0].focus()
        elif self.options_menu_difficulty_variable.get() == -1:
            messagebox.showwarning('Invalid Input', 'Please select difficulty')
            self.options_menu_easy_radio_button.focus()
        else:
            for subject in self.subjects_selected_list:
                startvar = int(self.options_menu_difficulty_variable.get()*self.QUESTIONS_PER_TOPIC/3) # gets the first value in the subject list of questions to pull from
                endvar = int(self.options_menu_difficulty_variable.get()*self.QUESTIONS_PER_TOPIC/3+self.QUESTIONS_PER_TOPIC/3) # gets the last ^^^
                self.all_quiz_questions[self.genre[subject].name] = self.genre[subject].questions[startvar:endvar] 
            self.options_menu_frame.grid_forget()
            self.choose_question()

    def check_answer(self):
        """Triggers when 'quiz_check_answer_button' is pressed. If answer is invalid (eg. letters or symbols to answer a maths question) 
        show a messagebox warning and change nothing. Otherwise check if answer matches the correct answer, update 'the quiz_correct_incorrect_label'
        and change the states of all the buttons to the opposite (all disabled except 'quiz_next_button')"""
        if self.currect_question.incorrect_answer1 == '': # A single answer question will always be a maths question
            try:
                self.quiz_answer_variable.set(int(self.quiz_answer_variable.get()))
            except:
                try:
                    float(self.quiz_answer_variable.get())
                    messagebox.showwarning('Invalid Input', 'Please enter a whole number')
                except:
                    messagebox.showwarning('Invalid Input', 'Please enter a number')
                self.quiz_answer_entry.delete(0, END)
                self.quiz_answer_entry.focus()
                return
        elif not self.quiz_answer_variable.get() in self.currect_question.all_answers:
            messagebox.showwarning('Invalid Input', 'Please select an answer')
            return
        if self.quiz_answer_variable.get() == str(self.currect_question.correct_answer):
            self.gui_style.configure('quiz_correct_incorrect_label.TLabel', background="#70f456")
            self.quiz_correct_incorrect_label.configure(text='Correct!')
            self.end_stats_correct_questions_counter_variable += 1
        else:
            self.gui_style.configure('quiz_correct_incorrect_label.TLabel', background="#f45656")
            self.quiz_correct_incorrect_label.configure(text=f'Inncorrect! The Correct Answer Is {self.currect_question.correct_answer.title()}')
            self.end_stats_incorrect_questions_counter_variable += 1
        self.quiz_correct_incorrect_label.grid(column=0, row=3, columnspan=2, ipady=10, ipadx=10, pady=5, padx=130, sticky='new')
        self.quiz_check_answer_button.configure(state=DISABLED)
        self.quiz_answer_entry.configure(state=DISABLED)
        self.quiz_answer_radiobutton1.configure(state=DISABLED)
        self.quiz_answer_radiobutton2.configure(state=DISABLED)
        self.quiz_answer_radiobutton3.configure(state=DISABLED)
        self.quiz_answer_radiobutton4.configure(state=DISABLED)
        self.quiz_next_button.configure(state=NORMAL)

    def return_home(self):
        """Trigers when end_return_to_start_button is pressed. grid_forget() all active frames and run 'create_ui()' function"""
        self.end_frame.grid_forget()
        self.question_pick_frame.grid_forget()
        self.create_ui()


if __name__ == "__main__":
    root = Tk()
    window = GUI(root)
    root.geometry('800x516')
    root.resizable(False, False) # Makes window non resizable.
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root.mainloop()