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
        self.estimated = self.estimated_insurance_cost()
        self.diff = self.diff_charged_estimated_costs()

    def __repr__(self):
        return "The id of the current costumer is: {id}.".format(id = self.identifier)
    
    def estimated_insurance_cost(self):
        return round(250 * self.age - 128 * self.sex + 370 * self.bmi + 425 * self.children + 24000 * self.smoker - 12500 , 1)
        
    def charged_insurance_cost(self):
        return self.charges

    def diff_charged_estimated_costs(self):
        return round(self.charges - self.estimated, 1)
        
    def has_insurance(self):
        if self.charges > 0:
            return "The costumer id:{id} has a medical insurance.".format(id = self.identifier)
        else:
            return "The costumer id:{id} does not have a medical insurance.".format(id = self.identifier)

    def export_data(self):
        return "{identifier},{age},{sex},{bmi},{children},{smoker},{charges},{estimated},{diff}\n".format(
            identifier = self.identifier, age = self.age, sex = self.sex, bmi = self.bmi, 
            children = self.children, smoker = self.smoker, charges = self.charges, 
            estimated = self.estimated, diff = self.diff      
            )

## test Costumer methods     
# instanciate Costumer   
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


## returns estimated insurance costs by costumer from a list of costumers
def estimated_insurance_cost_by_costumer(costumers_list):
    for costumer in costumers_list:
        print(costumer.estimated)

## function call
#estimated_insurance_cost_by_costumer(costumer_data)


## returns difference between charged and estimated insurance cost by costumer from a list of costumers
def diff_insurance_cost_by_costumer(costumers_list):
    for costumer in costumers_list:
        print(costumer.diff)

## funcation call
#diff_insurance_cost_by_costumer(costumer_data)


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