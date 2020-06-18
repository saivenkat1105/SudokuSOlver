import tkinter as tk
import time

line_init = 100
box_side = 50
timetaken = 0

nrows = 9



def ValidOrNot(num,mat,row,column):
        a = 1      
                    
                    
        if num == 0:
            return False
        for j in range((row//3)*3,(row//3)*3+3):
            for k in range((column//3)*3,(column//3)*3+3):
               
                if mat[j][k] == num:
                    return False
        if a != 0:    
            for i in range(nrows):
                if mat[row][i] == num:
                    return False
                if mat[i][column] == num:
                    return False

        return True
    
def NextEmptyCell(mat,row,column):
        for nextcolumn in range(column,nrows):
            if mat[row][nextcolumn] == 0:                
                return row,nextcolumn
        for nextrow in range(row+1,nrows):
            for nextcolumn in range(nrows):
                if mat[nextrow][nextcolumn] == 0:
                    return nextrow,nextcolumn
        
        nextrow,nextcolumn = 100,100 
        return nextrow,nextcolumn

def PrevCell(mat,row,column):
        for prevcolumn in reversed(range(column)):
            if mat[row][prevcolumn] == 0:                
                return row,prevcolumn
        for prevrow in reversed(range(row)):
            for prevcolumn in reversed(range(nrows)):
                if mat[prevrow][prevcolumn] == 0:
                    return prevrow,prevcolumn
        return 200,200

def PrintMat(mat):
        for i in range(nrows):
                print(mat[i][:])          
        
        
        
def SolveSudoku(mat):
        global numiter
        actualmat = list(map(list,mat))
        mat = list(map(list,actualmat))
        
        #print(actualmat)
        row = 0
        column = 0
        row,column = NextEmptyCell(mat,row,column)
        i = 0
        j = 0
        while True:
                     
            #print(row,column)
            if row == 100:
                break
            
            num = mat[row][column]

            while True:
                num += 1
                
                
                while num > nrows:
                        row,column = PrevCell(actualmat,row,column)
                        j = j+1
                        num = mat[row][column]
                        num += 1
                        
                        mat[row][column] = 0
                                
                    
                if ValidOrNot(num,mat,row,column) == True:
                    mat[row][column]=num
                    break
                i += 1
                                
                
                                
            
            row,column = NextEmptyCell(mat,row,column)
        #PrintMat(mat)
        numiter = i
        print(numiter)    
        return mat

        #print(i,j)
                

def callback(event):
    global rowgui, colgui,canvas
    
    
    x,y = event.x,event.y
    if (line_init < x <  line_init + box_side*9 and
        line_init < y < line_init +box_side*9):
        canvas.focus_set()
        colgui = int((x - line_init)/box_side)
        rowgui = int((y - line_init)/box_side)
        colorbox()
        #print(rowgui,colgui)
    else:
        canvas.focus_set()
        rowgui,colgui = -1,-1

def key(event):
    global rowgui,colgui,data,actualdata
    #print((event.char),'is typed')
    if rowgui >=0 and colgui >=0 and event.char in "1234567890":
        if data[rowgui][colgui] == 0:
            
            data[rowgui][colgui] = int(event.char)
            #print(data,int(event.char),rowgui,colgui,data[rowgui][colgui])
            actualdata = list(map(list,data))
            FillNumbers(canvas)
        else:
            
            canvas.delete("numbers" + str(rowgui)+str(colgui))
            data[rowgui][colgui] = int(event.char)
            actualdata = list(map(list,data))
            FillNumbers(canvas)

def backspace(event):
        global data, canvas,rowgui,colgui
        canvas.delete("numbers" + str(rowgui)+str(colgui))
        data[rowgui][colgui] = 0

def up(event):
        global data, canvas,rowgui,colgui
        if rowgui != 0:
                rowgui = rowgui - 1
        else:
                rowgui= 8
        colorbox()
def down(event):
        global data, canvas,rowgui,colgui
        if rowgui != 8:
                rowgui = rowgui + 1
        else:
                rowgui= 0
        colorbox()
def left(event):
        global data, canvas,rowgui,colgui
        if colgui != 0:
                colgui = colgui - 1
        else:
                colgui= 8
        colorbox()

def right(event):
        global data, canvas,rowgui,colgui
        if colgui != 8:
                colgui = colgui + 1
        else:
                colgui= 0
        colorbox()
        

def colorbox():
        global canvas,rowgui,colgui
        canvas.delete("colorbox")
        x1 = line_init + box_side*(colgui+1)
        y1 = line_init + box_side * (rowgui+1)
        x2 = line_init + box_side*colgui
        y2 = line_init + box_side*rowgui
        canvas.create_rectangle(x1,y1,x2,y2,outline = "red",tags = "colorbox")
        
        

def submit():
    global data,canvas,actualdata,timetaken,numiter
    canvas.delete("colorbox")
    actualdata = list(map(list,data))
    strttime = time.time()
    data = SolveSudoku(data)
    endtime = time.time()
    timetaken = endtime - strttime
    for i in range(9):
        for j in range(9):
            canvas.delete("numbers"+str(i)+str(j))    
    FillNumbers(canvas)
    

def clearall():
    global data,canvas
    data = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]
    for i in range(9):
        for j in range(9):
            canvas.delete("numbers"+str(i)+str(j))

   
 
def CreateGui():
    global data,canvas,timetaken,numiter
    #data = [[0]*9]*9
    window = tk.Tk()
    window.title("Sudoku Solver")
    headcanvas = tk.Canvas(window,bg ="white",bd = 0,highlightthickness=0,width = line_init+box_side*20,height = box_side*2)
    headcanvas.create_text(line_init + box_side*9,line_init/2,text = "Sudoku Solver",
                       font = ("Calibri",38),fill = "black")
    headcanvas.pack()
    window.configure(bg = 'white')
    firstframe = tk.Frame(window,bg = "white")
    firstframe.pack()
    canvasframe = tk.Frame(firstframe,bg = "white")
    textframe = tk.Frame(firstframe,bg = "white")
    canvasframe.pack(side="left")
    textframe.pack(side="left")
    
    canvas_width = line_init+box_side*11
    canvas_height = line_init+box_side*11
    canvas = tk.Canvas(master = canvasframe,bg = "white",width = canvas_width,
                       height = canvas_height,bd = 0,highlightthickness=0)

    
    canvas.pack(side = "left",expand = True)
    text = tk.Text(textframe,bd = 0,highlightthickness=0)
    text.insert(tk.INSERT,"Instructions For Use:\n")
    text.insert(tk.END,"1. Fill in the numbers into the sudoku puzzle.\n")
    text.insert(tk.END,"2. Once all the numbers are filled, press Submit button.\n")
    text.insert(tk.END,"3. To clear all the entries, press Clear button\n")
    text.insert(tk.END,"4. To clear a particular cell, select it and press backspace.\n")
    text.insert(tk.END,"5. Use Up, Down,Left and Right keys to move between cells.\n")
    text.insert(tk.END,"6. You can find the time taken for computation\n    and the number of iterations below.")
    text.tag_add("heading","1.0","1.21")
    text.tag_add("body","2.0",tk.END)
    text.tag_config("heading",font = ("Calibri",24))
    text.tag_config("body",font = ("Calibri",18))
    text.pack()
    
    frame = tk.Frame(textframe,bg = "white")
    frame.pack(side="bottom",expand = False)
    
    for i in range(10):
        if (i%3 == 0):
            color = "blue"
        else:
            color = "grey"
       
        xv1 = line_init*1 + box_side*i
        yv1 = line_init*1
        xv2 = line_init*1 + box_side*i
        yv2 = line_init*1+ box_side*9
        line1 = canvas.create_line(xv1,yv1,xv2,yv2,fill = color)
        line2 = canvas.create_line(yv1,xv1,yv2,xv2,fill = color)
        
    submitbtn = tk.Button(frame,text = "Submit",padx = "10",font = "Calibri,12",command = submit)
    submitbtn.pack(side = "left")
    
    clearbtn = tk.Button(frame,text = "Clear",font = "Calibri,12",command = clearall)
    clearbtn.pack(side="left")
        
    canvas.bind("<Button-1>",callback)
    canvas.bind("<Key>",key)
    canvas.bind("<BackSpace>",backspace)
    canvas.bind("<Tab>",left)
    canvas.bind("<Up>",up)
    canvas.bind("<Left>",left)
    canvas.bind("<Right>",right)
    canvas.bind("<Down>",down)  
 
    window.mainloop()
    

    
def FillNumbers(canvas):
    global numiter,timetaken
    for i in range(9):
        for j in range(9):
            canvas.delete("numbers"+str(i)+str(j))
    
    global data,actualdata
    
    for i in range(9):
        for j in range(9):
            num = data[i][j]
            if (num != 0):                
                x = line_init + box_side*j + box_side/2
                y = line_init + box_side*i + box_side/2
                if (num == actualdata[i][j]):
                    entry = canvas.create_text(x,y,text = num,fill = "black",
                                               font = ("Calibri",16),tags = "numbers"+str(i)+str(j))
                else:
                    entry = canvas.create_text(x,y,text = num,fill = "red",
                                               font = ("Calibri",16),tags = "numbers"+str(i)+str(j))
    if (min(min((data)))!= 0):
        canvas.delete("ctime")
        finaltext = canvas.create_text(line_init+box_side*9/2,line_init+box_side*10,
                                       text="Computation Time is "+str(timetaken)+"\n\n\n",tags="ctime",font = ("Calibri",12))
        finaltext1 = canvas.create_text(line_init+box_side*9/2,line_init+box_side*10,
                                       text="Number of iteartions are "+str(numiter),tags="ctime",font = ("Calibri",12))
            
            
                
##data = [
##[8, 0, 0, 0, 0, 0, 0, 0, 0],
##[0, 0, 3, 6, 0, 0, 0, 0, 0],
##[0, 7, 0, 0, 9, 0, 2, 0, 0],
##[0, 5, 0, 0, 0, 7, 0, 0, 0],
##[0, 0, 0, 0, 4, 5, 7, 0, 0],
##[0, 0, 0, 1, 0, 0, 0, 3, 0],
##[0, 0, 1, 0, 0, 0, 0, 6, 8],
##[0, 0, 8, 5, 0, 0, 0, 1, 0],
##[0, 9, 0, 0, 0, 0, 4, 0, 0]
##]

data = [
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0]
]

actualdata = list(map(list,data))               


CreateGui()
