# Running the code for Exam 4 by Samantha Adams:

## Running the Main Code

This code is designed to run through a file with different gene sequences and for each sequence calculate its length, the number of possible subsequences, the number of observed subsequences, its linguistic complexity, and create a dataframe with all the associating lengths, possible subsequences, and observable subsequences. 

The code is designed to be hands off so the user only has to input the name of the data file when prompted. <b><i> Make sure the data file is in the same directory as the main file. Also include the entire file, meaning if the name has the file type (.txt), i</i></b>

Through the use of for loops the code will go through each sequence. A tool is used to remove any non-alphabet symbols or spaces that could be present in the sequence. This is to obtain an accurate sequence and sequence length. Then an array is created with all the possible lengths (the varying lengths will be known as k) this sequence could have. From there the possible kmers (the number of subsequences with length k) are found along with the number of observable kmers. Two arrays are utilized to keep track of the different kmer values that are calculated. 

To calculate the number of observable kmers for a certain length k, two loops are used. The first one is to find all the subsequences with a length k and then the second loop is used to remove any duplicates. The number of remaining subsequences is the observable kmers value.

There are actually two ways one could calculate the number of possible kmer values, however in this case we want the smaller value. To do this we would calculate the possible kmers value both ways and then determine which one is smaller and return that value. The first calculation that can be done is through subracting k from the sequence length and then adding 1. The second way is through exponentiating 4 to k. The number 4 is used because the sequences being used are only made up of 4 different characters.

Once these values are calculated for each k value, they are added up to produce a total possible kmers value and a total observable kmers value. These totals are used to determine the linguistic complexity of the sequence, which is done through dividing the total observable value by the total possible value. The linguistc complexity value will be printed out into the terminal.

Lastly a dataframe is created to showcase all the associating k, observable kmers, and possible kmers values. The code simply takes in the arrays containg the information and the outputs a csv file. The csv file will have the same name as the sequence.

These were the only the steps for one sequence. Once the steps are complete the code will move onto the next sequence and keep going until there are no more

# What to write in the terminal

<i>Simply write:</i> python3 Adams_Exam4.py

## Doing Unit Tests

The script, test_Adams.py, contains a few tests to ensure the code does work. Since the possible kmers and observable kmers values were known for the sequence ATTTGGATT, this is what will be checked. The tests check the functions that in the main code file that calculate the possible and observable kmers values for each k value. In this case, k can have value from 1 to 9. 

<b><i> Make sure the test file is in the same directory as the main file </i></b>