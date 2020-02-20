# Algorithm - Solve questions

import warnings
from data_structures import *

from classes import Question, Solution

def solve(question: Question) -> Solution:
    warnings.warn("TODO SOLVE QUESTION %s" % question)
    return Solution(question=question)

def solveAll(questions: [Question]) -> [Solution]:
    solutions = []
    
    for question in questions:
        solutions.append(solve(question))
    
    return solutions