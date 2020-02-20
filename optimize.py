from scipy import optimize

def getScore():
    pass

optimize.minimize(fun=getScore, x0=[1.0, 1.0, 1.0], method="Nelder-Mead")