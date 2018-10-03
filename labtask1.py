"""Task1 --  this function returns list that contains the tuple (interfacename,"nameif"- value)"""
def name_interf(file_name):
	file=open(file_name)
	lst1=[]
	lst2=[]	#interface 
	lst3=[]	#interface name
	lst4=[]	#tuple of (interface,interface name)
	for line in file:
		line=line.strip()
		for word in line.split():
			lst1.append(word)	#make list of all words
	for i in range(len(lst1)):
		if lst1[i]=='interface':
			lst2.append(lst1[i+1])	#make list of interface
		elif lst1[i]=='nameif' or (lst1[i]=='no' and lst1[i+1]=='nameif'):
			#make list of interface name
			if lst1[i]=='no' and lst1[i+1]=='nameif':
				lst3.append('no name')
			elif lst1[i-1]!='no' and lst1[i]=='nameif':
				lst3.append(lst1[i+1])
	for i in range(len(lst2)):			#make list of tuple (interface,interface name)
		lst4.append((lst2[i],lst3[i]))
	return lst4

"""this function scan the configuration and return a dictionary that contains the "interface" as
the key and "nameif,VLAN,IPaddress,NetMask" list as the value"""
def name_net(file_name):
	file=open(file_name)
	lst1=[]
	lst2=[]	#list of interface
	lst3=[]	#interface name
	lst4=[]	#vlan
	lst5=[]	#ip add
	lst6=[]	#netmask
	lst7=[]	#lst of intName,vlan,ip add, netMask
	dict={}	#dict
	for line in file:
		line=line.strip()
		for word in line.split():
			lst1.append(word)
	for i in range(len(lst1)):
		if lst1[i]=='interface':
			lst2.append(lst1[i+1])  #make list of interface
		elif lst1[i]=='nameif' or (lst1[i]=='no' and lst1[i+1]=='nameif'):
			#make list of interface name
			if lst1[i]=='no' and lst1[i+1]=='nameif':
				lst3.append('no name')
				lst4.append('no vlan')	#for the networks which has no name,no ip, no netmask
				lst5.append('no ip address')
				lst6.append('no netmask')
			elif lst1[i-1]!='no' and lst1[i]=='nameif':
				lst3.append(lst1[i+1])
				lst5.append(lst1[i+6])
				lst6.append(lst1[i+7])
				if lst1[i-1]=='management-only':	#for management network
					lst4.append('no vlan')
				else:
					lst4.append(lst1[i-2]+lst1[i-1])
	for i in range(len(lst2)):
		lst7=[]
		lst7.append(lst3[i])
		lst7.append(lst4[i])
		lst7.append(lst5[i])
		lst7.append(lst6[i])
		dict[lst2[i]]=lst7	#add list of nameif,ip,netMask as value in dict
	return dict

if __name__=='__main__':
	print('list that contains the tuple (interfacename,"nameif"- value) is:\n',name_interf('running-config.cfg'))
	print('a dictionary that contains the "interfacename" as the key and "nameif,VLAN,IPaddress,NetMask" list as the value is :\n',name_net('running-config.cfg'))

