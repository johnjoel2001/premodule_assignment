# import unittest
# import csv
# import os
# from filter_medals import filter_countries

# class TestFilterMedals(unittest.TestCase):

#     def setUp(self):
#         self.input_file = 'test_athletes.csv'
#         self.output_file = 'test_filtered_countries.csv'
        
#         with open(self.input_file, mode='w', newline='') as file:
#             writer = csv.writer(file)
#             writer.writerow(['country_code', 'Gold Medal', 'Silver Medal', 'Bronze Medal'])
#             writer.writerow(['USA', '33', '39', '39'])
#             writer.writerow(['CHN', '33', '27', '23'])
#             writer.writerow(['AUS', '18', '16', '14'])
#             writer.writerow(['JPN', '16', '8', '13'])
#             writer.writerow(['CAN', '7', '6', '11'])  # Should not be included

#     def test_filter_countries(self):
#         filter_countries(self.input_file, self.output_file)
        
#         with open(self.output_file, mode='r') as file:
#             reader = csv.reader(file)
#             rows = list(reader)
#             self.assertEqual(rows[1], ['USA', '33', '39', '39'])
#             self.assertEqual(rows[2], ['CHN', '33', '27', '23'])
#             self.assertEqual(rows[3], ['AUS', '18', '16', '14'])

#     # def tearDown(self):
#     #     os.remove(self.input_file)
#     #     os.remove(self.output_file)

# if __name__ == '__main__':
#     unittest.main()

import unittest
import csv
import os
from filter_medals import filter_countries

class TestFilterMedals(unittest.TestCase):

    def setUp(self):
        self.input_file = 'test_athletes.csv'
        self.output_file = 'test_filtered_countries.csv'

    def create_input_file(self, data):
        with open(self.input_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['country_code', 'Gold Medal', 'Silver Medal', 'Bronze Medal'])
            writer.writerows(data)

    def test_filter_countries_basic(self):
        data = [
            ['USA', '33', '39', '39'],
            ['CHN', '33', '27', '23'],
            ['AUS', '18', '16', '14'],
            ['JPN', '16', '8', '13'],
            ['CAN', '7', '6', '11']  
        ]
        self.create_input_file(data)
        filter_countries(self.input_file, self.output_file)

        with open(self.output_file, mode='r') as file:
            reader = csv.reader(file)
            rows = list(reader)
            self.assertEqual(rows[1], ['USA', '33', '39', '39'])
            self.assertEqual(rows[2], ['CHN', '33', '27', '23'])
            self.assertEqual(rows[3], ['AUS', '18', '16', '14'])

    def test_filter_countries_empty_file(self):
        self.create_input_file([])
        filter_countries(self.input_file, self.output_file)

        with open(self.output_file, mode='r') as file:
            reader = csv.reader(file)
            rows = list(reader)
            self.assertEqual(len(rows), 1)  

    def test_filter_countries_no_valid_data(self):
        data = [
            ['USA', '0', '0', '0'], 
            ['CHN', '0', '0', '0']   
        ]
        self.create_input_file(data)
        filter_countries(self.input_file, self.output_file)

        with open(self.output_file, mode='r') as file:
            reader = csv.reader(file)
            rows = list(reader)
            self.assertEqual(len(rows), 1)  

    def test_filter_countries_with_edge_cases(self):
        data = [
            ['USA', '100', '100', '100'],
            ['CHN', '0', '0', '0'],
            ['AUS', '50', '50', '50'],
            ['JPN', '25', '25', '25'],
            ['CAN', '0', '0', '0']
        ]
        self.create_input_file(data)
        filter_countries(self.input_file, self.output_file)

        with open(self.output_file, mode='r') as file:
            reader = csv.reader(file)
            rows = list(reader)
            self.assertEqual(rows[1], ['USA', '100', '100', '100'])
            self.assertEqual(rows[2], ['AUS', '50', '50', '50'])
            self.assertEqual(rows[3], ['JPN', '25', '25', '25'])

    def tearDown(self):
        try:
            os.remove(self.input_file)
            os.remove(self.output_file)
        except FileNotFoundError:
            pass

if __name__ == '__main__':
    unittest.main()
