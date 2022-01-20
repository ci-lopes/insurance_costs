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