#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Pitson Mwakabila
# DATE CREATED: 08/11/2020                                 
# REVISED DATE: 16/11/2020
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    
    # Creates list of files in directory
    in_files = listdir(image_dir)
    
    # Processes each of the files to create a dictionary where the key
    # is the filename and the value is the picture label (below).
 
    # Creates empty dictionary for the results (pet labels, etc.)
    results_dic = dict()
    
    #items_in_dic = len(results_dic)
   
    #print("\nEmpty Dictionary results_dic - n items=", items_in _dic)
    
   # filenames = ["beagle_0239", "Boston_terrier_02259.jpg"]
   # pet_labels = ["beagle","boston terrier"]
    
    #ilenames = []
    #pet_labels = []
    
    #File names and labels 
    #filename_list = list_dir("pet_images/")
    #filename_list = listdir(image_dir)
    
    ''''
    for fn in range(len(filename_list)):
        filenames.append(filename_list[fn])
        
    #print(filenames)
    
    #pet labels
    for i in  range(len(filenames)):
        filename = filenames[i]
        splited_fn = filename.split("_")
        v = 0
        label_string = []
        while v < int(len(splited_fn)-1):
            label_string.append(splited_fn[v])
            v+=1
            
        pet_labels.append(" ".join(label_string))
    
    #print("\nPrinting labels\n")
    #print(pet_labels)
    
    for idx not in range (0,len(filenames),1):
        if filenames[idx] not in results_dic:
            results_dic[filenames[idx]] = [pet_labels[idx]]
        else:
            print("*** Warning: Keys=", filenames[idx], "already exists in results_dic with value=", results_dicfilenames[idx])
    
    #print("")
    # Replace None with the results_dic dictionary that you created with this
    # function
    '''
    
    # Processes through each file in the directory, extracting only the words
    # of the file that contain the pet image label
    for idx in range(0, len(in_files), 1):
        #print("File name=",in_files[idx])
        # Skips file if starts with . (like .DS_Store of Mac OSX) because it 
        # isn't an pet image file
        if in_files[idx][0] != ".":
           
            # Creates temporary label variable to hold pet label name extracted 
            pet_label = ""

            # TODO: 2a. BELOW REPLACE pass with CODE that will process each 
            #          filename in the in_files list to extract the dog breed 
            #          name from the filename. Recall that each filename can be
            #          accessed by in_files[idx]. Be certain to place the 
            #          extracted dog breed name in the variable pet_label 
            #          that's created as an empty string ABOVE
            #pass
            #pet_label = " ".join(in_files[idx].split("_")[0].strip().lower())
            pet_label = in_files[idx].split("_")[0].strip().lower()

            # If filename doesn't already exist in dictionary add it and it's
            # pet label - otherwise print an error message because indicates 
            # duplicate files (filenames)
            if in_files[idx] not in results_dic:
               results_dic[in_files[idx]] = [pet_label]
              
            else:
                print("** Warning: Duplicate files exist in directory:", 
                     in_files[idx])
 
    # TODO 2b. Replace None with the results_dic dictionary that you created
    # with this function
    #return None
    #print("Printing initial results dic")
    #print(results_dic)
    
    return results_dic
