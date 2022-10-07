from algorithm import *
from DrawGraph import *

def main():
    pathResult, pathBlockedResult = calculate()
    print(pathResult)
    print(pathBlockedResult)
    
    drawGraph(pathResult, pathBlockedResult)
    
    
    return
main()