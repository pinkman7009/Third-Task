import os 

import shutil 

thisdict={
   0:"Normal",
   1:"Hollenhorst Emboli",
   2:"Hypertensive Retinopathy",
   3:"Coat's",
   4:"Branch Retinal Artery Occlusion", 
   5:"Cilio-Retinal Artery Occlusion",  
   6:"Branch Retinal Vein Occlusion",   
   7:"Central Retinal Vein Occlusion",  
   8:"Hemi-Central Retinal Vein Occlusion", 
   9:"Background Diabetic Retinopathy", 
   10:"Proliferative Diabetic Retinopathy",
   11:"Arteriosclerotic Retinopathy",   
   12:"Macroaneurism",
   13:"Choroidal Neovascularization",   
   14:"Others" }

path="D:\\srmth\\thirdtask"

os.chdir(path)

for x in thisdict:
    string=thisdict[x]

    os.mkdir(string)

s="D:\\image files\\"

file=open("D:\\imagefiles.txt", 'r')
for line in file:
    a=line.split()
    img=a[0]
    length=len(a)
    for i in range(length):
        if a[i].isdigit():
            x=int(a[i])
            string=thisdict[x]
            path="D:\\srmth\\thirdtask\\"
            dst=path+string
            src=s+img+".ppm"
            try:
                shutil.copy(src,dst)
            except FileNotFoundError:
                continue;
            

    
    
 