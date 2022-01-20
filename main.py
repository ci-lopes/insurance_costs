from costumer import Costumer
from read_data import Reader

## csv columns: age,sex,bmi,children,smoker,region,charges

# ## test Costumer methods     
# costumer1 = Costumer(0, 30, 1 , 23.2, 0, 0, 1300)
# print(costumer1)
# print(costumer1.estimated)
# print(costumer1.charges)
# print(costumer1.diff)
# print(costumer1.has_insurance())
# print(costumer1.export_data())

reader = Reader("insurance.csv")
print(reader.read_costumer_data())

costumers = reader.costumer_data


# convert charged insurance cost to a list
def costumer_charges_list(costumer_data):
    charges_list = []
    for costumer in costumer_data:
        charges_list.append(costumer.charges)
    return charges_list

# min and max charges in costumers
print("Minimum insurance cost: {min_charges}$".format(min_charges = min(costumer_charges_list(costumers))))
print("Maximum insurance cost: {max_charges}$".format(max_charges = max(costumer_charges_list(costumers))))

## convert age data in costumers to a list
def costumer_age_list(costumer_data):
    age_list = []
    for costumer in costumer_data:
        age_list.append(costumer.age)
    return age_list

# min and max age in costumers
print("Minimum age of costumers: {min_age}".format(min_age = min(costumer_age_list(costumers))))
print("Maximum age of costumers: {max_age}".format(max_age = max(costumer_age_list(costumers))))

## convert sex data in costumers to a list
def costumer_sex_list(costumer_data):
    sex_list = []
    for costumer in costumer_data:
        sex_list.append(costumer.sex)
    return sex_list

# print number of female and male costumers in costumers
print("Number of female costumers: {females}".format(females = costumer_sex_list(costumers).count(1)))
print("Number of male costumers: {males}".format(males = costumer_sex_list(costumers).count(0)))


## convert bmi data in costumers to a list
def costumer_bmi_list(costumer_data):
    bmi_list = []
    for costumer in costumer_data:
        bmi_list.append(costumer.bmi)
    return bmi_list

# min and max bmi in costumers
print("Minimum bmi: {min_bmi}".format(min_bmi = min(costumer_bmi_list(costumers))))
print("Maximum bmi: {max_bmi}".format(max_bmi = max(costumer_bmi_list(costumers))))

## convert children data in costumers to a list
def costumer_children_list(costumer_data):
    children_list = []
    for costumer in costumer_data:
        children_list.append(costumer.children)
    return children_list

# min and max children in costumers
print("Minimum number of children: {min_children}".format(min_children = min(costumer_children_list(costumers))))
print("Maximum number of children: {max_children}".format(max_children = max(costumer_children_list(costumers))))

## convert smoker data in costumers to a list
def costumer_smoker_list(costumer_data):
    smoker_list = []
    for costumer in costumer_data:
        smoker_list.append(costumer.smoker)
    return smoker_list

# print number of smoker and non-smoker costumers in costumers
print("Number of smokers: {smokers}".format(smokers = costumer_smoker_list(costumers).count(1)))
print("Number of non-smokers: {nonsmokers}".format(nonsmokers = costumer_smoker_list(costumers).count(0)))






# ## write new csv with updated data along with the estimated insurance cost and diff between charged and estimated costs by costumer
# with open("insurance_data_final.csv", "w") as output_csv:
#     fieldnames = "id,age,sex,bmi,children,smoker,charges,estimated_insurance_cost,difference\n"
#     output_csv.write(fieldnames)
#     for costumer in costumer_data:
#         output_csv.write(costumer.export_data())

# ## read output csv
# with open("output.csv") as output_csv:
#     print(output_csv.read())
#     reader = csv.DictReader(output_csv)
#     for row in reader:
#         print(row)