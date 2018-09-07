from .person import Person

class Parent(Person):

    counter = 500

    def __init__(self, first_name, last_name, phone_no):
        super().__init__(first_name, last_name)
        self.phone_no   = phone_no
        self.childrens  = []
        # assign id
        self.id = Parent.counter
        Parent.counter += 1


    def print_info(self):
        print(f'id: {self.id}')
        print(f'parent name: {self.first_name} {self.last_name}')
        print(f'phone_no: {self.phone_no}')
        # print children name
        for child in self.childrens:
            print(f'children name: {child.first_name}')

        print(f'\nchild objects: {self.childrens}\n')


    def add_child(self, child):
        self.childrens.append(child)
        child.parents.append(self)
        
