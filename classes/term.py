class Term():

    def __init__(self, name, start_date, end_date):
        self.name       = name
        self.start_date = start_date
        self.end_date   = end_date
        self.members    = []
    
    def add_member(self, person):
        self.members.append(person)

    def print_info(self):
        print(f'\nname: {self.name}')
        print(f'start date: {self.start_date}')
        print(f'end date: {self.end_date}')
        # print member name
        for member in self.members:
            print(f'member name: {member.first_name}')

        print(f'\nmember objects: {self.members}\n')
        