from tkinter import *
import pygame
import math
from queue import PriorityQueue
import random
pygame.mixer.init()


bgimg=pygame.image.load("bg.png")
bgimg=pygame.transform.scale(bgimg,(900,500))

WIDTH = 1530
Height = 810

root1= Tk()
root1.geometry("1000x700")
root1.title('Introduction')
imagename=PhotoImage(file="bg.png")
background=Label(root1,image=imagename)
background.place(x=0,y=0,relheight=1,relwidth=1)
# icon
image_icon = PhotoImage(file="shortest_path.png")
root1.iconphoto(False, image_icon)
def get():
	root1.destroy()

label_0 =Label(root1,text="SHORTEST PATH VISUALISIER",width=40,font="canela 20 bold")
label_0.place(x=100,y=40)

label_5=Label(root1,text="Introduction to Interface",width=50,font=("canela 12 "))
label_5.place(x=200,y=110)


label_2=Label(root1,text="1. Select an Algorithm for finding a shortest path.\n",font=(10))
label_2.place(x=50,y=180)
label_3=Label(root1,text="2. Add the barrier's percentage in the grid.\n",font=(10))
label_3.place(x=50,y=230)

label_4=Label(root1,text="3. Mention the diagonals as neighbours or not.\n",font=(10))
label_4.place(x=50,y=280)
label_6=Label(root1,text="4. Select a starting node and ending node\n",font=(10))
label_6.place(x=50,y=330)

label_7=Label(root1,text="5. After selecting staring node and ending node, we can add more barriers.\n",font=(10))
label_7.place(x=50,y=380)
label_8=Label(root1,text="6. To Start The Algorithm, Press Space Bar!!!!.\n",font=(10))
label_8.place(x=50,y=430)
label_9=Label(root1,text="7. One Can Rerun the same Algorithm using the same Space Bar(Only after exection of the Algorithm).\n",font=(10))
label_9.place(x=50,y=480)
label_10=Label(root1,text="8. Press Ctrl+C to clear all the obstacle this will clear the entire Board including Start and End Node.\n",font=(10))
label_10.place(x=50,y=530)
Label(root1,text="Designed by Aman Aryan",font="italic 10 bold").place(x=800,y=610)

Button(root1, text='Done' ,font=(20),width=20,bg="black",fg='white',command=get).place(x=450,y=580)

root1.mainloop()


#choices	t


root = Tk()

root.geometry("500x500")

root.title("SHORTEST PATH VISUALISIER")
imagename=PhotoImage(file="bg1.png")
background=Label(root,image=imagename)
background.place(x=0,y=0,relheight=1,relwidth=1)

entry_4 = StringVar()
entry_1 = StringVar()
entry_3 = StringVar()


def getinfo():
    main(entry_4.get(),entry_1.get(),entry_3.get())

label_0 =Label(root,text="Select your Choices",width=20,font=("bold",20))
label_0.place(x=60,y=40)

label_5=Label(root,text="Algorithms",width=20,font=("bold",10))
label_5.place(x=40,y=130)

Algorithms =[
        "Breadth First Search",
        "Dijikstra's",]



droplist=OptionMenu(root,entry_4, *Algorithms)

droplist.config(width=25)

entry_4.set('Select Any of two Algorithms...')
droplist.place(x=240,y=130)



label_1 =Label(root,text="Diagnol Neighbors", width=20,font=("bold",10))
label_1.place(x=40,y=280)

diagnol=["yes","no"]

option3=OptionMenu(root,entry_3,*diagnol)
option3.place(x=240,y=280)

entry_3.set('Choose Yes or No')
option3.config(width=15)

label_1 =Label(root,text="Obstracle percentage", width=20,font=("bold",10))
label_1.place(x=40,y=200)

Obstacleper =["0%","10%","20%","30%","40%","50%","100%"]

    #temp.set(Obstracleper[0])
option2=OptionMenu(root,entry_1,*Obstacleper)
option2.config(width=25)


entry_1.set('Choose Obstacle percentage')
option2.place(x=240,y=200)




Button(root, text='Submit' , width=20,bg="black",fg='white',command=getinfo).place(x=180,y=380)



