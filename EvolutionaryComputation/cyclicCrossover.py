import random

#Given a list, return the next item which value is zero
def nextEmpty(parent):
	for i in range(0,len(parent)):
		if parent[i]==0:
			return i

#Given a list and number, returns the first ocurrence index
def findNumberIndex(parent,number):
	return parent.index(number)

def cyclicCrossover(parent1,parent2,threshold):
	#Sons initialization
	son1=[0]*len(parent1)
	son2=[0]*len(parent1)


	#While the sons are not completed the loop iterates completing the cycles
	while 0 in son1:
		#The pointer is positioned where is the first zero
		pos = nextEmpty(son1)
		#Storage of start position to finish cycles
		startPosition=pos

		aleat=random.random()

		#Iterates to complete a cycle
		while True:

			

			#If a random number is less than threshold cycle clones the cycle of parent in son 
			if aleat < threshold:
				son1[pos]=parent1[pos]
				son2[pos]=parent2[pos]
				#Update the index where to seach
				indexP2=findNumberIndex(parent2,son1[pos])
			else:
				#Else the son1 will receive parent2 cycle positions and son2 the parent1 cycle positions
				son1[pos]=parent2[pos]
				son2[pos]=parent1[pos]
				indexP2 = findNumberIndex(parent1, son1[pos])

			#If the current index equals to start index, the cycle will be completed
			if indexP2==startPosition:
				break

			pos = indexP2
	return son1,son2

parent1=[1,2,3,4,5]
parent2=[5,1,3,2,4]

#Threshold must be < 1
son1,son2=cyclicCrossover(parent1,parent2,0.5)

print parent1,parent2
print son1,son2