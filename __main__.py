# Main File (LIGHT MODIFICATIONS)

from utils.pack import packSolution
from parse import loadQuestions, saveSolutions, handleArgv
from classes import Question, Solution
from algorithm import solveAll
from score import getScores, getTotalScore
import os
from utils.constants import SOLUTION_FOLDER
from utils.secret import SUBMISSION_URL
import webbrowser
import subprocess
from sample import loadQuestionSamples, loadSolutionSamples
from datetime import datetime

from scipy import optimize

arguments = handleArgv()

def getQuestions() -> [Question]:
    start = datetime.now()

    print("Hash Code 2020")

    print("\nShell Args:")

    print(arguments)

    print("\nLoad Questions:")
    if arguments.usesQuestionSample:
        questions = loadQuestionSamples()
    else:
        questions = loadQuestions(arguments.files)

    if not arguments.silentMode:
        for question in questions:
            print(question)

questions = getQuestions()

def getOptimizeScore(x, *args) -> float:
    return -optimize(x)

def optimize(parameters) -> float:
    solutions = solveAll(questions, parameters)
    scores = getScores(solutions)

    return getTotalScore(scores)

def main(parameters) -> float:
    print("\nSolve Questions:")
    if arguments.usesSolutionSample:
        solutions = solveAll(loadSolutionSamples())
    else:
        solutions = solveAll(questions)

    if not arguments.silentMode:
        for solution in solutions:
            print(solution)

    print("\nEvaluate Solutions:")
    scores: [Score] = getScores(solutions)

    for score in scores:
        print(score)

    totalScore = getTotalScore(scores)

    print("Total Score: %d" % totalScore)
    print("Execution Time: %s" % (datetime.now() - start))

    print("\nSave Solutions:")
    saveSolutions(solutions)

    print("\nPack Source:")
    packSolution()

    if arguments.hasPopup:
        print("\nActivated Popup!")
        webbrowser.open(url=SUBMISSION_URL)
        subprocess.call('explorer "%s"' % os.path.join(os.path.dirname(os.path.realpath(__file__)), SOLUTION_FOLDER[2:-1]), shell=True)

    return totalScore

if __name__ == '__main__':
    b = (0.000001, 10.0)
    bnds = (b, b, b)

    optimize.minimize(fun=getOptimizeScore, x0=[1.0, 1.0, 1.0], method="POWELL", tol=10000, bounds = bnds)