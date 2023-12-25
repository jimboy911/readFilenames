#read_filenames.py
#this program reads the filename in the specific folder in the root directory of the python file and then deletes it
#should work for any operating system

import os #for file checking and manipulation

path = os.path.abspath("ENTER FOLDER NAME HERE") #gets the full path of the folder in the directory that you're running the program from

get_files = os.listdir(path) #looks at all the files in that folder and saves their names in a list
filename = get_files[0] #gets the filename of the first file in the index

#grab the full path of the file
full_path = path + "/" + filename

#how to delete that file
os.remove(full_path)