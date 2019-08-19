# --- Levenshtein distance --- #

import numpy as np
import time

def levenshtein(seq1, seq2):
    '''
    Initial function to compute the distance between two strings. 
    Levenshtein distance compute the number of delete, add or replacement to realise on the first string to be exactly like the second (works both ways). 
    
    Input:
        seq1 (str): first string to compare.
        seq2 (str): second string to compare with.
    
    Output:
        matrix[size_x - 1, size_y - 1] (int): Levenshtein distance between the two given strings.
    '''
    size_x = len(seq1) + 1
    size_y = len(seq2) + 1
    matrix = np.zeros ((size_x, size_y))
    for x in range(size_x):
        matrix [x, 0] = x
    for y in range(size_y):
        matrix [0, y] = y

    for x in range(1, size_x):
        for y in range(1, size_y):
            if seq1[x-1] == seq2[y-1]:
                matrix [x,y] = min(
                    matrix[x-1, y] + 1,
                    matrix[x-1, y-1],
                    matrix[x, y-1] + 1
                )
            else:
                matrix [x,y] = min(
                    matrix[x-1,y] + 1,
                    matrix[x-1,y-1] + 1,
                    matrix[x,y-1] + 1
                )
    return (matrix[size_x - 1, size_y - 1])



def levenshtein_upg(seq1, seq2, max_value = 2):
    '''
    Upgraded function to compute the distance between two strings. 
    Levenshtein distance compute the number of delete, add or replacement to realise on the first string to be exactly like the second (works both ways). 
    In this function it's cap to a value decided using 'max_value'. Levenshtein distances above this values are considered as uninteresting.
    
    Input:
        seq1 (str): first string to compare.
        seq2 (str): second string to compare with.
        max_value (int): maximum distance wanted between two string.
    
    Output:
        matrix[size_x - 1, size_y - 1] (int): Levenshtein distance between the two given strings. True values for values below 'max_value' else it's 'max_value' + 1.
    '''
    
    
    if(len(seq1) > len(seq2)): #Keep the shorter word by row, less computation with condition on X axis later.
        size_x = len(seq1) + 1
        size_y = len(seq2) + 1
    else:
        size_y = len(seq1) + 1
        size_x = len(seq2) + 1
    
    if (size_x - size_y) > max_value:
        return max_value + 1
    else:
        matrix = np.zeros ((size_x, size_y))
        for x in range(size_x):
            matrix [x, 0] = x
        for y in range(size_y):
            matrix [0, y] = y

        for x in range(1, size_x):
            if int(matrix[x-1,].max()) > max_value: # Over the threshold, stop computing differences.
                return max_value + 1
            else:
                for y in range(1, size_y):        

                    if seq1[x-1] == seq2[y-1]:
                        matrix [x,y] = min(
                            matrix[x-1, y] + 1,
                            matrix[x-1, y-1],
                            matrix[x, y-1] + 1
                        )
                    else:
                        matrix [x,y] = min(
                            matrix[x-1,y] + 1,
                            matrix[x-1,y-1] + 1,
                            matrix[x,y-1] + 1
                    )
                        
    # Final result if the process was not interrupted prematurely
    return (matrix[size_x - 1, size_y - 1])


start = time.time()
levenshtein('levenshtein', 'distance')
levenshtein('levenshtein', 'distances')
levenshtein('levenstein', 'levenshtein')
print('Standart Levenshtein (no "max_value" in it): ' + str(time.time() - start))

start = time.time()
levenshtein_up('levenshtein', 'distance')
levenshtein_up('levenshtein', 'distances')
levenshtein_up('levenstein', 'levenshtein')
print('Upgraded Levenshtein (with "max_value = 2"): ' + str(time.time() - start))
