import os
import time
from tkinter import *
from tkinter import filedialog
import threading


def traverse(depth, step, start):
	"""for aesthetic reasons, i'm implementing a breadth first search"""
	global moreleft
	# print('traversing', start, 'depth:', depth, 'step:', step)
	os.chdir(start)
	submap = {}
	traversed[start]=start  # if start is not in traversed, then add it
	count = 0
	try:
		for file in os.listdir(start):
			current = os.path.abspath(file)
			if step < depth:
				if os.path.isdir(current):
					submap[file] = traverse(depth, step + 1, current)
				else:
					traversed[current]=current
					submap[file] = {}
					if depth - step == 1:
						if (depth) not in depthWidth:
							depthWidth[depth] = 0
						else:
							depthWidth[depth] += 0
			else:
				if current not in traversed:
					count += 1
					moreleft = True
			os.chdir(start)
	except BaseException as e:
		print(str(e))

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
			time.sleep(0.5)
			traverse(depth + 1, 1, start)
		else:
			print('_' * 50, '\n', "DONE", start)

	return submap


def draw(depth, map):
	canvas.delete('all')
	maxwidth = max(depthWidth, key=depthWidth.get)

	widthcount = [0] * (depth)

	search(map, widthcount, depth, 1, maxwidth)


def search(map, widthcount, maxdepth, depth, maxwidth, parentx=-1):
	percent = 0.2
	myX = -1
	myY = -1
	cumulate = []

	myY = (canvas.winfo_height() / maxdepth) * (maxdepth - depth)
	myheight = canvas.winfo_height() / maxdepth
	join = myheight * percent
	if (depth - 1) >= maxwidth:
		myX = (canvas.winfo_width() / depthWidth[depth - 1]) * widthcount[depth - 1] + (
				(canvas.winfo_width() / depthWidth[depth - 1]) / 2)

		canvas.create_line(myX, myY + join, myX, myY + myheight)
		if parentx >= 0:
			canvas.create_line(myX, myY + myheight, parentx, (myY + myheight + join),fill='red')

	widthcount[depth - 1] += 1
	for dir in map:
		cumulate.append(search(map[dir], widthcount, maxdepth, depth + 1, maxwidth, myX))

	if (depth - 1) < maxwidth:
		if len(cumulate) == 0:
			myX = (canvas.winfo_width() / 2)
		else:
			myX = (sum(cumulate) / float(len(cumulate)))

		canvas.create_line(myX, myY + join, myX, myY + myheight)
		if parentx < 0:
			for loc in cumulate:
				canvas.create_line(myX, myY + join, loc, myY,fill='red')
	return myX


def main():
	global traversed
	global depthWidth
	global moreleft
	traversed = {}
	depthWidth = {}
	moreleft = False
	start = "C:"
	select = filedialog.askdirectory()
	if select is not "":
		start = select
	run = threading.Thread(target=traverse, args=(1, 1, start))
	run.daemon = True
	run.start()


if __name__ == '__main__':
	traversed = {}
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
