import csv

## csv columns: age,sex,bmi,children,smoker,region,charges

## create Costumer class
class Costumer:
    def __init__(self, identifier, age, sex, bmi, children, smoker, charges):
        self.identifier = identifier
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.children = children
        self.smoker = smoker
        self.charges = charges
        
    def __repr__(self):
        return "The id of the current costumer is: {id}.".format(id = self.identifier)
    
    def estimated_insurance_cost(self):
        self.estimated = 250 * self.age - 128 * self.sex + 370 * self.bmi + 425 * self.children + 24000 * self.smoker - 12500
        return self.estimated
    
    def charged_insurance_cost(self):
        return self.charges

    def diff_charged_estimated_costs(self):
        self.diff = self.charges - self.estimated
        return self.diff
    
    def has_insurance(self):
        if self.charges > 0:
            return "The costumer id:{id} has a medical insurance.".format(id = self.identifier)
        else:
            return "The costumer id:{id} does not have a medical insurance.".format(id = self.identifier)

## test Costumer methods     
# instanciate Costumer   
costumer1 = Costumer(0, 30, 1 , 23.2, 0, 0, 1300)
print(costumer1)
print(costumer1.estimated_insurance_cost())
print(costumer1.charges)
print(costumer1.diff_charged_estimated_costs())
print(costumer1.has_insurance())



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
with open("insurance.csv") as insurance_data:
    reader = csv.DictReader(insurance_data)
    identifier = 0
    for row in reader:
        costumer = Costumer(identifier, row["age"], convert_sex_data(row["sex"]), row["bmi"], 
        row["children"], convert_smoker_data(row["smoker"]), row["charges"])
        #print(costumer.charges)
        
        identifier = identifier + 1

