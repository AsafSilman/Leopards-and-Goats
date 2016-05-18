# CITS1401 & CITS4406 Semester 1 2016
# Project 2 Start up code
# Snow Leopards are played by the computer
# Billy Goats are played by human
# Advanced solution has the option of swapping the above or human vs human or computer vs computer

#Asaf Silman 21985278
<<<<<<< HEAD
#Pranav Ganeswaran
=======
>>>>>>> origin/master

from graphics import *
import math
import random
import time

wSize = 800

possMoves =[[0,1],[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,0],[1, 0],[2, 1],[3, 2],[4,3],[5,4],[6, 5],[7, 6],[0, 7],[8, 9],[9,10],[10,11],[11,12],[12,13],[13,14],[14,15],[15,8],[9,8],[10,9],[11,10],[12,11],[13,12],[14,13],[15,14],[8,15],[16,17],[17,18],[18,19],[19,20],[20,21],[21,22],[22,23],[23,16],[17,16],[18,17],[19,18],[20,19],[21,20],[22,21],[23,22],[16,23],[0,8],[1,9],[2,10],[3,11],[4,12],[5,13],[6,14],[7,15],[8,16],[9,17],[10,18],[11,19],[12,20],[13,21],[14,22],[15,23],[8,0],[9,1],[10,2],[11,3],[12,4],[13,5],[14,6],[15,7],[16,8],[17,9],[18,10],[19,11],[20,12],[21,13],[22,14],[23, 15]]
# maintain a list of possible moves as a global variable

Leaps = [[0,16],[1,17],[2,18],[3,19],[4,20],[5,21],[6,22],[7,23],[16,0],[17,1],[18,2],[19,3],[20,4],[21,5],[22,6],[23,7],[0,2],[2,4],[4,6],[6,0],[2,0],[4,2],[6,4],[0,6],[8,10],[10,12],[12,14],[14,8],[10,8],[12,10],[14,12],[8,14],[16,18],[18,20],[20,22],[22,16],[18,16],[20,18],[22,20],[16,22]]

# the main function should control the flow of the program, allow the players to place the Goats and Leopards and decide who has won
# it uses the random function for placing the Leopards
def main():
    win = GraphWin('Problem Solving and Programming - Project 2',wSize,wSize)
    win.setBackground('green')
    win.setCoords(0,0,wSize,wSize)

    ptList = drawBoard(win)

    GoatsOccup = []
    LeopardsOccup = []
    unOccup = list(range(0,24))
    GoatPieces = []
    LeopardPieces = []

    #ALPHA CODE
    addPiece(1,LeopardPieces, unOccup)
    addPiece(4,LeopardPieces, unOccup)
    addPiece(2,GoatPieces,unOccup)
    addPiece(9,GoatPieces,unOccup)
    addPiece(0,GoatPieces,unOccup)
    print(unOccup)
    print(GoatPieces)
    print(blocked(LeopardPieces,unOccup))
    #END ALPHA CODE

    notify = Text(Point(wSize/2,40), 'Goats Turn')
    notify.setTextColor('blue')
    notify.draw(win)

    # let the human player place Billy Goats
    # let the computer place Snow Leopards
    # let the human player move a Goat
    # let the computer move a Leopard
    # decide who won the game
    
def drawBoard(win): # DO NOT change this function. It is provided to help you. It draws the board and returns a list of Points (24 points)
    bk = wSize/8 # block size
    ptList = []
    for i in range(1,4):
        ptList = ptList + [Point(bk*i,bk*i), Point(bk*i,4*bk), Point(bk*i,bk*(8-i)),Point(4*bk,bk*(8-i)),
                       Point(bk*(8-i),bk*(8-i)),Point(bk*(8-i), 4*bk), Point(bk*(8-i),bk*i),Point(4*bk,bk*i)]
        pp = Polygon(ptList[-8:])
        pp.setWidth(5)
        pp.setOutline(color_rgb(255,255,0))
        pp.draw(win)
    for i in range(8):
        ll = Line(ptList[i],ptList[i+16])
        ll.setWidth(5)
        ll.setFill(color_rgb(255,255,0))
        ll.draw(win)

    "Exra code added to add circles at points of legal play to make UI more friendly for player"
    for i in ptList:
        cir = Circle(i,5)
        cir.setFill("Red")
        cir.setOutline("black")
        cir.draw(win)

    return ptList


def blocked(Occup, unOccup):
    # returns True if all pieces in Occup are blocked otherwise False
    #Initialises variable to True
    blocked = True
    for i in Occup:
        #If ANY piece in Occup is NOT blocked
        #then blocked must be set to false
        if not blockedIndividual(i,unOccup):
            blocked = False
    return blocked

def blockedIndividual(piece,unOccup):
    blocked = True
    for i in possMoves:
        if i[0] == piece:
            if i[1] in unOccup:
                blocked = False
    return blocked
    
    
def moveGoat(win,ptList,Occup,Pieces,unOccup):
    # This function allows the human player to move a Goat to a valid location and updates the relevant lists. The move must be
    # animated slowly rather than an abrupt disappear and appear at the other location.
    # win is the GraphWin object, ptList is defined in drawBoard(), Occup is a list of occupied locations by the Goats, 
    # Pieces is a list of the Goat objects and unOccup is a list of empty locations. The function should allow the human to select and
    # unselect (by clicking twice) a piece. When a Goat is selected for a move, a mark (such as a small circle) must appear on it.
    # The mark should disappear when the piece is unselected or moved. This function does not return anything.
    return []


     
def AImoveLeapord(win,ptList,LeopardsOccup,LeopardPieces,unOccup, GoatPieces, GoatsOccup):
    # This function performs an intelligent move for the Leopards. It first checks if any of the Leopards can eat a Goat. If so, it makes
    # the corresponding move to eat the Goat. Otherwise, it performs a random Leopard move to a valid location.  In either case, the
    # move must be animated slowly rather than an abrupt disappear and appear at the other location.
    # LeopardsOccup are locations occpupied by Leopards, GoatsOccup are locations occupied by the Goats, LeopardPieces and
    # GoatPieces are lists containing the actual objects. unOccup is a list of emtpy locations. This function performs the move and
    # updates the corresponding lists. It does not return anything. 
    return []



def findNN(pt, ptList):
    # returns the index number and distance of the nearest point from pt
    # finds the nearest valid location on the board to the (clicked) pt in ptList. This allows the use to click near the location and not    
    # pricesly on top of the location to place/select/move a piece. It returns the distance d and the index location nn in ptList of the nearest point.

    dlist = [] # dlist is a list of all the distance values from each of the 24 individual points
    for i in ptList:
        dist = math.sqrt((pt.getX()-i.getX())**2+(pt.getY()-i.getY())**2)
        dlist.append(dist)
    #print(dlist)
    d = min(dlist)
    nn = dlist.index(min(dlist))
    #print(d) This is to check the distance
    return d, nn

def addPiece(position, Occup, unOccup):
    #if the position is in unOccup
    #Add that position to goats Occup
    #Then remove that number from Occup 
    if position in unOccup:
        Occup.append(position);
        unOccup.remove(position)

  
main()
    
    
    
