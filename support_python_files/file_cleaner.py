import os 
  
# Function to rename multiple files 
def main(): 
    path = "social_distancing_detector/data/images/mv/"
  
    for count, filename in enumerate(os.listdir(path)): 
        dst ="tired" + str(count) + ".jpeg"
        src =path+ filename 
        dst =path+ dst 
          
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 