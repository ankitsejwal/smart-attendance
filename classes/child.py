from .person import Person

class Child(Person):

    counter = 100

    def __init__(self, first_name, last_name, dob):
        super().__init__(first_name, last_name)
        self.dob = dob
        # hold parents
        self.parents    = []
        # assign id
        self.id = Child.counter
        Child.counter += 1


    def add_parent(self, parent):
        self.parents.append(parent)
        parent.childrens.append(self)


    def print_info(self):
        print(f'id: {self.id}')
        print(f'child name: {self.first_name} {self.last_name}')
        print(f'dob: {self.dob}')
        # print parent name
        for parent in self.parents:
            print(f'Parent name: {parent.first_name} {parent.last_name}')

        print(f'\nparent object: {self.parents}\n')
