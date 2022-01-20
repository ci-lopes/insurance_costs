import csv
from costumer import Costumer

class Reader:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.costumer_data = []
    
    def read_costumer_data(self):
        self.costumer_data = []
        with open(self.csv_file) as insurance_data:
            reader = csv.DictReader(insurance_data)
            identifier = 0
            for row in reader:
                costumer = Costumer(identifier, int(row["age"]), self.convert_sex_data(row["sex"]), float(row["bmi"]), 
                int(row["children"]), self.convert_smoker_data(row["smoker"]), round(float(row["charges"]),1))
                #print(costumer.diff)
                self.costumer_data.append(costumer)
                identifier += 1
        return "The data was correctly loaded."

    def convert_sex_data(self, sex_data):
        if sex_data == "female":
            return 1
        if sex_data == "male":
            return 0

    def convert_smoker_data(self, smoker_data):
        if smoker_data == "yes":
            return 1
        if smoker_data == "no":
            return 0

