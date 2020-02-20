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

    return questions

def getOptimizeScore(x, *args) -> float:
    return -optimizeFunc(args[0], x)

def optimizeFunc(questions, parameters) -> float:
    solutions = solveAll(questions, parameters)
    scores = getScores(solutions)
    saveSolutions(solutions)

    total = getTotalScore(scores)

    print(total)

    return total

def main(parameters) -> float:
    questions = getQuestions()

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
    b = (0.5, 10.0)
    bnds = (b, b, b)

    questions = getQuestions()

    a= optimize.minimize(fun=getOptimizeScore,
                         x0=[1.55472633e-8, 3.58792896, 3.58792896],
                         method="Powell",
                         bounds = bnds,
                         options = {
                             "maxiter": 500,
                             "disp": True
                         }, args=(questions))
