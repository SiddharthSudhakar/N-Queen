__author__ = 'Siddharth'
import numpy as np

#n= raw_input("Enter n size of board")
n =5 #for now

#Queen is maintained with rowise position
queen= np.zeros(n)
for p in xrange(n):
    queen[p]=-1

board= np.zeros((n,n))
#zero in board means that nothing has been placed
#1 means not possible area
#2 means a queen has been placed

def displayboard():
    print ("****")
    for p in xrange(n):
        for q in xrange(n):
            print board[p,q], "  ",
        print "\n"
    print ("****")


#Function to place queen and set board with possibilities********
def placequeen(x,y):
    #x is from row & y is from user input

    #*****remove other row possibilities
    for p in xrange(n):
        board[x,p] = 1

    #*****remove column possibilities
    for p in xrange(n):
        board[p,y] =1

    #***** Remove Left diagonal possibilities
    #equal sum logic for left diagonal
    p=0
    q=0
    for p in xrange(n):
        for q in xrange(n):
            #Left diagonal
            if (p+q) == (x+y):
                board[p,q]=1

    #****Remove Right diagonal possibilities
    #temp variables
    pp=x
    qq= y
    #top part of right diagonal
    while (pp>=0) & (qq>=0):
        board[pp,qq]=1
        pp=pp-1
        qq=qq-1
    #bottom part of right diagonal
    while (pp in range(0,n,1)) & (qq in range(0,n,1)):
        board[pp,qq]=1
        pp=pp+1
        qq=qq+1


    #place queen
    board[x,y]=2
    queen[x]=y
    print "Queen placed at (",x,",",y,")"
    displayboard()
    li= []
    print queen_avail(li), li
# Function Place queen ends********

#Function to check for any available queen locations
def queen_avail(avail_list):
    #Avail list is a list of tuples
    for p in xrange(n):
        for q in xrange(n):
            if board[p,q]== 0.0:
                avail_list.append((p,q))
    if not avail_list:
        return False
    else:
        return True


displayboard()
placequeen(3,3)
placequeen(0,1)
placequeen(1,4)
placequeen(2,0)