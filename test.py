def my_AVERAGE_main(data_list):
    
    if len(data_list)==0:
        return 0
    if len(data_list)>2:
        data_list.remove(min(data_list))
        data_list.remove(max(data_list))
        average_data = int(sum(data_list))/len(data_list)
        return average_data
    elif len(data_list)<=2:
        average_data = int(sum(data_list))/len(data_list)
        return average_data

active = True
while active:
	list = []
	a=input("vector<int>scores:")
	str = a.split(",")
	i=0
	while i<= len(str)+2:
		list.append(int(str.pop()))
		i+=1
	#print(list)
	average = my_AVERAGE_main(list)
	print(average)