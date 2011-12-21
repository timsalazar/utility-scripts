import os

def create_directories():
    '''creates the generic asset structure for design files'''
    directory_list = [ "docs", "final-graphics", "mockups", "mockups/archive", "mockups/archive/01", "mockups/flattened-files", "mockups/layered-files", "prototypes", "resources", "final-graphics/layered-files", "resources/screencaps" ]

    for i in directory_list:
        os.makedirs(i)
        os.chmod(i, 777)

    print "The following directories were created: ", ", ".join(directory_list)
 
if __name__ == "__main__":
    create_directories()
  
    

    
   
 
