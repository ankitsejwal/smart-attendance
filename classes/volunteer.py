class Volunteer:

    counter = 1

    def __init__(self, first_name, last_name, phone_no):
        self.first_name = first_name
        self.last_name  = last_name
        self.phone_no   = phone_no
        # assigning id
        self.id = Volunteer.counter
        Volunteer.counter += 1

    def print_info(self):
        print(f'id: {self.id}')
        print(f'volunteer name: {self.first_name} {self.last_name}')
        print(f'phone_no: {self.phone_no}')
