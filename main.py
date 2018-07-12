import os

pathmap={}
traversed=[]
def main():
	start = "C:/Users/proju/Pictures"


'''for aestethic reasons, i'm implementing a breadth first search'''
def traverse(depth,step,start):
	for file in os.listdir(start):
		current = os.path.abspath(file)
		if step<depth:
			traverse(depth,step+1,current)
		else:
			pathmap[]


if __name__ == '__main__':
	main()