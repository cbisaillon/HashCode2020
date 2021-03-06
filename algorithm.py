# Algorithm - Solve questions

import warnings
from data_structures import *
from classes import Library

import scipy

from classes import Question, Solution

def solve(question: Question, parameters) -> Solution:

    # Sort the libraries by their score
    libraries = question.libraries

    libraries = sorted(libraries, key=lambda x: x.getScore(parameters))
    totalDays = 0

    librariesOut = []
    booksOut = []

    # signup all the libraries
    for index, library in enumerate(libraries):
        totalDaysShip = library.signup_time + totalDays
        librariesOut.append(library)
        booksOut.append([])
        for book in library.books:
            totalDaysShip += 1 / library.books_per_day
            booksOut[index].append(book)

            if totalDaysShip > question.days_to_scan:
                break

        totalDays += library.signup_time
        if(totalDays > question.days_to_scan):
            break

    return Solution(file_name=question.file_name, libraries=librariesOut, books_from_libary=booksOut)

def solveAll(questions: [Question], parameters) -> [Solution]:
    solutions = []

    print(parameters)
    
    for question in questions:
        solutions.append(solve(question, parameters))
    
    return solutions