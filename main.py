import os
import time
from tkinter import *
import threading


def traverse(depth, step, start):
	"""for aesthetic reasons, i'm implementing a breadth first search"""
	global moreleft
	# print('traversing', start, 'depth:', depth, 'step:', step)
	os.chdir(start)
	submap = {}
	traversed.append(start)   #  if start is not in traversed, then add it
	count = 0
	for file in os.listdir(start):
		current = os.path.abspath(file)
		if step < depth:
			if os.path.isdir(current):
				submap[file] = traverse(depth, step + 1, current)
			else:
				traversed.append(current)
				submap[file] = {}
				if depth - step == 1:
					if (depth) not in depthWidth:
						depthWidth[depth] = 1
					else:
						depthWidth[depth] += 1
		else:
			if current not in traversed:
				count += 1
				moreleft = True
		os.chdir(start)

	if step == depth:  # if i'm at the current depth
		if (depth) in depthWidth:
			depthWidth[depth] += count
		else:
			depthWidth[depth] = count

	if step == 1:
		depthWidth[0] = 1
		draw(depth, submap)
		if moreleft:
			moreleft = False
			time.sleep(1)
			traverse(depth + 1, 1, start)
		else:
			print('_'*50,'\n',"DONE")

	return submap


def draw(depth, map):
	canvas.delete('all')
	# maxwidth = max(depthWidth, key=depthWidth.get)

	widthcount = [0] * (depth)

	search(map, widthcount, depth, 1)


def search(map, widthcount, maxdepth, depth, parentx=-1):
	myX = (canvas.winfo_width() / depthWidth[depth-1]) * widthcount[depth-1] + ((canvas.winfo_width() / depthWidth[depth-1])/2)
	myY = (canvas.winfo_height() / maxdepth) * (maxdepth - depth)
	myheight = canvas.winfo_height() / maxdepth

	canvas.create_line(myX, myY, myX, myY + myheight)

	widthcount[depth-1] += 1
	for dir in map:
		search(map[dir], widthcount, maxdepth, depth + 1, myX)


	if parentx >= 0:
		canvas.create_line(myX, myY, parentx, myY)



def main():
	global traversed
	global  depthWidth
	global moreleft
	traversed = []
	depthWidth = {}
	moreleft = False
	# start = "C:\\Users\\proju\\Desktop"
	start = "D:\\Downloads\\school notes and slides"
	run = threading.Thread(target=traverse, args=(1, 1, start))
	run.daemon = True
	run.start()


if __name__ == '__main__':
	traversed = []
	depthWidth = {}
	moreleft = False
	frame = Tk()
	frame.title('Map of your Computer')
	frame.state('zoomed')
	canvas = Canvas(frame, width=500, height=500)
	canvas.pack(expand=YES, fill=BOTH)
	startButton = Button(frame, text="Start", command=main)
	startButton.pack()
	mainloop()
