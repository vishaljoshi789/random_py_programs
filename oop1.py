class Programmer:
    company = 'Microsoft'
    def __init__(self, name, age, gender, number):
       self.name = name
       self.age = age
       self.gender = gender
       self.number = number
    def getInfo(self):
        print(f'\nThe name of employee is {self.name}')
        print(f'The age of employee is {self.age}')
        print(f'The employee works in {self.company}')
        print(f'The gender of employee is {self.gender}')
        print(f'The contect number of employee is {self.number}\n')
vishal = Programmer('Vishal', 15 , 'Male', 6395811181)
somya = Programmer('Somya', 15, 'Female', 9720722602)
vishal.getInfo()
somya.getInfo()
