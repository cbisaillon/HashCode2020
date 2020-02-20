# Main File (LIGHT MODIFICATIONS)

from utils.pack import packSolution
from parse import loadQuestions, saveSolutions, handleArgv
from algorithm import solveAll
from score import getScores
import os
from utils.constants import SOLUTION_FOLDER
from utils.secret import SUBMISSION_URL
import webbrowser
import subprocess
from sample import loadQuestionSamples, loadSolutionSamples
from datetime import datetime

def main():
    start = datetime.now()

    print("Hash Code 2020")

    arguments = handleArgv()

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

    print("\nSolve Questions:")
    if arguments.usesSolutionSample:
        solutions = solveAll(loadSolutionSamples())
    else:
        solutions = solveAll(questions)

    if not arguments.silentMode:
        for solution in solutions:
            print(solution)

    print("\nSave Solutions:")
    saveSolutions(solutions)

    print("\nEvaluate Solutions:")
    scores: [Score] = getScores(solutions)

    totalScore = 0

    for score in scores:
        print(score)
        totalScore += score.val

    print("Total Score: %f" % totalScore)
    print("Execution Time: %s" % (datetime.now() - start))

    print("\nPack Source:")
    packSolution()

    if arguments.hasPopup:
        print("\nActivated Popup!")
        webbrowser.open(url=SUBMISSION_URL)
        subprocess.call('explorer "%s"' % os.path.join(os.path.dirname(os.path.realpath(__file__)), SOLUTION_FOLDER[2:-1]), shell=True)
        
if __name__ == '__main__':
    main()