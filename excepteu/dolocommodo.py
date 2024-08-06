import re

# Define the pattern you want to search for
pattern = r'\d{3}-\d{3}-\d{4}'  # Example pattern for a phone number

# Search for the pattern in the string
matches = re.findall(pattern, soup_string)

# Print the matches
for match in matches:
    print(match)
