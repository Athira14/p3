string=input("enter the string")
count={}
for char in string:
 if char in count.keys():
    count[char] +=1
 else:
    count[char] =1
for i in count:   
  
 print ('%s' %(i))
 print ('*\n'*count[i],)
