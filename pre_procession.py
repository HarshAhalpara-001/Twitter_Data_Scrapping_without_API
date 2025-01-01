filename = "C:\\0_DATA\\Environments\\Scrapping\\fetched_data_of_BMW_from_tweeter.txt"
import csv

# Specify the input and output file paths
input_file = filename  # Replace with the path to your text file
output_file = "tweets.csv"  # Path for the output CSV file

# Read data from the text file
with open(input_file, mode='r', encoding='utf-8') as file:
    data = file.read()

# Split the data into entries based on the separator
entries = data.split("--------------------------------------------------------------------")
parsed_data = []

# Parse each entry
for entry in entries:
    lines = entry.strip().split("\n")
    if len(lines) < 4:  # Skip empty or incomplete entries
        continue
    author_name = lines[0].strip()
    handle = lines[1].strip()
    date = lines[2].strip("·").strip()
    content = " ".join(lines[3:]).strip()
    parsed_data.append([author_name, handle, date, content])

# Write the parsed data into a CSV file
with open(output_file, mode='w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    # Write headers
    writer.writerow(["Author Name", "Handle", "Date", "Content"])
    # Write the data
    writer.writerows(parsed_data)

print(f"Data has been successfully converted to {output_file}")
