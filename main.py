import os

pathmap = {}
traversed = []


def main():
	start = "C:\\Users\\proju\\Desktop\\classes"
	print(traverse(3,0,start))
	print(traversed)


'''for aestethic reasons, i'm implementing a breadth first search'''
def traverse(depth, step, start):
	os.chdir(start)
	submap={}
	traversed.append(start)
	for file in os.listdir(start):
		current = os.path.abspath(file)
		# current = current.replace(os.sep,'/')
		if step < depth:
			if current in traversed:
				pass
			else:
				if os.path.isdir(current):
					submap[file]=traverse(depth, step + 1, current)
					os.chdir(start)
				else:
					submap[file]={}
	return submap

if __name__ == '__main__':
	main()
