Hi Ma'am,

I want to give a brief overview of the work which I have done as per the instructions in the assignment.

OPERATION ON A CSV FILE

(1) I have used medals_total csv file. I found this dataset on Kaggle which that showcases the medals (Gold, Silver, and Bronze) won by various countries during the Paris 2024 Olympics. 
(2) The operation I performed on the dataset is to filter out the countries that have won more than 10 Gold medals, 10 Silver medals, and 10 Bronze medals.
(3) The filtered countries, along with their medal tallies, were written to a new CSV file.

UNIT TESTING

(1) Basic Filtering: Ensures that countries with more than 10 Gold, 10 Silver, and 10 Bronze medals are correctly filtered.

(2) Empty File Handling: Verifies that the package handles empty input files gracefully, producing only a header in the output file.

(3) Edge Cases: Tests the package with edge cases, such as no valid countries meeting the criteria or countries with extreme medal counts.

(4) No Valid Data: Checks how the package behaves when no countries meet the filtering criteria

PACKAGING INTO A CLI TOOL

PACKAGE NAME: filter-medals

OVERVIEW

filter-medals is a Python package designed to filter information from a dataset of Olympic medal counts. Specifically, it filters countries that have won more than 10 Gold, 10 Silver, and 10 Bronze medals. The filtered data is then written to a new CSV file which makes it easier to analyze the top-performing countries.

STEPS TO INSTALL THE PACKAGE

1)  Clone the repository
2)  To install the package, Run the oommand: pip install .
3)  To use the package via the command line, run the command: filter-medals input_file.csv output_file.csv. In our case, the input file is medals_total.csv, and the output file can be named as desired. I'll name it filtered_countries.csv, so the command would be: filter-medals medals_total.csv filtered_countries.csv
4)  To run the unit tests, run the command: python -m unittest discover


