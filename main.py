""" Created by: Leo Martinez III in Spring 2022 """

def project1(seq1, seq2):
    result = "True"
    for a in seq1:
        for b in seq2: # Loop through both sequences to check for duplicates
            if a == b:
                result = "False"
    return result # Returns "True" or "False" based on the for loop results 

print(project1([1, 2, 3, 4, 5], [5, 6, 7, 8, 9])) # Returns "False" because there are duplicate 5's
print(project1([1, 2, 3, 4, 5], [0, 6, 7, 8, 9])) # Returns "True" because there are no duplicates

""" Runtime = O(n^2) , the function is exponential. """
