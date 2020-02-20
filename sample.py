# Samples for Testing (Feel free to modify and not revert)

from classes import Question, Solution, Library, Book

def loadQuestionSamples() -> [Question]:
    return [Question('sample_question', days_to_scan=10, book_scores=[1,2,3,4], libraries=[(1, 9, [1, 0, 3]), (1, 2, [0,2,3])])] #(books_per_day, signup_time, book_ids)

def loadSolutionSamples() -> [Solution]:
    return [Solution('sample_solution', libraries=[Library(id=0, book_per_day=1, signup_time=1, books=[1, 2])], books_from_libary=[[Book(1, 10)]])]