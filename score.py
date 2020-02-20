# Score - Calculates Score

from utils.constants import SOLUTION_FORMAT
from classes import Score, Solution
from glob import glob
import warnings

def getScore(solution: Solution) -> Score:
    warnings.warn("TODO GET SCORE")

    books_seen = set()
    for lib, books in solution.library_books:
        

    return Score(0, solution)

def getScores(solutions: [Solution]) -> [Score]:
    scores = []

    for solution in solutions:
        scores.append(getScore(solution))

    return scores