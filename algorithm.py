# Algorithm - Solve questions

import warnings
from data_structures import *
from classes import Library

from classes import Question, Solution

def solve(question: Question) -> Solution:

    # Sort the libraries by their score
    libraries = question.libraries

    libraries.sort()
    totalDays = 0

    # signup all the libraries
    for library in libraries:

        totalDays += library.signup_time

    return Solution(file_name=question.file_name)

def solveAll(questions: [Question]) -> [Solution]:
    solutions = []
    
    for question in questions:
        solutions.append(solve(question))
    
    return solutions