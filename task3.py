"""Task3 --- function to create a list of "access-list" for "global_access" and "fw-management_access_in"""

def access_lst(file_config):
	file=open(file_config) #file accessing though file_config parameter
	lst=[]
	for line in file:
	  line=line.strip()
	  for i in line.split():	#if line contains global-access or fw-management appends to list
		if i=='global_access' or i=='fw-management_access_in':
			lst.append(line)
	return lst
print(access_lst('running-config.cfg')		



