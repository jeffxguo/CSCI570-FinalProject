# Open the file in read mode
import numpy as np
with open('Project/SampleTestCases/input5.txt', 'r') as file:
    # Read the first string
    first_string = file.readline().strip()
    
    # Read positions for the first string
    first_positions = []
    line = file.readline().strip()
    while line and  line.isdigit():  # Continue until encountering the second string or end of file
        first_positions.extend(map(int, line.split(',')))
        line = file.readline().strip()

    # Read the second string
    second_string = line

    # Read positions for the second string
    second_positions = []
    line = file.readline().strip()
    while line:  # Continue until end of file
        second_positions.extend(map(int, line.split(',')))
        line = file.readline().strip()

# Define a function to insert string at positions
def insert_string_at_positions(base_string, positions):
    modified_string = base_string
    for pos in positions:
        modified_string = modified_string[:pos+1] + modified_string + modified_string[pos+1:]
    return modified_string

# Insert strings at positions
modified_first_string = insert_string_at_positions(first_string, first_positions)
modified_second_string = insert_string_at_positions(second_string, second_positions)

# Print the modified strings
print("Modified First String:", modified_first_string)
print("Modified Second String:", modified_second_string)
p_gap = 30
table = {
    'A': {'A': 0, 'C': 110, 'G': 48, 'T': 94},
    'C': {'A': 110, 'C': 0, 'G': 118, 'T': 48},
    'G': {'A': 48, 'C': 118, 'G': 0, 'T': 110},
    'T': {'A': 94, 'C': 48, 'G': 110, 'T': 0}
}


def simple_version(x:str, y:str, Pxy: dict, pgap:int):
    m = len(x)
    n = len(y)
    dp = np.zeros([m+1,n+1], dtype=int) #int dp[m+1][n+1] = {0};
    i = 0
    j = 0
    # initialising the table
    dp[0:(m+1),0] = [ i * pgap for i in range(m+1)]
    dp[0,0:(n+1)] = [ i * pgap for i in range(n+1)]

    i = 1
    for i in range(1,len(x)+1):
        for j in range(1,len(y)+1):
            if x[i-1]==y[j-1]:
                min_value=min(dp[i-1][j-1],
                              dp[i-1][j]+ pgap,
                              dp[i][j-1]+pgap)
                dp[i][j]=min_value
            else:
                min_value= min(dp[i - 1][j - 1]+Pxy[x[i - 1]][y[j - 1]],
                                dp[i - 1][j] + pgap,
                                dp[i][j - 1] + pgap)
                dp[i][j]=min_value

    l = n + m   # maximum possible length
    i = m
    j = n
     
    xpos = l
    ypos = l
 
    # Final answers for the respective strings
    xans = np.zeros(l+1, dtype=int)
    yans = np.zeros(l+1, dtype=int)
     
    pen = 0
    while not (i == 0 or j == 0):
        #print(f"i: {i}, j: {j}")
        if x[i - 1] == y[j - 1]:        
            xans[xpos] = ord(x[i - 1])
            yans[ypos] = ord(y[j - 1])
            xpos -= 1
            ypos -= 1
            i -= 1
            j -= 1
        elif (dp[i - 1][j - 1] + Pxy[x[i-1]][y[j-1]]) == dp[i][j]:
         
            xans[xpos] = ord(x[i - 1])
            yans[ypos] = ord(y[j - 1])
            pen = pen + Pxy[x[i-1]][y[j-1]]
            xpos -= 1
            ypos -= 1
            i -= 1
            j -= 1
         
        elif (dp[i - 1][j] + pgap) == dp[i][j]:
            xans[xpos] = ord(x[i - 1])
            yans[ypos] = ord('_')
            pen = pen + pgap
            xpos -= 1
            ypos -= 1
            i -= 1
         
        elif (dp[i][j - 1] + pgap) == dp[i][j]:        
            xans[xpos] = ord('_')
            yans[ypos] = ord(y[j - 1])
            pen = pen + pgap
            xpos -= 1
            ypos -= 1
            j -= 1
         
 
    while xpos > 0:
        if i > 0:
            i -= 1
            xans[xpos] = ord(x[i])
            xpos -= 1
        else:
            xans[xpos] = ord('_')
            xpos -= 1
     
    while ypos > 0:
        if j > 0:
            j -= 1
            yans[ypos] = ord(y[j])
            ypos -= 1
        else:
            yans[ypos] = ord('_')
            ypos -= 1
 
    # Since we have assumed the answer to be n+m long,
    # we need to remove the extra gaps in the starting
    # id represents the index from which the arrays
    # xans, yans are useful
    id = 1
    i = l
    while i >= 1:
        if (chr(yans[i]) == '_') and chr(xans[i]) == '_':
            id = i + 1
            break
         
        i -= 1
 
    # Printing the final answer
    print(f"Minimum Penalty in aligning the genes = {dp[m][n]}")
    print("The aligned genes are:")    
    # X
    i = id
    x_seq = ""
    while i <= l:
        x_seq += chr(xans[i])
        i += 1
    print(f"X seq: {x_seq}")
 
    # Y
    i = id
    y_seq = ""
    while i <= l:
        y_seq += chr(yans[i])
        i += 1
    print(f"Y seq: {y_seq}")
simple_version(modified_first_string,modified_second_string,table,p_gap)