yel=(242, 227, 7)
bl=(112,205, 226)
blu=(0, 172, 205)
RED = (190,0,0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (181, 181, 22)
WHITE = (255, 255, 255)
BLACK = (60,60,60)
PURPLE = (128, 0, 128)
ORANGE = (201, 103, 170)
GREY = (128, 128, 128)
TURQUOISE = (15,135,0)

#CLASS

class Spot:
	def __init__(self, row, col,gap,gap1,width,height, total_rows,total_cols,diag):
		self.row = row
		self.col = col
		self.x = row * gap
		self.y = col * gap1
		self.color = WHITE
		self.neighbors = []
		self.diag=diag
		self.height=height
		self.width = width
		self.total_rows = total_rows
		self.total_cols = total_cols

	def get_pos(self):
		return self.row, self.col

	def is_closed(self):
		return self.color == RED

	def is_open(self):
		return self.color == GREEN

	def is_barrier(self):
		return self.color == BLACK

	def is_start(self):
		return self.color == RED

	def is_end(self):
		return self.color == TURQUOISE

	def reset(self):
		self.color = WHITE

	def make_start(self):
		self.color = RED

	def make_closed(self):
		self.color = blu

	def make_open(self):
		self.color = bl

	def make_barrier(self):
		self.color = BLACK

	def make_end(self):
		self.color = TURQUOISE

	def make_path(self):
		self.color = BLUE
		

	def draw(self, win):
		pygame.draw.rect(win, self.color, (self.y, self.x, self.width,self.height))

	def update_neighbors(self, grid):
		self.neighbors = []
		if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier(): # DOWN
			self.neighbors.append(grid[self.row + 1][self.col])

		if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): # UP
			self.neighbors.append(grid[self.row - 1][self.col])

		if self.col < self.total_cols - 1 and not grid[self.row][self.col + 1].is_barrier(): # RIGHT
			self.neighbors.append(grid[self.row][self.col + 1])

		if self.col > 0 and not grid[self.row][self.col - 1].is_barrier(): # LEFT
			self.neighbors.append(grid[self.row][self.col - 1])

		if(self.diag=="yes"):
			if self.col >0 and self.row < self.total_rows -1 and not grid[self.row+1][self.col-1].is_barrier(): # bottom left
				self.neighbors.append(grid[self.row+1][self.col-1])

			if self.col >0 and self.row >0 and not grid[self.row-1][self.col-1].is_barrier(): #top left
				self.neighbors.append(grid[self.row-1][self.col-1])

			if self.col < self.total_cols -1 and self.row < self.total_rows -1 and not grid[self.row+1][self.col+1].is_barrier(): #bottom right
				self.neighbors.append(grid[self.row+1][self.col+1])

			if self.row >0 and self.col < self.total_cols -1 and not grid[self.row-1][self.col+1].is_barrier():  #top right
				self.neighbors.append(grid[self.row-1][self.col+1])




	def __lt__(self, other):
		return False


def h(p1, p2,diag):
	x1, y1 = p1
	x2, y2 = p2

	if(diag=="yes"):
		if(x2==x1+1 and y2==y1+1):
			return(math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)))
		elif(x2==x1-1 and y2==y1+1):
			return(math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)))
		elif(x2==x1+1 and y2==y1-1):
			return(math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)))
		elif(x2==x1-1 and y2==y1+1):
			return(math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)))
		else:
			return abs(x1 - x2) + abs(y1 - y2)

	else:
		return abs(x1 - x2) + abs(y1 - y2)




def reconstruct_path(came_from, current, draw,temp,length):
	count=0
	t1=current
	while current in came_from:
		count+=1
		current = came_from[current]
		if(current!=temp):
		#print(current.get_pos())
			current.make_path()
			draw()
	pygame.mixer.music.stop()
	dialogbox1=Tk()
	dialogbox1.geometry("600x100")
	dialogbox1.title("Result")
	Label(dialogbox1,text=f"Total Nodes Explored by The Algorithm: {length} ",font="calibri 15 bold").pack()
	Label(dialogbox1,text=f"Shortest Path Found Is of Distance: {count} units",font="calibri 15 bold").pack()
	dialogbox1.mainloop()

	print("Shortest Path Found Is of Distance",count)



def algorithm(Algorithm,draw, grid, start, end,diag):
	pygame.mixer.music.load("music.mp3")
	pygame.mixer.music.play()
	count = 0
	open_set = PriorityQueue()
	open_set.put((0, count, start))
	current=0
	temp=start
	came_from = {}
	g_score = {spot: float("inf") for row in grid for spot in row}
	g_score[start] = 0
	f_score = {spot: float("inf") for row in grid for spot in row}
	f_score[start] = h(start.get_pos(), end.get_pos(),diag)
	count1=0
	t=[]
	open_set1 = PriorityQueue()
	open_set1.put((0, count1, end))
	current1=0
	came_from1 = {}
	g_score1 = {spot: float("inf") for row in grid for spot in row}
	g_score1[end] = 0
	f_score1 = {spot: float("inf") for row in grid for spot in row}
	f_score1[end] = h(end.get_pos(), start.get_pos(),diag)
	open_set_hash1={end}
	struct=[start]
	struct1=[end]
	open_set_hash = {start}


	if(Algorithm=="Breadth First Search"):
		
		visited=[]
		structure=[start]

		#structure.append(start)
		while structure:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()

			current=structure.pop(0)
			if current == end:
						
				print("Total Nodes Explored by The Algorithm  = ",len(visited))
				reconstruct_path(came_from, end, draw,temp,len(visited))
				end.make_end()
				return True



			if current not in visited:
				visited.append(current)
				for neighbor in current.neighbors:
					if neighbor == end:
						came_from[neighbor]=current
						
						print("Total Nodes Explored by The Algorithm  = ",len(visited))
						reconstruct_path(came_from, end, draw,temp,len(visited))
						end.make_end()
						return True

					if neighbor not in visited and neighbor not in structure:
						came_from[neighbor]=current
						structure.append(neighbor)
						neighbor.make_open()
			draw()
			
			if current != start:
				current.make_closed()
		



	
		
