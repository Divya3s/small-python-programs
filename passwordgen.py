import random
import array

# Define the possible characters in the password
MAX_LEN = int(input("Enter maximum length of the password to generate."))

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']

# Combine all characters
COMBINED_LIST = DIGITS + LOCASE_CHARACTERS + UPCASE_CHARACTERS + SYMBOLS

# Randomly select at least one character from each character set
rand_digit = random.choice(DIGITS)
rand_lower = random.choice(LOCASE_CHARACTERS)
rand_upper = random.choice(UPCASE_CHARACTERS)
rand_symbol = random.choice(SYMBOLS)

# Combine the randomly selected characters
temp_pass = rand_digit + rand_lower + rand_upper + rand_symbol

# Fill the remaining characters randomly from the combined list
for x in range(MAX_LEN - 4):
    temp_pass = temp_pass + random.choice(COMBINED_LIST)

# Convert temporary password into array and shuffle to ensure random order
temp_pass_list = array.array('u', temp_pass)
random.shuffle(temp_pass_list)

# Create the final password string
password = "".join(temp_pass_list)

print(f"Generated password: {password}")
