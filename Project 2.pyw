# CITS1401 & CITS4406 Semester 1 2016
# Project 2 Start up code
# Snow Leopards are played by the computer
# Billy Goats are played by human
# Advanced solution has the option of swapping the above or human vs human or computer vs computer

#Asaf Silman 21985278
#Pranav Ganeswaran 21965512 


from graphics import *
import math
import random
import time

wSize = 800

possMoves =[[0,1],[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,0],[1, 0],[2, 1],[3, 2],[4,3],[5,4],[6, 5],[7, 6],[0, 7],[8, 9],[9,10],[10,11],[11,12],[12,13],[13,14],[14,15],[15,8],[9,8],[10,9],[11,10],[12,11],[13,12],[14,13],[15,14],[8,15],[16,17],[17,18],[18,19],[19,20],[20,21],[21,22],[22,23],[23,16],[17,16],[18,17],[19,18],[20,19],[21,20],[22,21],[23,22],[16,23],[0,8],[1,9],[2,10],[3,11],[4,12],[5,13],[6,14],[7,15],[8,16],[9,17],[10,18],[11,19],[12,20],[13,21],[14,22],[15,23],[8,0],[9,1],[10,2],[11,3],[12,4],[13,5],[14,6],[15,7],[16,8],[17,9],[18,10],[19,11],[20,12],[21,13],[22,14],[23, 15]]
# maintain a list of possible moves as a global variable

#leas are orginised [Start, End, Middle] -> where the middle would have to be an occupided goat.
Leaps = [[0,16,8],[1,17,9],[2,18,10],[3,19,11],[4,20,12],[5,21,13],[6,22,14],[7,23,15],[16,0,8],[17,1,9],[18,2,10],[19,3,11],[20,4,12],[21,5,13],[22,6,14],[23,7,15],[0,2,1],[2,4,3],[4,6,5],[6,0,7],[2,0,1],[4,2,3],[6,4,5],[0,6,7],[8,10,9],[10,12,11],[12,14,13],[14,8,15],[10,8,9],[12,10,11],[14,12,13],[8,14,15],[16,18,17],[18,20,19],[20,22,21],[22,16,23],[18,16,17],[20,18,19],[22,20,21],[16,22,23]]

# the main function should control the flow of the program, allow the players to place the Goats and Leopards and decide who has won
# it uses the random function for placing the Leopards
def main():

    win= drawStart()
    
    #win = GraphWin('Problem Solving and Programming - Project 2',wSize,wSize)
    #win.setBackground('green')
    win.setCoords(0,0,wSize,wSize)


    ptList = drawBoard(win)
    GoatsOccup = []
    LeopardsOccup = []
    unOccup = list(range(0,24))
    GoatPieces = []
    LeopardPieces = []

    
    
    #ALPHA CODE
    #addPiece(1,LeopardPieces, unOccup)
    #addPiece(4,LeopardPieces, unOccup)
    #addPiece(2,GoatPieces,unOccup)
    #addPiece(9,GoatPieces,unOccup)
    #addPiece(0,GoatPieces,unOccup)
    #print(unOccup)
    #print(GoatPieces)
    #print(blocked(LeopardPieces,unOccup))
    #END ALPHA CODE

    notify = Text(Point(wSize/2+200,40), 'Goats Turn')
    notify.setTextColor('Red')
    notify.setStyle("bold")
    notify.setSize(20)
    notify.draw(win)
    
    for i in range(3):
    # let the human player place Billy Goats
    # let the computer place Snow Leopards
        drawGoat(win,ptList,GoatsOccup,unOccup,GoatPieces,notify)
        AImoveLeapord(win,ptList,LeopardsOccup,LeopardPieces,unOccup, GoatPieces, GoatsOccup)
        drawLeopard(win,ptList,LeopardsOccup,unOccup,LeopardPieces,notify)
        

    print(GoatsOccup)
    print(unOccup)

    try:
        circ,goatObj,goatPt,goatIndex = selectGoat(win,ptList,GoatPieces,GoatsOccup)
    except TypeError:
        circ,goatObj,goatPt,goatIndex = selectGoat(win,ptList,GoatPieces,GoatsOccup)
    moveGoat(win,ptList,GoatsOccup,GoatPieces,unOccup,circ,goatObj,goatPt,goatIndex)

    print(GoatsOccup)
    print(unOccup)

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
        time.sleep(0.09)
    for i in range(8):
        ll = Line(ptList[i],ptList[i+16])
        ll.setWidth(5)
        ll.setFill(color_rgb(255,255,0))
        ll.draw(win)
        time.sleep(0.09)

    "Exra code added to add circles at points of legal play to make UI more friendly for player"
    for i in ptList:
        cir = Circle(i,5)
        cir.setFill("Red")
        cir.setOutline("black")
        cir.draw(win)
        time.sleep(0.01)

    return ptList


