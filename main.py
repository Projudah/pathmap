import os
from tkinter import *
import threading


def traverse(depth, step, start):
	"""for aesthetic reasons, i'm implementing a breadth first search"""
	global moreleft
	print('traversing', start, 'depth:', depth, 'step:', step)
	os.chdir(start)
	submap = {}
	traversed.append(start)
	count = 0
	for file in os.listdir(start):
		current = os.path.abspath(file)
		if step < depth:
			if os.path.isdir(current):
				submap[file] = traverse(depth, step + 1, current)
			else:
				traversed.append(current)
				submap[file] = {}
		else:
			if current not in traversed:
				count += 1
				moreleft = True
		os.chdir(start)

	if step == depth:  # if i'm at the current depth
		if depth in depthWidth:
			depthWidth[depth] += count
		else:
			depthWidth[depth] = count

	if step == 0:
		if moreleft:
			print('entering depth', depth + 1)
			moreleft = False
			traverse(depth + 1, 0, start)
		else:
			print(submap)
			print()
			print('maximum depth:', depth)

	return submap


def draw(depth, map):
	canvas.delete('all')


def main():
	# start = "C:\\Users\\proju\\Desktop"
	start = "C:\\Users\\proju\\Videos"
	run = threading.Thread(target=traverse, args=(0, 0, start))
	run.daemon = True
	run.start()


if __name__ == '__main__':
	traversed = []
	depthWidth = {}
	moreleft = False
	frame = Tk()
	frame.title('Map of your Computer')
	canvas = Canvas(frame, width=500, height=500)
	canvas.pack(expand=YES, fill=BOTH)
	startButton = Button(frame, text="Start", command=main)
	startButton.pack()
	mainloop()