# Dijistra
	else:
		while not open_set.empty():
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()

			current = open_set.get()[2]

			open_set_hash.remove(current)


			if current == end:
				print("Total Nodes Explored By The Algorithm  = ",(count))
				reconstruct_path(came_from, end, draw,temp,count)
				end.make_end()
				return True


			for neighbor in current.neighbors:
					temp_g_score = g_score[current] + 1

					if temp_g_score < g_score[neighbor]:
						came_from[neighbor] = current
						g_score[neighbor] = temp_g_score 
						#f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
						if neighbor not in open_set_hash:
							count += 1
							open_set.put((g_score[neighbor], count, neighbor))
							open_set_hash.add(neighbor)
							if(neighbor!=end):
								neighbor.make_open()


			draw()
			if current != start:
				current.make_closed()


	print("Algorithm Failed!!")
	
	return False


def make_grid(cols,rows, width,height,diag):
	grid = []
	gap = height // rows
	col = width // cols

	for i in range(rows):
		grid.append([])
		for j in range(cols):
			spot = Spot(i, j,gap,col,width,height,rows,cols,diag)
			grid[i].append(spot)

	return grid



def draw_grid(win, cols,rows, width,height):
	col = width // cols
	gap = height // rows

	for i in range(rows):
		pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
		for j in range(cols):
			pygame.draw.line(win, GREY, (j * col,0), (j*col, height))


def draw(win,cols,grid, rows, width,height):

	win.fill(WHITE)

	for row in grid:
		for spot in row:
			spot.draw(win)

	draw_grid(win, cols,rows, width,height)
	pygame.display.update()


def get_clicked_pos(pos, rows,cols, width,height):
	gap = height // rows
	col1 = width // cols
	y, x = pos

	col = y// gap
	row = x // col1


	return row, col



def main(Algorithm,ob,diag):
     
	WIN = pygame.display.set_mode((WIDTH, Height))
	
	if(Algorithm=="Breadth First Search"):
		pygame.display.set_caption("Breadth First Search - Simple & Efficient Guarantees Shortest Path. ")
	
	else:
		pygame.display.set_caption("Dijikstra's - Father of PathFinding Algorithm Guarantees Shortest Path. ")
	
   
	win=WIN
	
	width=WIDTH
	height=Height
	ROWS =27
	cols=51
	grid = make_grid(cols,ROWS, width,height,diag)
	obs=str(ob)
	obs=obs.split('%')
	obs=int(obs[0])
	start = None
	end = None
	rc=0
	temp=0
	cc=0
	run = True
	if(obs==6):
		obs=10
	while run:
		draw(win,cols,grid, ROWS, width,height)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			if(temp==0):
				for row in grid:
					for spot in row:
						s=random.randint(0,100)
						if s < obs and spot != start and spot != end:
							spot.make_barrier()
						cc+=1
					rc+=1
				temp+=1

			if pygame.mouse.get_pressed()[0]: # LEFT
				pos = pygame.mouse.get_pos()
				row,col = get_clicked_pos(pos, ROWS,cols, width,height)
				spot = grid[row][col]
				if not start and spot != end:
					start = spot
					start.make_start()

				elif not end and spot != start:
					end = spot
					end.make_end()

				elif spot != end and spot != start:
					spot.make_barrier()

			elif pygame.mouse.get_pressed()[2]: # RIGHT
				pos = pygame.mouse.get_pos()
				row, col = get_clicked_pos(pos, ROWS,cols, width,height)
				spot = grid[row][col]
				spot.reset()
				if spot == start:
					start = None
				elif spot == end:
					end = None


			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE and start and end:
					
					for row in grid:
						for spot in row:
							

							spot.update_neighbors(grid)

					algorithm(Algorithm, lambda: draw(win, cols, grid, ROWS, width,height), grid, start, end,diag)
					
				if event.key == pygame.K_c:
					start = None
					end = None
					grid = make_grid(cols,ROWS, width,height,diag)

	pygame.quit()


root.mainloop()