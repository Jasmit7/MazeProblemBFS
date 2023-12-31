import tkinter as tk
import random
from queue import Queue
from PIL import ImageTk,Image
import os
import time




maze = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,1,1,1,1,1,1,0,1,1,1,1,0,1,0,1,1,1,1,0,1,1,1,1,0,0,0,1,1,1,0,1,1,1,1,1,1,1,0,0,0,1,0,0,0,1,1,1,1,0],
        [0,1,0,0,1,0,0,0,0,0,0,1,0,1,0,1,0,0,1,0,1,0,0,1,1,1,1,1,0,1,0,1,0,0,1,0,0,1,0,0,0,1,1,1,1,1,0,0,0,0],
        [0,1,0,0,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,0,0,1,0,1,0,0,1,0,0,1,1,1,1,1,0,0,0,1,1,1,1,0],
        [0,1,1,0,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,1,0,0,0,1,0,0,1,0,1,1,1,1,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0],
        [0,0,1,0,0,0,0,1,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,0,0,1,0,0,1,0,1,0,0,0,0,1,1,1,1,1,0,1,0,1,0,0],
        [0,1,1,0,1,1,1,1,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,1,0,0,1,0,1,1,0,1,0,0,1,1,1,0,1,0,0,0,0,0,1,1,0],
        [0,1,0,0,1,0,0,1,0,1,1,1,1,1,0,0,0,0,0,1,1,1,0,0,0,0,1,0,0,1,0,1,0,0,1,0,0,1,0,1,1,1,1,1,1,1,0,1,0,0],
        [0,1,1,1,1,0,1,1,0,1,0,1,0,0,0,0,0,0,1,1,0,1,0,0,1,1,1,1,1,1,0,1,1,0,1,0,0,1,0,0,1,0,1,0,0,1,0,1,1,0],
        [0,0,1,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,1,0,0,1,1,1,1,0,0,0,0,1,0,0,1,0,1,0,0,1,0,0,1,0,1,0,0,1,0,1,0,0],
        [0,0,1,0,1,0,1,1,1,1,1,1,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,1,1,0,1,0,0,1,0,0,1,0,1,0,0,1,1,1,0,0],
        [0,1,1,1,1,0,0,1,0,1,0,1,1,1,0,0,0,1,1,1,1,1,1,1,0,0,1,1,1,1,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,1,1,0,1,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,1,1,0,0,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,0],
        [0,1,0,1,1,0,1,0,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0], 
        [0,0,0,0,0,0,1,0,0,0,1,0,0,1,0,1,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,1,1,1,1,0,1,0,1,0,1,0],
        [0,1,0,1,1,1,1,0,0,0,1,0,0,1,0,1,0,0,1,0,1,0,1,0,1,1,1,1,1,1,0,0,1,1,1,0,0,1,0,1,0,0,0,0,1,0,1,0,1,0],
        [0,1,0,0,0,0,1,0,0,1,1,1,1,1,0,1,0,0,1,1,1,0,1,0,1,0,0,0,0,1,0,0,1,0,0,0,0,1,0,1,1,1,0,0,1,0,1,0,1,0],
        [0,1,1,1,0,0,1,0,0,1,0,0,0,1,1,1,0,0,1,0,0,0,1,0,1,1,1,1,1,1,0,0,1,0,0,1,0,1,0,0,0,1,0,0,1,0,1,0,1,0],
        [0,0,0,1,0,0,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0],
        [0,1,1,1,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1,0,1,1,1,0],
        [0,1,0,0,0,0,0,1,1,1,1,1,0,1,0,0,0,0,1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,1,0,1,0,0,0,0,0],
        [0,1,0,1,1,1,0,1,0,0,1,0,0,1,0,0,1,1,1,0,0,1,0,0,0,1,0,1,1,1,1,1,1,0,0,1,0,1,0,1,1,1,1,0,1,1,1,1,1,0],
        [0,1,1,1,0,1,1,1,0,0,1,0,0,1,0,0,1,0,0,0,1,1,1,0,0,1,0,1,0,0,0,0,1,0,0,1,0,1,0,1,0,0,1,0,0,0,0,0,1,0],
        [0,0,1,0,0,1,0,1,0,0,1,0,0,1,0,0,1,0,0,0,1,0,1,1,1,1,0,1,0,1,1,1,1,0,0,1,0,1,0,1,1,1,1,1,1,1,1,0,1,0],
        [0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,1,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,1,0,0,0,0,1,0,0,0,1,0],
        [0,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,0,0,0,1,0,0,1,1,1,1,1,1,1,0],
        [0,1,0,0,1,0,0,1,1,1,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,1,0,1,0,0,0,0,0,1,0,1,1,1,0,0,1,0,0,0,0,0,1,0],
        [0,1,0,0,1,0,0,1,0,1,1,1,0,0,1,0,0,0,0,0,1,0,1,1,0,1,0,1,0,1,0,0,1,0,0,1,1,1,0,1,1,1,1,0,1,1,1,0,1,0],
        [0,1,0,1,1,1,0,1,0,0,0,1,1,1,1,1,0,1,1,1,1,0,1,0,0,1,1,1,0,1,1,1,1,1,1,1,0,0,0,0,0,0,1,0,1,0,1,0,1,0],
        [0,1,0,0,0,0,0,1,0,1,0,1,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,1,0,0,0,0,0,1,1,1,1,1,0,0,1,0,0,0,1,0,1,0],
        [0,1,1,1,1,0,0,1,0,1,0,1,0,0,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,0,1,0,0,0,1,0,1,0,1,1,1,1,1,0,0,1,1,1,0],
        [0,4,0,0,1,1,1,1,0,1,1,1,0,0,0,0,1,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,1,1,0,0,0,1,1,1,1,0,1,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
       ]

