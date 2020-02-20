# Score - Calculates Score

from utils.constants import SOLUTION_FORMAT
from classes import Score, Solution, Library
from glob import glob
import warnings

def getScore(solution: Solution) -> Score:
    books_seen = set()
    score = 0

    for _, books in solution.library_books:
        for book in books:
            if not book in books_seen:
                score += book.score
                books_seen.add(book)

    return Score(score, solution)

def getScores(solutions: [Solution]) -> [Score]:
    scores = []

    for solution in solutions:
        scores.append(getScore(solution))

    return scores

def getTotalScore(scores: [Score]) -> [int]:
    total = 0

    for score in scores:
        total += score.val
    
    return total