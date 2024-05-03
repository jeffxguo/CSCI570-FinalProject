# Open the file in read mode
with open('SampleTestCases/input1.txt', 'r') as file:
    # Read the first string
    first_string = file.readline().strip()

    # Read positions for the first string
    first_positions = []
    line = file.readline().strip()
    while line and line.isdigit():  # Continue until encountering the second string or end of file
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
        modified_string = modified_string[:pos] + base_string + modified_string[pos:]
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