import csv
from costumer import Costumer

## csv columns: age,sex,bmi,children,smoker,region,charges

## test Costumer methods     
costumer1 = Costumer(0, 30, 1 , 23.2, 0, 0, 1300)
print(costumer1)
print(costumer1.estimated)
print(costumer1.charges)
print(costumer1.diff)
print(costumer1.has_insurance())
print(costumer1.export_data())


## convert sex and smoker columns to bool
def convert_sex_data(sex_data):
    if sex_data == "female":
        sex_data = 1
        return sex_data
    if sex_data == "male":
        sex_data = 0
        return sex_data
#print(convert_sex_data("male"))

def convert_smoker_data(smoker_data):
    if smoker_data == "yes":
        smoker_data = 1
        return smoker_data
    if smoker_data == "no":
        smoker_data = 0
        return smoker_data
#print(convert_smoker_data("no"))


## open csv file and read it as a dict 
# create costumer_data variable that stores all costumers data
costumer_data = []
with open("insurance.csv") as insurance_data:
    reader = csv.DictReader(insurance_data)
    identifier = 0
    for row in reader:
        costumer = Costumer(identifier, int(row["age"]), convert_sex_data(row["sex"]), float(row["bmi"]), 
        int(row["children"]), convert_smoker_data(row["smoker"]), round(float(row["charges"]),1))
        #print(costumer.diff)
        costumer_data.append(costumer)
        identifier = identifier + 1
















## write new csv with updated data along with the estimated insurance cost and diff between charged and estimated costs by costumer
with open("insurance_data_final.csv", "w") as output_csv:
    fieldnames = "id,age,sex,bmi,children,smoker,charges,estimated_insurance_cost,difference\n"
    output_csv.write(fieldnames)
    for costumer in costumer_data:
        output_csv.write(costumer.export_data())

## read output csv
with open("output.csv") as output_csv:
    print(output_csv.read())
    reader = csv.DictReader(output_csv)
    for row in reader:
        print(row)