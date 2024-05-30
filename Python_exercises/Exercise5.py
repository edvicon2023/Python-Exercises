# Exercise 5: Write a script to read from and write to a text file

def read_write_text_file():
    # Write to a text file
    with open('sample.txt', 'w') as file:
        file.write("Hello, this is a sample text file.\n")
        file.write("This is the second line.\n")

    # Read from the text file
    with open('sample.txt', 'r') as file:
        content = file.read()
        print("Reading from the text file:")
        print(content)

read_write_text_file()

# Create a CSV file and write data to it, then read the data

import csv

def write_read_csv():
    # Write to a CSV file
    with open('sample.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Age", "City"])
        writer.writerow(["Alice", 30, "New York"])
        writer.writerow(["Bob", 25, "Los Angeles"])

    # Read from the CSV file
    with open('sample.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

write_read_csv()

# Parse JSON data from a file and write JSON data to a file

import json

def read_write_json():
    data = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }

    # Write JSON data to a file
    with open('sample.json', 'w') as file:
        json.dump(data, file)

    # Read JSON data from a file
    with open('sample.json', 'r') as file:
        data = json.load(file)
        print(data)

read_write_json()