def blocked(Occup, unOccup):
    #returns True if all pieces in Occup are blocked otherwise False
    #Initialises variable to True
    blocked = True
    for i in Occup:
        #If ANY piece in Occup is NOT blocked
        #then blocked must be set to false
        if not blockedIndividual(i,unOccup):
            blocked = False
    return blocked

def blockedIndividual(piece,unOccup):
    """
    Tests if an individual piece is blocked
    This is a helper method for blocked.
    """
    blocked = True
    for i in possMoves:
        if i[0] == piece:
            if i[1] in unOccup:
                blocked = False
    return blocked
    
    
def moveGoat(win,ptList,GoatsOccup,GoatPieces,unOccup,circ,goatObj,goatPt,goatIndex):
    # This function allows the human player to move a Goat to a valid location and updates the relevant lists. The move must be
    # animated slowly rather than an abrupt disappear and appear at the other location.
    # win is the GraphWin object, ptList is defined in drawBoard(), Occup is a list of occupied locations by the Goats, 
    # Pieces is a list of the Goat objects and unOccup is a list of empty locations. The function should allow the human to select and
    # unselect (by clicking twice) a piece. When a Goat is selected for a move, a mark (such as a small circle) must appear on it.
    # The mark should disappear when the piece is unselected or moved. This function does not return anything.

    pt = win.getMouse()
    d,nn = findNN(pt,ptList)
    
    if goatPt.getX() == ptList[nn].getX() and goatPt.getY() == ptList[nn].getY():
        #this tests to see if the goat object returned by click is the same as the one selected in first click from selectGoat() function
        circ.undraw()
        circ,goatObj,goatPt,goatIndex = selectGoat(win,ptList,GoatPieces,GoatsOccup)
        moveGoat(win,ptList,GoatsOccup,GoatPieces,unOccup,circ,goatObj,goatPt,goatIndex)

    else:
        #if valid move, performs a animated movement of goat
        if checkValid(nn,goatIndex,unOccup):
            x,y = (ptList[nn].getX() - goatPt.getX()),(ptList[nn].getY() - goatPt.getY())
            for i in range(20):
                goatObj.move(x/20,y/20)
                time.sleep(0.01)
            circ.undraw()

            unOccup.append(goatIndex)
            unOccup.remove(nn)
            GoatsOccup.append(nn)
            GoatsOccup.remove(goatIndex)
            
        else:
            #mouseclick elswhere causes cicle to be removed and selection process to happen again
            circ.undraw()
            circ,goatObj,goatPt,goatIndex = selectGoat(win,ptList,GoatPieces,GoatsOccup)
            moveGoat(win,ptList,GoatsOccup,GoatPieces,unOccup,circ,goatObj,goatPt,goatIndex)
    return []


     
def AImoveLeapord(win,ptList,LeopardsOccup,LeopardPieces,unOccup, GoatPieces, GoatsOccup):
    # This function performs an intelligent move for the Leopards. It first checks if any of the Leopards can eat a Goat. If so, it makes
    # the corresponding move to eat the Goat. Otherwise, it performs a random Leopard move to a valid location.  In either case, the
    # move must be animated slowly rather than an abrupt disappear and appear at the other location.
    # LeopardsOccup are locations occpupied by Leopards, GoatsOccup are locations occupied by the Goats, LeopardPieces and
    # GoatPieces are lists containing the actual objects. unOccup is a list of emtpy locations. This function performs the move and
    # updates the corresponding lists. It does not return anything. 
    moves = []
    for leopard in LeopardsOccup:
        if leapable(leopard,GoatsOccup,unOccup):
            move = leapable(leopard,GoatsOccup,unOccup)
            goat = ptList[move[2]] #the goat variable now holds the point on the board
            GoatsOccup.remove(move[2])
            unOccup.append(move[2])

            #Removes the goat from the board
            for i in GoatPieces:
                if goat.getX() == i.getAnchor().getX() and goat.getY() == i.getAnchor().getY():
                    i.undraw()
                    GoatPieces.remove(i)

            makeMove(move[0],move[1],unOccup, LeopardsOccup, LeopardPieces, ptList)
            return
        if movable(leopard,unOccup):
            for i in possMoves:
                if i[0] == leopard and i[1] in unOccup:
                    moves.append(i)
    if not moves:
        return

    r = random.randrange(0,len(moves))
    makeMove(moves[r][0],moves[r][1],unOccup, LeopardsOccup, LeopardPieces, ptList)  
    return []

