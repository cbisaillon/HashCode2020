# Classes - Structures used in Competition

import warnings

class Question:
    def __init__(self, file_name: str):
        self.file_name = file_name
        warnings.warn("TODO QUESTION CLASS")

    def __str__(self):
        return "Question: %s" % (self.file_name)

class Solution:
    def __init__(self, question: Question):
        self.file_name = question.file_name
        warnings.warn("TODO SOLUTION CLASS")
    
    def __str__(self):
        return "Solution: %s" % (self.file_name)

class Score:
    def __init__(self, val: float, solution: Solution):
        self.val = val
        self.file_name = solution.file_name
        warnings.warn("TODO SCORE CLASS")
    
    def __str__(self):
        return "Score for %s is %f." % (self.file_name, self.val)

class Arguments:
    def __init__(self):
        self.files = []
        self.hasPopup = False

    def __str__(self):
        return "Arguments has files %s, popup %s." % (self.files, self.hasPopup)