import json

class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

# Read the JSON file and convert it to a Python dictionary
with open('employee.json', 'r') as f:
    data = json.load(f)

# Create a list of Employee objects from the dictionary
employees = [Employee(e['Name'], e['DOB'], e['Height'], e['City'], e['State']) for e in data['Employees']]

# Print the list of Employee objects
for employee in employees:
    print(employee.name, employee.dob, employee.height, employee.city, employee.state)
