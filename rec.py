import os,sys



dirname=os.path.dirname(os.path.realpath(sys.argv[0]))

list1= dirname.split('/')
print list1[-1]

#for root, dirs, files in os.walk(".", topdown=True):
	#print dirs
#while 1:
d={}
f={}
l=[]
l1=[]
for root,dirs ,files in os.walk(".", topdown=True):
	
			#print root,'\n'
			
			#print dirs,'\n'
			#print files,'\n'
	for z in dirs:
		d['dirs']=z
	print d	
		
	for y in files:
		f['files']=y
	print f
	
					 
						

			
	
	
	#for i in dirs:
'''for dirs in os.walk(".", topdown=True):
		if dirs!='/':
			l= dirs
			print '\t',l'''
		#else:
			#print '\n
		
	#for name in files:
		
		#print '\t',name
	
