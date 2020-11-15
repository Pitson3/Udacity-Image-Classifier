#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#                                                                             
# PROGRAMMER: Pitson Mwakabila
# DATE CREATED: 10/11/2020                                
# REVISED DATE: 12/11/2020
# PURPOSE: Create a function classify_images that uses the classifier function 
#          to create the classifier labels and then compares the classifier 
#          labels to the pet image labels. This function inputs:
#            -The Image Folder as image_dir within classify_images and function 
#             and as in_arg.dir for function call within main. 
#            -The results dictionary as results_dic within classify_images 
#             function and results for the functin call within main.
#            -The CNN model architecture as model wihtin classify_images function
#             and in_arg.arch for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           classifier label as the item at index 1 of the list and the comparison 
#           of the pet and classifier labels as the item at index 2 of the list.
#
##
# Imports classifier function for using CNN to classify images 
from classifier import classifier 
from os import listdir
import ast

# TODO 3: Define classify_images function below, specifically replace the None
#       below by the function definition of the classify_images function. 
#       Notice that this function doesn't return anything because the 
#       results_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.
# 
def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels with classifier function, compares pet labels to 
    the classifier labels, and adds the classifier label and the comparison of 
    the labels to the results dictionary using the extend function. Be sure to
    format the classifier labels so that they will match your pet image labels.
    The format will include putting the classifier labels in all lower case 
    letters and strip the leading and trailing whitespace characters from them.
    For example, the Classifier function returns = 'Maltese dog, Maltese terrier, Maltese' 
    so the classifier label = 'maltese dog, maltese terrier, maltese'.
    Recall that dog names from the classifier function can be a string of dog 
    names separated by commas when a particular breed of dog has multiple dog 
    names associated with that breed. For example, you will find pet images of
    a 'dalmatian'(pet label) and it will match to the classifier label 
    'dalmatian, coach dog, carriage dog' if the classifier function correctly 
    classified the pet images of dalmatians.
     PLEASE NOTE: This function uses the classifier() function defined in 
     classifier.py within this function. The proper use of this function is
     in test_classifier.py Please refer to this program prior to using the 
     classifier() function to classify images within this function 
     Parameters: 
      images_dir - The (full) path to the folder of images that are to be
                   classified by the classifier function (string)
      results_dic - Results Dictionary with 'key' as image filename and 'value'
                    as a List. Where the list will contain the following items: 
                  index 0 = pet image label (string)
                --- where index 1 & index 2 are added by this function ---
                  NEW - index 1 = classifier label (string)
                  NEW - index 2 = 1/0 (int)  where 1 = match between pet image
                    and classifer labels and 0 = no match between labels
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
     Returns:
           None - results_dic is mutable data type so no return needed.         
    """
    
    filenames = []
    
    filename_list = listdir(images_dir)
    
    
    for fn in range(len(filename_list)):
        filenames.append(filename_list[fn])
    
    classifier_labels = []
    
    classifier_label_set = open("imagenet1000_clsid_to_human.txt")
    
    set_label = ast.literal_eval(classifier_label_set.read())
    
    for i in range(0,len(set_label),1):
        classifier_labels.append(set_label[i].strip().lower())
        #classifier_labels.append(set_label[i])
    
    #print(set_label)
    #print(classifier_labels)
    
    
    #for sl in range(0,len(set_label),1):
    #for sl in set_label:
       # print(sl)
    
    #print(set_label)
    
    #Pet labels 
    pet_labels = []
    #Iterating through results_dic to get labels 
    for idx in results_dic:
        pet_labels.append(results_dic[idx][0].strip().lower())
        #print(results_dic[idx][0])
     
    #print("Printing Pet Labels")
    #print(pet_labels)
    #Pet labels is dog 
    pet_label_is_dog = []
    
    #classifier label as dog 
    classifier_label_is_dog = []
    
    #Populate a list for matching dogs
    for i in range(len(filenames)):
        if(int(len(filenames)-len(pet_label_is_dog))==1):
            pet_label_is_dog.append(0)
            #classifier_label_is_dog.append(0)
            
        else:
            pet_label_is_dog.append(1)
            #classifier_label_is_dog.append(1)
    
    for i in range(len(filenames)):
        if(int(len(filenames)-len(classifier_label_is_dog))==1):
            #pet_label_is_dog.append(0)
            classifier_label_is_dog.append(0)
            
        else:
            #pet_label_is_dog.append(1)
            classifier_label_is_dog.append(1)
        
        
   
    #Modifying the dictionary with both labels and indicates if they match 
    
    for idx in range(0,len(filenames),1):
        #print(filenames[idx])
        #
        if filenames[idx] in results_dic:
            results_dic[filenames[idx]] = [pet_labels[idx], classifier_labels[idx]]
            #print(results_dic[filenames[idx]])
            #print(pet_labels[idx])
            #print(classifier_labels[idx])
            #print(filenames[idx])
        #print("Pet Labels Against Classifier Labels");
        #print("Dog " + pet_labels[idx] + " : Classifier " + classifier_labels[idx])
       
        if pet_labels[idx] in classifier_labels[idx]:
            results_dic[filenames[idx]].append(1)
            #classifier_label_is_dog.append(1)
        else:
            results_dic[filenames[idx]].append(0)
            #classifier_label_is_dog.append(0)
           
    
    """
    for idx in range(len(filenames)):
        results_dic[filenames[idx]].extend([pet_label_is_dog[idx], classifier_label_is_dog[idx]])
    #print(results_dic)
    
    # Iterates through the list to print the results for each filename
   
    for key in results_dic:
        print("\nFilename=", key, "\npet_image Label=", results_dic[key][0],
          "\nClassifier Label=", results_dic[key][1], "\nmatch=",
          results_dic[key][2], "\nImage is dog=", results_dic[key][3],
          "\nClassifier is dog=", results_dic[key][4])
        # Provides classifications of the results
        if sum(results_dic[key][2:]) == 3:
            print("*Breed Match*")
        if sum(results_dic[key][3:]) == 2:
            print("*Is-a-Dog Match*")
        if sum(results_dic[key][3:]) == 0 and results_dic[key][2] == 1:
            print("*NOT-a-Dog Match*")
     
    #print(classifier_labels)
    """
    #print(results_dic)
    None 