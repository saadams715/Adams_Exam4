#!/usr/bin/env python3

#definition of functions used in this code
def poss_kmers(string, k_val):
    ''' takes in the sequence string and the substring length and returns the minimum number of possible kmers'''
    
    way_1 = len(string) - k_val + 1
    
    way_2 = 4**k_val
    
    #chooses the minimum of the two different outcomes for calculating possible kmers
    if way_1 < way_2:
        min_p_kmers = way_1
    else:
        min_p_kmers = way_2
    
    #returns the minimum possible kmers value
    return min_p_kmers

def obs_kmers(string,k_val):
    ''' takes in the sequence string and the substring length and returns number of observable kmers'''
    
    #creates 2 different empty arrays that will then be filled
    seq_lst = []
    unique_lst = []

    #This loop just creates all the possible substrings of k length
    for a in range(len(string)):
        b = a + k_val
    
        if b > len(string):
            break
        else:
            seq_lst.append(string[a:b])
            
    #This list now goes through all the substrings and removes any duplicates
    for c in range(len(seq_lst)):
    
        if seq_lst[c] not in unique_lst:
             unique_lst.append(seq_lst[c])
                
    #Returns the number of unique kmers for that k value (so the observed kmers value)            
    return(len(unique_lst))    

def complexity (p, o):
    '''takes in the number of possible kmers and observable kmers and returns the linguistig complexity'''
    
    #calculates the linguistic complexity which is total observed kmers divided by total possible kmers
    ling_complex = o/p
    
    #prints the linguistic complexity value
    print(ling_complex)

def k_table (k,pos_arr, obs_arr,string):
    '''takes in arrays for k, possible kmers, and observable kmers and creates a panda data frame with the associating values'''  
    # creates a dataframe with the k values and their corresmponding observable and possible kmer values
    data = {'k':k,'Observed kmers':obs_arr,'Possible kmers':pos_arr}
    df = pd.DataFrame(data)  
    #outputs our datframe as a csv file. The name of this file will be the sequence 
    df.to_csv(string + '.csv', index=False)
    
    
#Now that the functions are defined the actual process begins here

#This code will only run when this script is being ran and not when it is imported into a test file
if __name__ == '__main__':

    #import pandas and numpy. They will be usefull when it comes to creating a data frame later on.
    import pandas as pd
    import numpy as np
    
    #user inputs name of file they would want to run the code with
    file = open(input("What is the name of the data file?"), 'r')
    
    #sets each line (aka each sequence) to be a string in an array
    sequences = file.readlines()
    revis_sequences = []
    counter = 0

    for i in sequences:
    
        #removes any spaces or non alphabetitical numbers in the sequences
        revis_sequences.append(''.join(filter(str.isalnum, i)))
    
        k = []
        seq_length = len(revis_sequences[counter])
    
        #creates an array with all the k values for that sequence
        for j in range(seq_length):
            k.append(j+1)
        
        #creates the arrays that will be filled with the kmers values for the k values
        pos_arr = []
        obs_arr = []

        t = 1
        
        #iterates through every k value and finds the number of possible and observable kmers and adds them to an array.
        while t < len(k)+1:
    
            pos_arr.append(poss_kmers(revis_sequences[counter],t))
            obs_arr.append(obs_kmers(revis_sequences[counter],t))
        
            t = t +1

        total_obs = 0
        total_pos = 0

        s = 0
    
        #calculates the total number of observable and possible kmers
        while s < 9:
    
            total_obs = total_obs + obs_arr[s]
            total_pos = total_pos + pos_arr[s]
    
            s = s + 1

        #function that calculates the linguistic complexity using the total number of possible and observed kmers. The result is printed out
        complexity(total_pos,total_obs) 
        
        #creates a dataframe with all the associating k, possible kmers, and observable kmers values
        k_table (k,pos_arr, obs_arr,revis_sequences[counter])
        
        counter = counter + 1