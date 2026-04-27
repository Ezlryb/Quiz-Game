class Question:
    def __init__(self, question, correct_answer, incorrect_answer1 = '', incorrect_answer2 = '', incorrect_answer3 = ''):
        self.question = question # eg. 1 + 1 = | Who is the capital of Middle Earth? | What getes wetter as it dries?
        self.correct_answer = correct_answer # eg. 2 | marvin the martian | a towel
        self.incorrect_answer1 = incorrect_answer1 # eg. 3 | donald duck | a candle
        self.incorrect_answer2 = incorrect_answer2 # eg. 1 | me | the human soul
        self.incorrect_answer3 = incorrect_answer3 # eg. 90 | turn it to eleven | quicksand
        self.number_of_answers = 0
        self.count_answers()
    
    def count_answers(self):
        if self.correct_answer != '':
            self.number_of_answers += 1
        if self.incorrect_answer1 != '':
            self.number_of_answers += 1
        if self.incorrect_answer2 != '':
            self.number_of_answers += 1
        if self.incorrect_answer3 != '':
            self.number_of_answers += 1


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
trivia = {
    'history': [
        {'question': 'Who was the first President of the United States?', 'correct_answer': 'George Washington', 'incorrect_answer1': 'Thomas Jefferson'},
        {'question': 'In which year did World War II end?', 'correct_answer': 1945, 'incorrect_answer1': 1944, 'incorrect_answer2': 1946, 'incorrect_answer3': 1950},
        {'question': 'The Magna Carta was signed in which century?', 'correct_answer': '13th', 'incorrect_answer1': '11th', 'incorrect_answer2': '15th'},
        {'question': 'Who was the "Sun King" of France?', 'correct_answer': 'Louis XIV', 'incorrect_answer1': 'Louis XVI'},
        {'question': 'Which empire was ruled by Mansa Musa?', 'correct_answer': 'Mali Empire', 'incorrect_answer1': 'Songhai Empire', 'incorrect_answer2': 'Ottoman Empire', 'incorrect_answer3': 'Roman Empire'},
        {'question': 'The Peloponnesian War was fought between Athens and which other city-state?', 'correct_answer': 'Sparta', 'incorrect_answer1': 'Thebes', 'incorrect_answer2': 'Corinth'},
        {'question': 'In what year was the Berlin Wall pulled down?', 'correct_answer': 1989, 'incorrect_answer1': 1991},
        {'question': 'Who was the first female Prime Minister of the UK?', 'correct_answer': 'Margaret Thatcher', 'incorrect_answer1': 'Theresa May', 'incorrect_answer2': 'Angela Merkel', 'incorrect_answer3': 'Indira Gandhi'},
        {'question': 'The Meiji Restoration occurred in which country?', 'correct_answer': 'Japan', 'incorrect_answer1': 'China', 'incorrect_answer2': 'Korea'},
        {'question': 'Which Roman Emperor legalised Christianity?', 'correct_answer': 'Constantine the Great', 'incorrect_answer1': 'Nero'},
        {'question': 'The Battle of Hastings took place in which year?', 'correct_answer': 1066, 'incorrect_answer1': 1055, 'incorrect_answer2': 1077, 'incorrect_answer3': 1215},
        {'question': 'Who was the primary author of the Declaration of Independence?', 'correct_answer': 'Thomas Jefferson', 'incorrect_answer1': 'Benjamin Franklin', 'incorrect_answer2': 'Alexander Hamilton'},
        {'question': 'Which dynasty built the majority of the Great Wall of China?', 'correct_answer': 'Ming', 'incorrect_answer1': 'Qin'},
        {'question': 'In what year did the French Revolution begin?', 'correct_answer': 1789, 'incorrect_answer1': 1799, 'incorrect_answer2': 1776, 'incorrect_answer3': 1804},
        {'question': 'Who was the last Tsar of Russia?', 'correct_answer': 'Nicholas II', 'incorrect_answer1': 'Alexander III', 'incorrect_answer2': 'Peter the Great'},
        {'question': 'The "Code of Hammurabi" originated in which ancient civilisation?', 'correct_answer': 'Babylon', 'incorrect_answer1': 'Sumer'},
        {'question': 'What was the name of the ship that brought the Pilgrims to America in 1620?', 'correct_answer': 'Mayflower', 'incorrect_answer1': 'Beagle', 'incorrect_answer2': 'Endeavour', 'incorrect_answer3': 'Santa Maria'},
        {'question': 'Which 19th-century conflict resulted in the most American casualties?', 'correct_answer': 'The Civil War', 'incorrect_answer1': 'War of 1812', 'incorrect_answer2': 'Mexican-American War'},
        {'question': 'The Punic Wars were fought between Rome and which North African city?', 'correct_answer': 'Carthage', 'incorrect_answer1': 'Alexandria'},
        {'question': 'What treaty ended the Thirty Years\' War in 1648?', 'correct_answer': 'Peace of Westphalia', 'incorrect_answer1': 'Treaty of Versailles', 'incorrect_answer2': 'Treaty of Utrecht', 'incorrect_answer3': 'Treaty of Tordesillas'}
    ],
    'mythology': [
        {'question': 'Who is the Greek god of the sea?', 'correct_answer': 'Poseidon', 'incorrect_answer1': 'Zeus'},
        {'question': 'In Norse mythology, what is the name of Thor\'s hammer?', 'correct_answer': 'Mjölnir', 'incorrect_answer1': 'Gungnir', 'incorrect_answer2': 'Stormbreaker', 'incorrect_answer3': 'Aegis'},
        {'question': 'Who flew too close to the sun with wings made of wax?', 'correct_answer': 'Icarus', 'incorrect_answer1': 'Daedalus', 'incorrect_answer2': 'Perseus'},
        {'question': 'Who is the Roman equivalent of the Greek goddess Aphrodite?', 'correct_answer': 'Venus', 'incorrect_answer1': 'Juno'},
        {'question': 'Which hero pulled the sword Excalibur from a stone?', 'correct_answer': 'King Arthur', 'incorrect_answer1': 'Lancelot', 'incorrect_answer2': 'Galahad', 'incorrect_answer3': 'Merlin'},
        {'question': 'The Sphinx sat outside which ancient Greek city?', 'correct_answer': 'Thebes', 'incorrect_answer1': 'Athens', 'incorrect_answer2': 'Sparta'},
        {'question': 'In Egyptian mythology, who is the god of the afterlife?', 'correct_answer': 'Anubis', 'incorrect_answer1': 'Ra'},
        {'question': 'Which Greek hero performed 12 labours?', 'correct_answer': 'Heracles', 'incorrect_answer1': 'Achilles', 'incorrect_answer2': 'Odysseus', 'incorrect_answer3': 'Jason'},
        {'question': 'What is the name of the three-headed dog that guards the underworld?', 'correct_answer': 'Cerberus', 'incorrect_answer1': 'Hydra', 'incorrect_answer2': 'Chimera'},
        {'question': 'Who is the Norse god of mischief?', 'correct_answer': 'Loki', 'incorrect_answer1': 'Odin'},
        {'question': 'Which goddess sprang fully formed from Zeus\'s forehead?', 'correct_answer': 'Athena', 'incorrect_answer1': 'Artemis', 'incorrect_answer2': 'Hera', 'incorrect_answer3': 'Demeter'},
        {'question': 'In Japanese mythology, Amaterasu is the goddess of what?', 'correct_answer': 'The Sun', 'incorrect_answer1': 'The Moon', 'incorrect_answer2': 'The Storms'},
        {'question': 'What is the name of the Greek personification of the earth?', 'correct_answer': 'Gaia', 'incorrect_answer1': 'Rhea'},
        {'question': 'Who killed the Minotaur in the Labyrinth?', 'correct_answer': 'Theseus', 'incorrect_answer1': 'Jason', 'incorrect_answer2': 'Bellerophon', 'incorrect_answer3': 'Perseus'},
        {'question': 'What animal did the Egyptian god Set represent?', 'correct_answer': 'A Sha (Set Animal)', 'incorrect_answer1': 'A Falcon', 'incorrect_answer2': 'A Jackal'},
        {'question': 'In Norse myth, what is the name of the bridge connecting Midgard and Asgard?', 'correct_answer': 'Bifrost', 'incorrect_answer1': 'Yggdrasil'},
        {'question': 'Which Titan was forced to hold up the celestial heavens for eternity?', 'correct_answer': 'Atlas', 'incorrect_answer1': 'Prometheus', 'incorrect_answer2': 'Cronus', 'incorrect_answer3': 'Oceanus'},
        {'question': 'Who was the Aztec god of wind and learning, often depicted as a feathered serpent?', 'correct_answer': 'Quetzalcoatl', 'incorrect_answer1': 'Huitzilopochtli', 'incorrect_answer2': 'Tezcatlipoca'},
        {'question': 'In Hindu mythology, who is the god of preservation?', 'correct_answer': 'Vishnu', 'incorrect_answer1': 'Shiva'},
        {'question': 'Which Sumerian epic features a hero seeking immortality after the death of Enkidu?', 'correct_answer': 'Epic of Gilgamesh', 'incorrect_answer1': 'The Enuma Elish', 'incorrect_answer2': 'The Descent of Inanna', 'incorrect_answer3': 'Atrahasis'}
    ],
    'internet': [
        {'question': 'What does "WWW" stand for?', 'correct_answer': 'World Wide Web', 'incorrect_answer1': 'Web World Wide'},
        {'question': 'Which social media platform is known for its 280-character limit?', 'correct_answer': 'Twitter/X', 'incorrect_answer1': 'Facebook', 'incorrect_answer2': 'Instagram', 'incorrect_answer3': 'Reddit'},
        {'question': 'In what year was the first YouTube video uploaded?', 'correct_answer': 2005, 'incorrect_answer1': 2003, 'incorrect_answer2': 2007},
        {'question': 'What is the most popular search engine in the world?', 'correct_answer': 'Google', 'incorrect_answer1': 'Bing'},
        {'question': 'Which company developed the Chrome browser?', 'correct_answer': 'Google', 'incorrect_answer1': 'Apple', 'incorrect_answer2': 'Microsoft', 'incorrect_answer3': 'Mozilla'},
        {'question': 'What does "HTTP" stand for?', 'correct_answer': 'Hypertext Transfer Protocol', 'incorrect_answer1': 'Hyperlink Text Transfer Plot', 'incorrect_answer2': 'High Tech Transfer Protocol'},
        {'question': 'Who is considered the primary creator of the World Wide Web?', 'correct_answer': 'Tim Berners-Lee', 'incorrect_answer1': 'Bill Gates'},
        {'question': 'What was the first social media site to reach 1 million monthly active users?', 'correct_answer': 'MySpace', 'incorrect_answer1': 'Facebook', 'incorrect_answer2': 'Friendster', 'incorrect_answer3': 'SixDegrees'},
        {'question': 'In internet slang, what does "AFK" mean?', 'correct_answer': 'Away From Keyboard', 'incorrect_answer1': 'Always For Keeps', 'incorrect_answer2': 'All For Knowledge'},
        {'question': 'What was the name of the first graphical web browser?', 'correct_answer': 'Mosaic', 'incorrect_answer1': 'Netscape'},
        {'question': 'Which cryptocurrency was created first?', 'correct_answer': 'Bitcoin', 'incorrect_answer1': 'Ethereum', 'incorrect_answer2': 'Litecoin', 'incorrect_answer3': 'Dogecoin'},
        {'question': 'What is the maximum file size for a standard email attachment in Gmail?', 'correct_answer': '25MB', 'incorrect_answer1': '10MB', 'incorrect_answer2': '50MB'},
        {'question': 'What is the term for a "distributed ledger" technology?', 'correct_answer': 'Blockchain', 'incorrect_answer1': 'Cloud Computing'},
        {'question': 'Which programming language is often called the "language of the web"?', 'correct_answer': 'JavaScript', 'incorrect_answer1': 'Python', 'incorrect_answer2': 'C++', 'incorrect_answer3': 'PHP'},
        {'question': 'What was Google\'s original name?', 'correct_answer': 'BackRub', 'incorrect_answer1': 'SearchMaster', 'incorrect_answer2': 'PageRank'},
        {'question': 'In which year did the "Dot-com bubble" burst?', 'correct_answer': 2000, 'incorrect_answer1': 1998},
        {'question': 'Which protocol is used to securely browse the web?', 'correct_answer': 'HTTPS', 'incorrect_answer1': 'FTP', 'incorrect_answer2': 'SMTP', 'incorrect_answer3': 'SSH'},
        {'question': 'The first ever email was sent between two computers in which year?', 'correct_answer': 1971, 'incorrect_answer1': 1981, 'incorrect_answer2': 1965},
        {'question': 'What does "URL" stand for?', 'correct_answer': 'Uniform Resource Locator', 'incorrect_answer1': 'Universal Reset Link'},
        {'question': 'Who co-founded Reddit alongside Steve Huffman?', 'correct_answer': 'Alexis Ohanian', 'incorrect_answer1': 'Mark Zuckerberg', 'incorrect_answer2': 'Jack Dorsey', 'incorrect_answer3': 'Jimmy Wales'}
    ],
    'geography': [
        {'question': 'What is the largest country in the world by land area?', 'correct_answer': 'Russia', 'incorrect_answer1': 'Canada'},
        {'question': 'Which ocean is the largest?', 'correct_answer': 'Pacific', 'incorrect_answer1': 'Atlantic', 'incorrect_answer2': 'Indian', 'incorrect_answer3': 'Arctic'},
        {'question': 'What is the capital of France?', 'correct_answer': 'Paris', 'incorrect_answer1': 'Lyon', 'incorrect_answer2': 'Marseille'},
        {'question': 'Which continent is the Sahara Desert located on?', 'correct_answer': 'Africa', 'incorrect_answer1': 'Asia'},
        {'question': 'Mount Everest is part of which mountain range?', 'correct_answer': 'Himalayas', 'incorrect_answer1': 'Andes', 'incorrect_answer2': 'Alps', 'incorrect_answer3': 'Rockies'},
        {'question': 'What is the longest river in the world?', 'correct_answer': 'Nile', 'incorrect_answer1': 'Amazon', 'incorrect_answer2': 'Yangtze'},
        {'question': 'Which country has the most natural lakes?', 'correct_answer': 'Canada', 'incorrect_answer1': 'USA'},
        {'question': 'What is the smallest country in the world?', 'correct_answer': 'Vatican City', 'incorrect_answer1': 'Monaco', 'incorrect_answer2': 'San Marino', 'incorrect_answer3': 'Liechtenstein'},
        {'question': 'Which city is located on two continents?', 'correct_answer': 'Istanbul', 'incorrect_answer1': 'Cairo', 'incorrect_answer2': 'Moscow'},
        {'question': 'What is the capital of Australia?', 'correct_answer': 'Canberra', 'incorrect_answer1': 'Sydney'},
        {'question': 'Which country is also known as the "Land of the Rising Sun"?', 'correct_answer': 'Japan', 'incorrect_answer1': 'South Korea', 'incorrect_answer2': 'Thailand', 'incorrect_answer3': 'Vietnam'},
        {'question': 'The Great Barrier Reef is off the coast of which country?', 'correct_answer': 'Australia', 'incorrect_answer1': 'Indonesia', 'incorrect_answer2': 'Philippines'},
        {'question': 'What is the deepest point in the world\'s oceans?', 'correct_answer': 'Mariana Trench', 'incorrect_answer1': 'Java Trench'},
        {'question': 'Which desert is the driest place on Earth?', 'correct_answer': 'Atacama', 'incorrect_answer1': 'Gobi', 'incorrect_answer2': 'Sahara', 'incorrect_answer3': 'Kalahari'},
        {'question': 'What is the capital of Iceland?', 'correct_answer': 'Reykjavik', 'incorrect_answer1': 'Oslo', 'incorrect_answer2': 'Helsinki'},
        {'question': 'How many countries does the equator pass through?', 'correct_answer': 13, 'incorrect_answer1': 10},
        {'question': 'What is the only sea without any coasts?', 'correct_answer': 'Sargasso Sea', 'incorrect_answer1': 'Dead Sea', 'incorrect_answer2': 'Caspian Sea', 'incorrect_answer3': 'Red Sea'},
        {'question': 'Which country has the longest coastline in the world?', 'correct_answer': 'Canada', 'incorrect_answer1': 'Norway', 'incorrect_answer2': 'Russia'},
        {'question': 'In which country would you find the city of Timbuktu?', 'correct_answer': 'Mali', 'incorrect_answer1': 'Niger'},
        {'question': 'What is the name of the world\'s largest island?', 'correct_answer': 'Greenland', 'incorrect_answer1': 'New Guinea', 'incorrect_answer2': 'Borneo', 'incorrect_answer3': 'Madagascar'}
    ]
}
puzzles = {
        'riddles': [
            {'question': 'I speak without a mouth... What am I?', 'correct_answer': 'An echo', 'incorrect_answer1': 'A whistle'},
            {'question': 'The more of this there is, the less you see. What is it?', 'correct_answer': 'Darkness', 'incorrect_answer1': 'Fog', 'incorrect_answer2': 'Light', 'incorrect_answer3': 'Smoke'},
            {'question': 'What has keys but can\'t open locks?', 'correct_answer': 'A piano', 'incorrect_answer1': 'A map', 'incorrect_answer2': 'A computer'},
            {'question': 'What has to be broken before you can use it?', 'correct_answer': 'An egg', 'incorrect_answer1': 'A promise'},
            {'question': 'What gets wet while drying?', 'correct_answer': 'A towel', 'incorrect_answer1': 'Rain', 'incorrect_answer2': 'A sponge', 'incorrect_answer3': 'A road'},
            {'question': 'What has one eye but can’t see?', 'correct_answer': 'A needle', 'incorrect_answer1': 'A hurricane', 'incorrect_answer2': 'A potato'},
            {'question': 'What belongs to you, but others use it more?', 'correct_answer': 'Your name', 'incorrect_answer1': 'Your phone'},
            {'question': 'I have cities, but no houses... What am I?', 'correct_answer': 'A map', 'incorrect_answer1': 'A globe', 'incorrect_answer2': 'A dream', 'incorrect_answer3': 'A photo'},
            {'question': 'What is so fragile that saying its name breaks it?', 'correct_answer': 'Silence', 'incorrect_answer1': 'Glass', 'incorrect_answer2': 'A secret'},
            {'question': 'What can travel around the world while staying in a corner?', 'correct_answer': 'A stamp', 'incorrect_answer1': 'A spider'},
            {'question': 'I am tall when young, short when old. What am I?', 'correct_answer': 'A candle', 'incorrect_answer1': 'A person', 'incorrect_answer2': 'A tree', 'incorrect_answer3': 'A pencil'},
            {'question': 'What has hands, but can’t clap?', 'correct_answer': 'A clock', 'incorrect_answer1': 'A statue', 'incorrect_answer2': 'A baby'},
            {'question': 'What can you catch, but not throw?', 'correct_answer': 'A cold', 'incorrect_answer1': 'A ball'},
            {'question': 'Who makes it sells it, who buys it never uses it... What is it?', 'correct_answer': 'A coffin', 'incorrect_answer1': 'Insurance', 'incorrect_answer2': 'A wig', 'incorrect_answer3': 'A gift'},
            {'question': 'What has a neck but no head?', 'correct_answer': 'A bottle', 'incorrect_answer1': 'A shirt', 'incorrect_answer2': 'A guitar'},
            {'question': 'Give me a smile and I’ll always smile back. What am I?', 'correct_answer': 'A mirror', 'incorrect_answer1': 'An egg'},
            {'question': 'I have branches, but no fruit or leaves. What am I?', 'correct_answer': 'A bank', 'incorrect_answer1': 'A library', 'incorrect_answer2': 'A road', 'incorrect_answer3': 'A river'},
            {'question': 'What can you break, even if you never touch it?', 'correct_answer': 'A promise', 'incorrect_answer1': 'Silence', 'incorrect_answer2': 'The law'},
            {'question': 'What comes once in a minute, twice in a moment...?', 'correct_answer': 'The letter M', 'incorrect_answer1': 'A heartbeat'},
            {'question': 'How did the dog cross the river without getting wet?', 'correct_answer': 'The river was frozen', 'incorrect_answer1': 'The dog can fly', 'incorrect_answer2': 'It was a toy dog', 'incorrect_answer3': 'He swam underwater'}
        ],
        'anagrams': [
            {'question': 'Anagram of "Listen":', 'correct_answer': 'Silent', 'incorrect_answer1': 'Inlets'},
            {'question': 'Anagram of "Dormitory":', 'correct_answer': 'Dirty Room', 'incorrect_answer1': 'Roomy Dirt', 'incorrect_answer2': 'Tory Dorm', 'incorrect_answer3': 'Mirror Dot'},
            {'question': 'Anagram of "The Eyes":', 'correct_answer': 'They See', 'incorrect_answer1': 'Eye Thes', 'incorrect_answer2': 'Thee Yes'},
            {'question': 'Anagram of "Schoolmaster":', 'correct_answer': 'The Classroom', 'incorrect_answer1': 'Master Schools'},
            {'question': 'Anagram of "Astronomy":', 'correct_answer': 'Moon starer', 'incorrect_answer1': 'Star money', 'incorrect_answer2': 'No my stars', 'incorrect_answer3': 'Starry Moon'},
            {'question': 'Anagram of "Debit card":', 'correct_answer': 'Bad credit', 'incorrect_answer1': 'Card bidet', 'incorrect_answer2': 'Diet brad'},
            {'question': 'Anagram of "Funeral":', 'correct_answer': 'Real fun', 'incorrect_answer1': 'Earful'},
            {'question': 'Anagram of "Election":', 'correct_answer': 'Licenteo', 'incorrect_answer1': 'Net lice', 'incorrect_answer2': 'Electron', 'incorrect_answer3': 'Lecture'},
            {'question': 'Anagram of "A gentleman":', 'correct_answer': 'Elegant man', 'incorrect_answer1': 'Gentle man a', 'incorrect_answer2': 'Mean tangle'},
            {'question': 'Anagram of "Eleven plus two":', 'correct_answer': 'Twelve plus one', 'incorrect_answer1': 'Two plus eleven'},
            {'question': 'Anagram of "The Morse Code":', 'correct_answer': 'Here come dots', 'incorrect_answer1': 'More codes the', 'incorrect_answer2': 'Dots come here', 'incorrect_answer3': 'Code the mores'},
            {'question': 'Anagram of "Snooze alarms":', 'correct_answer': 'Alas no more Zs', 'incorrect_answer1': 'No more snooze', 'incorrect_answer2': 'Alarm snoozes'},
            {'question': 'Anagram of "Clothespins":', 'correct_answer': 'So help scnt', 'incorrect_answer1': 'Pins clothes'},
            {'question': 'Anagram of "Vacation time":', 'correct_answer': 'I am not active', 'incorrect_answer1': 'Time vacation', 'incorrect_answer2': 'Active am I', 'incorrect_answer3': 'Oceanic vitamin'},
            {'question': 'Anagram of "The Public Art Galleries":', 'correct_answer': 'Large picture halls, I bet', 'incorrect_answer1': 'Gallery public', 'incorrect_answer2': 'Art halls large'},
            {'question': 'Anagram of "Conversation":', 'correct_answer': 'Voices rant on', 'incorrect_answer1': 'Conservation'},
            {'question': 'Anagram of "Meteorological":', 'correct_answer': 'Cool game to learn', 'incorrect_answer1': 'Logical meteor', 'incorrect_answer2': 'Room to leg logic', 'incorrect_answer3': 'Goo metal local'},
            {'question': 'Anagram of "Western Union":', 'correct_answer': 'Unite no answer', 'incorrect_answer1': 'Union western', 'incorrect_answer2': 'No answer unite'},
            {'question': 'Anagram of "Statue of Liberty":', 'correct_answer': 'Built stay of tree', 'incorrect_answer1': 'Liberty statue'},
            {'question': 'Anagram of "Semolina":', 'correct_answer': 'Is no meal', 'incorrect_answer1': 'Meal is no', 'incorrect_answer2': 'No meal is', 'incorrect_answer3': 'Lemon ais'}
        ],
        'fill in the blank': [
            {'question': 'Better late than _______.', 'correct_answer': 'Never', 'incorrect_answer1': 'Early'},
            {'question': 'A picture is worth a thousand _______.', 'correct_answer': 'Words', 'incorrect_answer1': 'Pixels', 'incorrect_answer2': 'Dollars', 'incorrect_answer3': 'Frames'},
            {'question': 'The early bird catches the _______.', 'correct_answer': 'Worm', 'incorrect_answer1': 'Seed', 'incorrect_answer2': 'Fly'},
            {'question': 'Actions speak louder than _______.', 'correct_answer': 'Words', 'incorrect_answer1': 'Shouts'},
            {'question': 'When in Rome, do as the _______ do.', 'correct_answer': 'Romans', 'incorrect_answer1': 'Tourists', 'incorrect_answer2': 'Gladiators', 'incorrect_answer3': 'Locals'},
            {'question': 'Easy come, easy _______.', 'correct_answer': 'Go', 'incorrect_answer1': 'Stay', 'incorrect_answer2': 'Leave'},
            {'question': 'Every cloud has a silver _______.', 'correct_answer': 'Lining', 'incorrect_answer1': 'Edge'},
            {'question': 'Practice makes _______.', 'correct_answer': 'Perfect', 'incorrect_answer1': 'Progress', 'incorrect_answer2': 'Better', 'incorrect_answer3': 'Harder'},
            {'question': 'Beauty is in the eye of the _______.', 'correct_answer': 'Beholder', 'incorrect_answer1': 'Artist', 'incorrect_answer2': 'Witness'},
            {'question': 'A penny saved is a penny _______.', 'correct_answer': 'Earned', 'incorrect_answer1': 'Spent'},
            {'question': 'Don\'t count your chickens before they _______.', 'correct_answer': 'Hatch', 'incorrect_answer1': 'Grow', 'incorrect_answer2': 'Run', 'incorrect_answer3': 'Lay'},
            {'question': 'The _______ is always greener on the other side.', 'correct_answer': 'Grass', 'incorrect_answer1': 'Garden', 'incorrect_answer2': 'Hill'},
            {'question': 'Knowledge is _______.', 'correct_answer': 'Power', 'incorrect_answer1': 'Key'},
            {'question': 'Laughter is the best _______.', 'correct_answer': 'Medicine', 'incorrect_answer1': 'Solution', 'incorrect_answer2': 'Feeling', 'incorrect_answer3': 'Gift'},
            {'question': 'Necessity is the mother of _______.', 'correct_answer': 'Invention', 'incorrect_answer1': 'Creation', 'incorrect_answer2': 'Innovation'},
            {'question': 'Curiosity killed the _______.', 'correct_answer': 'Cat', 'incorrect_answer1': 'Dog'},
            {'question': 'Rome wasn\'t built in a _______.', 'correct_answer': 'Day', 'incorrect_answer1': 'Year', 'incorrect_answer2': 'Week', 'incorrect_answer3': 'Month'},
            {'question': 'Fortune favors the _______.', 'correct_answer': 'Bold', 'incorrect_answer1': 'Rich', 'incorrect_answer2': 'Kind'},
            {'question': 'Absence makes the heart grow _______.', 'correct_answer': 'Fonder', 'incorrect_answer1': 'Colder'},
            {'question': 'Still waters run _______.', 'correct_answer': 'Deep', 'incorrect_answer1': 'Fast', 'incorrect_answer2': 'Cold', 'incorrect_answer3': 'Quietly'}
        ]
    }
maths_data = process_data(maths, 'maths')
trivia_data = process_data(trivia, 'trivia')
puzzle_data = process_data(puzzles, 'puzzles')