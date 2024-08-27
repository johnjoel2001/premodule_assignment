# import csv

# def filter_countries(input_path, output_path):
#     results = []

#     # Open and read the input CSV file
#     with open(input_path, mode='r', newline='') as file:
#         reader = csv.DictReader(file)
        
#         # Process each row in the CSV file
#         for record in reader:
#             country = record['country_code']
#             gold = int(record['Gold Medal'])
#             silver = int(record['Silver Medal'])
#             bronze = int(record['Bronze Medal'])

#             # Check if all medal counts are greater than 10
#             if gold > 10 and silver > 10 and bronze > 10:
#                 results.append([country, gold, silver, bronze])

#     # Write the filtered results to the output CSV file
#     with open(output_path, mode='w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(['Country', 'Gold', 'Silver', 'Bronze'])
#         writer.writerows(results)

# # Specify your input and output file paths here
# input_file_path = 'medals_total.csv'
# output_file_path = 'filtered_countries.csv'

# # Call the function with the specified file paths
# filter_countries(input_file_path, output_file_path)

import csv
import argparse

def filter_countries(input_file, output_file):
    filtered_countries = []

    with open(input_file, mode='r', newline='') as infile:
        reader = csv.DictReader(infile)
        
        for row in reader:
            country = row['country_code']
            gold = int(row['Gold Medal'])
            silver = int(row['Silver Medal'])
            bronze = int(row['Bronze Medal'])

            if gold > 10 and silver > 10 and bronze > 10:
                filtered_countries.append([country, gold, silver, bronze])

    with open(output_file, mode='w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['Country', 'Gold', 'Silver', 'Bronze'])
        writer.writerows(filtered_countries)

def main():
    parser = argparse.ArgumentParser(description='Filter countries based on the number of medals.')
    parser.add_argument('input_file', help='Path to the input CSV file')
    parser.add_argument('output_file', help='Path to the output CSV file')
    
    args = parser.parse_args()
    filter_countries(args.input_file, args.output_file)

if __name__ == '__main__':
    main()