def makeMove(piece, move, unOccup, pieceOccup, pieceObjects, ptList):
    """
    moves the piece at location 'piece' on the board to location 'move'
    then animates the move
    """
    if move in unOccup: #if the move is a valid one
        pieceLocation = ptList[piece] #grabing the piece object
        for i in pieceObjects:
            if pieceLocation.getX() == i.getAnchor().getX() and pieceLocation.getY() == i.getAnchor().getY():
                pieceOccup.remove(piece)
                unOccup.append(piece)
                pieceOccup.append(move)
                
                newPoint = ptList[move]
                x,y = newPoint.getX() - i.getAnchor().getX(),newPoint.getY() - i.getAnchor().getY()
                for k in range(20):
                        i.move(x/20,y/20)
                        time.sleep(0.01)


def leapable(piece, GoatOccup,unOccup):
    """
    Tests the leopard piece to see whether it can perform a leap
    if true it returns the list
    otherwise it returns false
    """
    for i in Leaps:
        if i[0] == piece and i[2] in GoatOccup and i[1] in unOccup:
            return i
    return False
    
def movable(piece,unOccup):
    """
    Checks is a piece has any valid moves
    """
    for i in possMoves:
        if i[0] == piece and i[1] in unOccup:
            return True
    return False

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
    #print(d)---> This is to check the distance
    return d, nn

def addPiece(position, Occup, unOccup):
    #if the position is in unOccup
    #Add that position to list Occup
    #Then remove that number from Occup 
    if position in unOccup:
        Occup.append(position);
        unOccup.remove(position)


def drawGoat(win,ptList,GoatsOccup,unOccup,GoatPieces,notify):
    #changes the notification text
    #gets the mouseclick and passes on "nn" index to check in list
    #if nn not in the list, draws object and updates the lists
    notify.setText("Goats's Turn")
    length = len(GoatsOccup)
    while len(GoatsOccup) < length+4:
        pt = win.getMouse()
        d,nn = findNN(pt,ptList)
        if nn in unOccup:    
            goat = Image(ptList[nn],"goat.png")
            goat.draw(win)
            GoatPieces.append(goat)
            GoatsOccup.append(nn)
            unOccup.remove(nn)
    return []
    
def drawLeopard(win,ptList,LeopardsOccup,unOccup,LeopardPieces,notify):
    #changes the notification text
    #randomly chooses a spot from the unOccup list 
    #uses index from unOccup list to draw the object with time delay for animated effect 
    notify.setText("Leopard's Turn")
    time.sleep(1)
    index = random.choice(unOccup) 
    leopard = Image(ptList[index],"leopard.png")
    leopard.draw(win)
    LeopardPieces.append(leopard)
    LeopardsOccup.append(index)
    unOccup.remove(index)
    notify.setText("Goats's Turn")
    return []

def selectGoat(win,ptList,GoatPieces,GoatsOccup):
        """gets mouseclick and compares it to see if goat object in same place as mouse click"""
        pt = win.getMouse()
        d,nn = findNN(pt,ptList)
        for i in GoatPieces:
            if i.getAnchor().getX() == ptList[nn].getX() and i.getAnchor().getY() == ptList[nn].getY():
                goatObj = i
                goatPt = i.getAnchor()
                circ = Circle(ptList[nn],7)
                circ.setFill('cyan')
                circ.draw(win)
                return circ,goatObj,goatPt,nn
                
def checkValid(nn,goatIndex,unOccup):
    #checks to see if the index of the location you want to move to is in unOccup
    #checks next to see if you index of goat to unoccupied space is a legal move
    if nn in unOccup:
        if [goatIndex,nn] in possMoves:
            return True
    else:
        print("Invalid Move")

def isClicked(pt,button):
    """tests if mouse click is within button or not"""
    if pt.getX() >= button.getP1().getX() and pt.getX() <= button.getP2().getX() and pt.getY() >= button.getP1().getY() and pt.getY() <= button.getP2().getY():
        return True
    else:
        return False

def drawStart():
    """buttons and labels in order of [Play,Quit]"""
    button = [Rectangle(Point(100,100),Point(300,200)),Rectangle(Point(500,100),Point(700,200))]
    labels = [Text(Point(200,150),"Play"),Text(Point(600,150),"Quit")]
    win = GraphWin('Problem Solving and Programming - Project 2',wSize,wSize)
    backg = Image(Point(400,400),"mountain.png")
    backg.draw(win)
    win.setCoords(0,0,wSize,wSize)
    for i,j in zip(button,labels):
        i.setFill("Yellow")
        i.setOutline("red")
        i.setWidth(3)
        i.draw(win)
        j.setStyle("bold italic")
        j.setSize(20)
        j.draw(win)

    title = Text(Point(400,680),"Mountains Goats vs. Snow Leopards")
    title.setFace("arial")
    title.setStyle("bold")
    title.setSize(30)
    title.setFill("Red")
    title.draw(win) 

    while True:
        pt = win.getMouse()
        if isClicked(pt,button[0]):
            title.undraw()
            for i,j in zip(button,labels):
                i.undraw()
                j.undraw()
            break
        elif isClicked(pt,button[1]):
            win.close()

    return win
  
main()
