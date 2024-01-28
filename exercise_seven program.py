# Hello! This program finds how many times substring “Emma” appears in the given string.

# pseudocode

# Define a function to count the number of occurrences of the substring "Emma" in a given string
def count_emma(statement):
    print("Given String: ", statement)
    count = 0
    for i in range(len(statement) - 1):
        # Check if the substring "Emma" appears at the current position
        if statement[i: i + 4] == 'Emma':
            # If it does, increment the count by 1
            count += 1
    return count

# Call the function with a test string and print the result
count = count_emma("Emma is good developer. Emma is a writer")
print("The word Emma appeared for about ", count, "times")
