import os
from os import listdir
from os.path import isfile, join

my_path = os.getcwd()


onlyfiles = [f for f in listdir(my_path) if isfile(join(my_path, f))]

new_file_name = input("What do you want your file names to be?\n")
starting_number = int(input("From what number you want to start from?\n"))


for file_name in onlyfiles:
    if file_name == "main.py" or file_name=="main.exe" or file_name=="fileRenamer.exe":
        continue
    old_name = os.path.join(my_path,file_name)
  
 
    new_name =  new_file_name +'-'+ str(starting_number)+ '.' + old_name.split(".")[1]
    os.rename(old_name,new_name)
    starting_number+=1

