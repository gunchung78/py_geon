from os import system, name 
import sys
sys.path.append("..")

def consoleClear():

   # for windows 
   if name == 'nt': 
       _ = system('cls') 
  
   # for mac and linux(here, os.name is 'posix') 
   else: 
       _ = system('clear') 