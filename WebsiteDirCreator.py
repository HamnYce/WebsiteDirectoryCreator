import os
from os import chdir,mkdir
chdir(os.path.join(os.path.join(os.environ['USERPROFILE']), 'desktop'))

mkdir("ProjectName")
chdir("ProjectName")


open("index.html",'w')


mkdir("graphics") 
mkdir("styles")
mkdir("scripts")


chdir("styles")
open("stylesheet.css",'w')


chdir('..')
chdir("scripts")
open("sample-script.js",'w')



