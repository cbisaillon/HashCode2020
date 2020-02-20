from datetime import datetime

# File Settings

SOLUTION_FOLDER = "./solution/"
QUESTION_FOLDER = "./question/"
SOLUTION_ZIP = SOLUTION_FOLDER + 'solution.zip'
SOLUTION_FORMAT = SOLUTION_FOLDER + '*.sol'
PACK_EXCLUDE = []

# Time Manger

STARTING_TIME = datetime.strptime('2019-02-19 12:30:00', '%Y-%m-%d %H:%M:%S')
END_TIME = datetime.strptime('2019-02-19 16:30:00', '%Y-%m-%d %H:%M:%S')

# (Length of Event, Event Name)
SCHEDULE = [
    (15, 'Reveal Stream'),
    (15, 'Read Documentation'),
    (15, 'Study question'),
    (30, 'Solution (25%)'), 
    (5, 'Submit Solution (25%)'), 
    (45, 'Solution (50%)'), 
    (5, 'Submit Solution (50%)'), 
    (45, 'Solution (75%)'),
    (5, 'Submit Solution(75%)'),
    (55, 'Solution (100%)'),
    (5, 'Submit Solution (100%)')
]