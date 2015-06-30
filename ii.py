string=input("enter the string")
co={}
for char in string:
 if char in co.keys():
    co[char] +=1
 else:
    co[char] =1
for j in co:   
  
 print ('%s' %(j))
 print ('*\n'*co[j],)
