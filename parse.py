# Parser - Handle Save/Load Files

from utils.constants import QUESTION_FOLDER, SOLUTION_FOLDER
from glob import glob
from classes import Question, Solution, Arguments
import sys
import warnings

# Load Question

def loadQuestion(file_name: str) -> Question:
    warnings.warn("TODO LOAD QUESTION: %s" % file_name)
    return Question(file_name=file_name)

def loadQuestions(file_names: [str] = []) -> [Question]:
    questions = []

    if len(file_names) > 0:
        for f in file_names:
            questions.append(loadQuestion(f))
    else:
        for f in glob(QUESTION_FOLDER + '*.*'):
            questions.append(loadQuestion(f))

    return questions

# Save Question

def saveSolution(solution: Solution):
    file = open('solution/' + solution.file_name + '.solve', 'w')
    nbLibraries = len(solution.library_books)

    file.write("{}\n".format(nbLibraries))

    for lib,books in solution.library_books:
        file.write("{} {}\n".format(lib.id, len(books)))
        file.write("{}\n".format(' '.join([str(x.id) for x in books])))

    file.close()


def saveSolutions(solutions: [Solution]):
    for solution in solutions:
        saveSolution(solution)

# Handle Argv

def handleArgv() -> Arguments:
    arguments = Arguments()

    for arg in [x.lower() for x in sys.argv[1:]]:
        if arg == '-p':
            arguments.hasPopup = True
        elif arg == '-sq':
            arguments.usesQuestionSample = True
        elif arg == '-ss':
            arguments.usesSolutionSample = True
        elif arg == '-h':
            print('\nUsage: python . [-h] [-n] [-sq] [-ss] [[file_name_1] [file_name_2] ...]')
            print('-h: Help and usage.')
            print('-p: Activates the automatic popup for submission.')
            print('-sq: Uses temporary sample question.')
            print('-ss Uses temporary sample solution.')
            print('file_name_n: File name to find a solution (by default, runs all files in QUESTION_FOLDER).')
            exit(0)
        else:
            arguments.files.append(arg)

    return arguments