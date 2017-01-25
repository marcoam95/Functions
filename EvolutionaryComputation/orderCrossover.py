
def order(ref2,son,parent):

	posson=(ref2+1)%len(parent1)
	posparent=(ref2+1)%len(parent1)

	while 0 in son:
		if not parent[posparent] in son:
			son[posson]=parent[posparent]
			posson=(posson+1)%len(parent1)
		posparent=(posparent+1)%len(parent1)
	return son

def orderCrossover(ref1,ref2,parent1,parent2):
	son1 = [0] * len(parent1)
	son2 = [0] * len(parent1)

	son1[ref1:ref2] = parent1[ref1:ref2]
	son1[ref2] = parent1[ref2]
	son2[ref1:ref2] = parent2[ref1:ref2]
	son2[ref2] = parent2[ref2]

	#Son1 is completed from parent2
	son1=order(ref2,son1,parent2)
	#Son2 is completed from parent1
	son2=order(ref2,son2,parent1)

	
	return son1,son2


parent1=[5,2,3,1,4]
parent2=[2,4,1,3,5]

son1,son2=orderCrossover(1,2,parent1,parent2)

print parent1,parent2
print son1,son2