import csv  # to read csv file
fin=open("crime1.csv","r")
def crimes_halifax():
  d=dict()                      #created dictionary
  list1=list()			#created list
  list2=list()			#created list
  for line in fin:
    line=line.strip()
    lines=line.split('\t')
    list1.append(lines[-1])
    list2.append(lines[-2])
    combined=zip(list1,list2)		#to assign one to one
  
  for type in list1:
    if (type=='RUCR_EXT_D'):		#removed heading
      pass
    else:
      if type not in d:
        d[type]=1
      else:
        d[type]=d[type]+1
  print("Type     Number")
  for type, number in d.items():
    print("{}\t{}".format(type,number))		#even though i gave tab space b/w type and number it is not taking(i missed) 
    
  
  
crimes_halifax()

