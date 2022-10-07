from graphics import *
import math

screenwidth = 1400
screenheight = 1000
radiusofbigcircle = 450
radiusofsmallcircle = 25


array = [[0,	71,	151,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0, 0],
        [71,	0,	0,	75,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0, 0],
        [151,	0,	0,	140,	0,	0,	0,	0,	0,	0,	80,	0,	99,	0,	0,	0,	0,	0,	0,	0, 80],
        [0,	75,	140,	0,	118,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0, 0],
        [0,	0,	0,	118,	0,	111,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0, 0],
        [0,	0,	0,	0,	111,	0,	70,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0, 0],
        [0,	0,	0,	0,	0,	70,	0,	75,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0, 0],
        [0,	0,	0,	0,	0,	0,	75,	0,	120,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0, 0],
        [0,	0,	0,	0,	0,	0,	0,	120,	0,	138,	146,	0,	0,	0,	0,	0,	0,	0,	0,	0, 146],
        [0,	0,	0,	0,	0,	0,	0,	0,	138,	0,	97,	101,	0,	0,	0,	0,	0,	0,	0,	0, 97],
        [0,	0,	80,	0,	0,	0,	0,	0,	146,	97,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0, 0],
        [0,	0,	0,	0,	0,	0,	0,	0,	0,	101,	0,	0,	211,	90,	85,	0,	0,	0,	0,	0, 0],
        [0,	0,	99,	0,	0,	0,	0,	0,	0,	0,	0,	211,	0,	0,	0,	0,	0,	0,	0,	0, 0],
        [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	90,	0,	0,	0,	0,	0,	0,	0,	0, 0],
        [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	85,	0,	0,	0,	98,	0,	0,	0,	0, 0],
        [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	98,	0,	142,	86,	0,	0, 0],
        [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	142,	0,	0,	92,	0, 0],
        [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	86,	0,	0,	0,	0, 0],
        [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	92,	0,	0,	87, 0],
        [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	87,	0, 0],
        [0, 0, 80, 0, 0, 0, 0, 0, 146, 97 ,0 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0 ,0]]


names = ['Ordea', 'Zerind', 'Sibiud', 'Arad', 'Timisoara', 'Lugoj', 'Mehadia', 'Drobeta', 'Craiova', 'Pitesti', 'Rimnicu', 'Bucharest', 'Fagaras', 'Giurgiu', 'Urziceni', 'Hirsova', 'Vaslui', 'Eforie', 'Iasi', 'Neamt', 'R. Vilcea']
numberofsmallcircles = len(array[0])
def drawLines(arrayofcoordinates, listPoints, window):
    arraylength = len(array[0])
    for x in range(0, len(array[0])):
        for y in range(0, arraylength):
            if array[x][y] != 0:
                drawLine(x, y, listPoints, window, 'blue')
    arraylength = arraylength - 1

def pointsInCircum(r,n):
    return [(screenwidth/2+math.cos(2*math.pi/n*x)*r,screenheight/2+math.sin(2*math.pi/n*x)*r) for x in range(0,n+1)]

def drawLetters(listPoints, names, window):
    for x in range(0, len(array[0])):
        label = Text(Point(listPoints[x][0], listPoints[x][1]), names[x])
        label.draw(window)

def drawSmallCircles(listPoints,radCircle, window, color):
    lengthofarray = len(listPoints)
    for x in range(0, lengthofarray):
        circle = Circle(Point(listPoints[x][0],listPoints[x][1]), radCircle)
        circle.draw(window)
        circle.setOutline(color) 
        circle.setFill('white')


def drawLine(noFirst, noSecond, listPoints, window, colorofline):
    line = Line(Point(listPoints[noFirst][0],listPoints[noFirst][1]), Point(listPoints[noSecond][0],listPoints[noSecond][1]))
    line.draw(window)
    line.setOutline(colorofline)

def main():
    win = GraphWin("Canadian Traveler Problem", screenwidth, screenheight)

    pt = Point(screenwidth/2, screenheight/2)


    points = pointsInCircum(radiusofbigcircle, numberofsmallcircles)
    print(points)

    
    drawLines(array, points, win)
    
    drawSmallCircles(points, radiusofsmallcircle, win, 'blue')

    drawLetters(points, names, win)

    
    win.getMouse()
    win.close()
main()




