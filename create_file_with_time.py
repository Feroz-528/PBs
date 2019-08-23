import os
import datetime

filename1 = datetime.datetime.now().strftime("Sample_Out_%d_%m_%Y-%H_%M_%S_.txt")

#print filename1

os.chdir('/home/feroz/results')
f1=open(filename1,'w')
f1.write("HI There!")
f1.close()
