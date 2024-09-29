print ("Hello World!!")
###################################################
# CMSC-5723 Machine Learning Programming Project
# Professor: Dr. Robert Nix
# Author: Lori Reynolds
# Overview:
###################################################

# 1. Ask the user if they want to train the model.
#    a. If they do:
#       i. Prompt the user for the training data file
#       ii. Build the model
#       iii. Store the model for next run
#    b. If they don’t:
#       i. Load the stored model from disk
# 2. Prompt the user for the test data file
# 3. For each instance in the test data file, output (to standard output) that instance followed
#    by the classification your model gives it.

def main():
    do_train_model = input("To train or not to train? Aka, Do you want to\
                            train the model? (yes/no): ")
    if do_train_model.lower() in ["yes", "y"]:
        training_data_file_name = input("To train! Please provide the training data file: ")
    else:
        print("Loading the stored model from the disk...")

    return