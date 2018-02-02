def create_dict(length):
  #length sets the length of the dictionary
  k=range(length) #create a list of integers for keys
  v=[] #create an empty list for values
  seed="asdasdoiasdkjlnadfipu983nf"*length #used to generate text that is always longer than the number of keys
  count=0 #used for the loop generating values
  for i in range(length):
    value=seed[count:count+4]
    v.append(value)
    count+=3
  #print dict(zip(k,v))
  return dict(zip(k,v))

my_dict=create_dict(9)