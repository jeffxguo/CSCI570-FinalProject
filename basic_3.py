import time
import psutil
import math
import sys
file = sys.argv[1]
out = sys.argv[2]
with open(file, 'r') as file:
    first_string = file.readline().strip()
    first_positions = []
    line = file.readline().strip()
    while line and  line.isdigit():  
        first_positions.extend(map(int, line.split(',')))
        line = file.readline().strip()
    second_string = line
    second_positions = []
    line = file.readline().strip()
    while line:
        second_positions.extend(map(int, line.split(',')))
        line = file.readline().strip()
def insert_string_at_positions(base_string, positions):
    modified_string = base_string
    for pos in positions:
        modified_string = modified_string[:pos+1] + modified_string + modified_string[pos+1:]
    return modified_string
modified_first_string = insert_string_at_positions(first_string, first_positions)
modified_second_string = insert_string_at_positions(second_string, second_positions)
p_gap = 30
table = {
    'A': {'A': 0, 'C': 110, 'G': 48, 'T': 94},
    'C': {'A': 110, 'C': 0, 'G': 118, 'T': 48},
    'G': {'A': 48, 'C': 118, 'G': 0, 'T': 110},
    'T': {'A': 94, 'C': 48, 'G': 110, 'T': 0}
}


def simple_version(x:str, y:str, Pxy: dict, p_gap:int):
    m = len(x)
    n = len(y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    i = 0
    j = 0
    for i in range(m + 1):
        dp[i][0] = i * p_gap
    for i in range(n+1):
        dp[0][i] = i * p_gap

    i = 1
    for i in range(1,len(x)+1):
        for j in range(1,len(y)+1):
            if x[i-1]==y[j-1]:
                min_value=min(dp[i-1][j-1],
                              dp[i-1][j]+ p_gap,
                              dp[i][j-1]+p_gap)
                dp[i][j]=min_value
            else:
                min_value= min(dp[i - 1][j - 1]+Pxy[x[i - 1]][y[j - 1]],
                                dp[i - 1][j] + p_gap,
                                dp[i][j - 1] + p_gap)
                dp[i][j]=min_value

    total_length = n + m   
    i = m
    j = n
     
    xpos = total_length
    ypos = total_length
 
   
    xfinal = [0] * (total_length + 1)
    yfinal = [0] * (total_length + 1)
     
    pen = 0
    while not (i == 0 or j == 0):
        if x[i - 1] == y[j - 1]:        
            xfinal[xpos] = ord(x[i - 1])
            yfinal[ypos] = ord(y[j - 1])
            xpos -= 1
            ypos -= 1
            i -= 1
            j -= 1
        elif (dp[i - 1][j - 1] + Pxy[x[i-1]][y[j-1]]) == dp[i][j]:
         
            xfinal[xpos] = ord(x[i - 1])
            yfinal[ypos] = ord(y[j - 1])
            pen = pen + Pxy[x[i-1]][y[j-1]]
            xpos -= 1
            ypos -= 1
            i -= 1
            j -= 1
         
        elif (dp[i - 1][j] + p_gap) == dp[i][j]:
            xfinal[xpos] = ord(x[i - 1])
            yfinal[ypos] = ord('_')
            pen = pen + p_gap
            xpos -= 1
            ypos -= 1
            i -= 1
         
        elif (dp[i][j - 1] + p_gap) == dp[i][j]:        
            xfinal[xpos] = ord('_')
            yfinal[ypos] = ord(y[j - 1])
            pen = pen + p_gap
            xpos -= 1
            ypos -= 1
            j -= 1
         
 
    while xpos > 0:
        if i > 0:
            i -= 1
            xfinal[xpos] = ord(x[i])
            xpos -= 1
        else:
            xfinal[xpos] = ord('_')
            xpos -= 1
     
    while ypos > 0:
        if j > 0:
            j -= 1
            yfinal[ypos] = ord(y[j])
            ypos -= 1
        else:
            yfinal[ypos] = ord('_')
            ypos -= 1
    id = 1
    i = total_length
    while i >= 1:
        if (chr(yfinal[i]) == '_') and chr(xfinal[i]) == '_':
            id = i + 1
            break
         
        i -= 1
    i = id
    x_seq = ""
    while i <= total_length:
        x_seq += chr(xfinal[i])
        i += 1
    i = id
    y_seq = ""
    while i <= total_length:
        y_seq += chr(yfinal[i])
        i += 1
    return dp[m][n], x_seq,y_seq
def process_memory(call_algorithm):
    process = psutil.Process()
    memory_info = process.memory_info()
    memory_consumed = int(memory_info.rss / 1024)
    return memory_consumed
def time_wrapper(call_algorithm):
    start_time = time.time()
    call_algorithm()
    end_time = time.time()
    time_taken = (end_time - start_time) * 1000
    return time_taken
alignment_result = simple_version(modified_first_string, modified_second_string, table, p_gap)
execution_time = time_wrapper(lambda: simple_version(modified_first_string, modified_second_string, table, p_gap))
memory_used = process_memory(lambda: simple_version(modified_first_string, modified_second_string, table, p_gap))
score, x_seq, y_seq = alignment_result
with open(out, 'w') as file:
    file.write(f"{score}\n")
    file.write(f"{x_seq}\n")
    file.write(f"{y_seq}\n")
    file.write(f"{execution_time}\n")
    file.write(f"{memory_used} \n")

    
    