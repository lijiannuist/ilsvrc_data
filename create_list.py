import os
import numpy
datadir="/media/lijian/G/train"
root_dir="/home/lijian/caffe-master/data/ilsvrc10"
train_list_dir=root_dir+'/train_list.txt'
train_list_file=open(train_list_dir,'w')
lable_dir=root_dir+'/lable.txt'
lable_file = open(lable_dir, 'w')
lable =[]
lablenum =-1
train_list=[] 
for classname in os.listdir(datadir):
    #lable.append(classname)
    lable_file.write(classname + '\n')
    imagedir=datadir+'/'+classname
    lablenum=lablenum + 1
    testnum= 0
    for eachimage in os.listdir(imagedir):
       judgejpg=eachimage.split('.')
       testnum =testnum +1
       if judgejpg[len(judgejpg)-1] == 'JPEG' and testnum >10:
         eachimagedir= classname +'/' + eachimage + ' ' + str(lablenum) +'\n'
        # train_list.append(eachimagedir)
         train_list_file.write(eachimagedir)
#print train_list[2]
train_list_file.close()
lable_file.close()
#numpy.savetxt(train_list_file,train_list)
#numpy.savetxt(lable_dir,lable)

