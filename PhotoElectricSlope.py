def main():
	AllDataIn=(open("Yellow Data2.txt","r"))
	AllDataOut=(open("Yellow Slope2.txt","w"))
	Current=[]
	Voltage=[]
	for line in AllDataIn:
		DataLine=line
		Data=DataLine.split()
		Current.append(float(Data[1]))
		Voltage.append(float(Data[0]))
	i=int(0)
	slope=0
	while i<len(Current)-1:
		num=(Current[i]-Current[i+1])
		denom=(Voltage[i]-Voltage[i+1])
		slope=(num/denom)
		AllDataOut.write(str(Voltage[i])+"    "+str(slope)+"\n")
		i+=1
		





main()