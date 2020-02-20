# Classes - Structures used in Competition

import warnings

class Book:
    def __init__(self, id: int, score: int):
        self.id = id
        self.score = score

    def __str__(self):
        return "Book %d Score %d" % (self.id, self.score)

class Library:
    def __init__(self, id: int, book_per_day: int, signup_time: int,  books: [Book]):
        self.id = id
        self.books_per_day = book_per_day
        self.signup_time = signup_time
        self.books = books

    def __str__(self):
        return "Library -> Id: %d, Per Day: %d, Singup: %d, Books %s" % (self.id, self.books_per_day, self.signup_time, [str(x) for x in self.books])

class Question:
    def __init__(self, file_name: str = '', days_to_scan: int = 0, book_scores: [int] = [], libraries =[]):
        self.file_name = file_name
        self.days_to_scan = days_to_scan
        self.books = [Book(id=i, score=x) for i, x in enumerate(book_scores)]
        self.libraries = [Library(id=k, book_per_day=books_per_day, signup_time=signup_time, books=[self.books[i] for i in book_ids]) for (k, (books_per_day, signup_time, book_ids)) in enumerate(libraries)]

    def __str__(self):
        return "Question (%s) -> Day to Scan: %d, Books: %s, Libraries: %s" % (self.file_name, self.days_to_scan, [str(x) for x in self.books], [str(x) for x in self.libraries])

class Solution:
    def __init__(self, file_name: str):
        self.file_name = file_name
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
        self.usesQuestionSample = False
        self.usesSolutionSample = False

    def __str__(self):
        return "Arguments has files %s, popup %s, question sample %s, solution sample %s." % (self.files, self.hasPopup, self.usesQuestionSample, self.usesSolutionSample)