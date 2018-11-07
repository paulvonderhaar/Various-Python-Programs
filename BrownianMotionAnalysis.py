def main():
	DataIn=open("BrownianMotionData.txt","r")
	data=[[]]
	i=0
	for line in DataIn:
		ThisLine=float(line)
		if(line==0.0):
			data.append([])
			i+=1
		data[i].append(ThisLine)

	print(data[1])















main()