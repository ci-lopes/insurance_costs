with open("insurance.csv") as insurance_data:
    print(insurance_data.read())

# age,sex,bmi,children,smoker,region,charges
class Costumer:
    def __init__(age, sex, children, smoker):
        self.age = age
        self.sex = sex
        self.children = children
        self.smoker = smoker

