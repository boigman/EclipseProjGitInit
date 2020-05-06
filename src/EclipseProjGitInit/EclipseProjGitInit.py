'''
Python program to create Git repository from existing Eclipse workspace project. Repository name is assumed to be created in Github and should match the Eclipse project folder name.
Created on May 6, 2020

@author: 08925
'''
import os,sys
import shutil
gitcmds = ['git init','git add .','git commit -m "first commit"','git remote add origin https://github.com/boigman/$PROJNAME$.git','git push origin master']
eclipseProjDir = "C:\\Users\\08925\\Documents\\Eclipse\\workspace"
gitRepoDir = "C:\\Users\\08925\\git"
projName = sys.argv[1]
projPath = eclipseProjDir + "\\" + projName
print ("The current Eclipse project directory is: "+projPath)
repoPath = gitRepoDir + "\\" + projName
if not os.path.exists(repoPath):
    shutil.copytree(projPath, repoPath)
    print (repoPath+ " created")
os.chdir(repoPath)
os.system('echo "#'+projName+'" >Readme.md')
print (repoPath+ "\\Readme.md created")
for cmd in gitcmds:
    print('Executing: '+cmd.replace('$PROJNAME$',projName))
    os.system(cmd.replace('$PROJNAME$',projName))
print (repoPath+ "finished")

    
    
