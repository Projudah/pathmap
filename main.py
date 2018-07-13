import os

traversed = []
moreleft = False

def main():
	start = "C:\\Users\\proju\\Desktop"
	print(traverse(0, 0, start))
	print()


'''for aestethic reasons, i'm implementing a breadth first search'''


def traverse(depth, step, start):
	global moreleft
	os.chdir(start)
	submap = {}
	traversed.append(start)
	for file in os.listdir(start):
		current = os.path.abspath(file)
		if step < depth:
			if os.path.isdir(current):
				submap[file] = traverse(depth, step + 1, current)
				os.chdir(start)
			else:
				submap[file] = {}
		else:
			if os.path.isdir(current):
				os.chdir(current)
				for fileToCheck in os.listdir(current):
					fullpath = os.path.abspath(fileToCheck)
					if os.path.isdir(fullpath) and (fullpath not in traversed):
						moreleft = True
	if step == 0:
		if moreleft:
			moreleft = False
			traverse(depth + 1, 0, start)
		else:
			print(submap)

	return submap


if __name__ == '__main__':
	main()
