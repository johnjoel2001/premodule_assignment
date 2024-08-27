import csv
import argparse

def filter_countries(input_file, output_file):
    filtered_countries = []

    with open(input_file, mode='r', newline='') as infile:
        reader = csv.DictReader(infile)
        
        for row in reader:    # Lopping through the input dataset
            country = row['country_code']
            gold = int(row['Gold Medal'])
            silver = int(row['Silver Medal'])
            bronze = int(row['Bronze Medal'])

            if gold > 10 and silver > 10 and bronze > 10:  # Filtering condition
                filtered_countries.append([country, gold, silver, bronze])

    with open(output_file, mode='w', newline='') as outfile:  # Writing the filtered output in a new csv file
        writer = csv.writer(outfile)
        writer.writerow(['Country', 'Gold', 'Silver', 'Bronze'])
        writer.writerows(filtered_countries)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    parser.add_argument('output_file')
    
    args = parser.parse_args()
    filter_countries(args.input_file, args.output_file)

if __name__ == '__main__':
    main()