# maze = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
#         [0,1,0,0,0,0,0,1,0,0,0,0,0,1,0],
#         [0,1,0,0,0,0,0,1,0,0,0,0,0,1,0],
#         [0,1,0,0,0,0,0,1,0,0,0,0,0,1,0],
#         [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
#         [0,1,0,0,0,0,0,1,0,0,0,0,0,1,0],
#         [0,1,0,0,0,0,0,1,0,0,0,0,0,1,0],
#         [0,1,4,1,1,1,1,1,1,1,1,1,1,1,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#        ]
    
def makeMove(window,maze,node,move):
    i,j=node[0],node[1]
    if move == 0:
        i=i+1 #right
    if move == 1:
        i=i-1 #left
    if move == 2:
        j=j-1  #up
    if move == 3:
        j=j+1 #down

    if maze[i][j]==1:
        maze[i][j]=5
        cell_color = "yellow"
        label = tk.Label(window, width=1, height=1, bg=cell_color)
        label.grid(row=i, column=j)
    node = [i,j]
    return node;
    
    
def checkFinal(node,finalPos):
    i,j = node[0],node[1]
#     print("check:",i,j)
    if maze[i][j] == 4:
        return True
    return False
    
def genMove(node):
    moves=[]
    i,j = node[0],node[1]
    if maze[i+1][j] == 1 or maze[i+1][j] == 4: #down
        moves.append(0)
    if maze[i-1][j] == 1 or maze[i-1][j] == 4: #up
        moves.append(1)
    if maze[i][j-1] == 1 or maze[i][j-1] == 4: #left
        moves.append(2)
    if maze[i][j+1] == 1 or maze[i][j+1] == 4: #right
        moves.append(3)
    return moves
        
def bfs(window,i,j,finalPos):
    pos = [i,j]
    q= Queue()
    visited=[]
    print(finalPos)
    q.put((pos,[]))
    while not q.empty():
        node,path = q.get()
        visited.append(node)
        window.update() #tkinter updating every loop
        time.sleep(0.25)
        if checkFinal(node,finalPos)==True:
            return True,path
        
            
        for move in genMove(node):
            theMove = makeMove(window,maze,node,move)
            if theMove not in visited:
                q.put((theMove,path+[theMove]))
                visited.append(theMove)
                #print(path)
    return False
        
        
def initial_position():
    flag =True
    while(flag==True):
        i,j = random.randint(0,32),random.randint(0,49)
        if maze[i][j] == 1:
            flag = False
    return i,j

imgpath='pacman-g08f3a88d2_640.jpg'

imgpath1='download.jpeg'
def finalPath(window,path):
    cell_color = "green"
    
    #panel.pack(side='bottom',fill='both',expand='yes')
    #window.mainloop()
    for node in path:
        time.sleep(0.3)
        img = ImageTk.PhotoImage(Image.open(imgpath1))
        
        label = tk.Label(window, width=1, height=1,bg=cell_color,image=img)
        label.grid(row=node[0], column=node[1])
        window.update()
    
def create_maze_ui():
    # Create the main window
    window = tk.Tk()
    window.title("Group No.15 (Maze Problem using BFS)")
    #window.attributes('-fullscreen', True) 

    for i in range(len(maze)):
        for j in range(len(maze[i])):
            cell_color = "blue" if maze[i][j] == 0 else "black"
            if maze[i][j] == 4:
                cell_color = "red"
                finalPos = [i,j]
            label = tk.Label(window, width=1, height=1, bg=cell_color)
            label.grid(row=i, column=j)
    
    cell_color = "white"
    #i,j= initial_position()
    i,j = 20,48
    maze[i][j]=5
    print(i,j)
    label = tk.Label(window, width=1, height=1, bg=cell_color)
    label.grid(row=i, column=j)
    
    ans,path = bfs(window,i,j,finalPos);
    if ans == True:
        print("Yes, the path is possible \n")
    else:
        print("No, the path is not possible for the above maze")
    print("Path is as follows: \n",path)
    
    finalPath(window,path)
#     c = tk.Canvas(window, width=1, height=1, bg="black")
#     c.create_arc(i, j, i+1, j+1, fill=cell_color, style=PIESLICE, start=45, extent=270)
# #     app = pacmanFace(master=window)
#     # Start the main loop
    window.mainloop()

create_maze_ui()
