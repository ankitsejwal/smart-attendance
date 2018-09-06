class Child:

    counter = 100

    def __init__(self, first_name, last_name, dob):
        self.first_name = first_name
        self.last_name  = last_name
        self.dob        = dob
        # hold parents
        self.parents    = []
        # assign id
        self.id = Child.counter
        Child.counter += 1


    def print_info(self):
        print(f'id: {self.id}')
        print(f'child name: {self.first_name} {self.last_name}')
        print(f'dob: {self.dob}')
        # print parent name
        for parent in self.parents:
            print(f'Parent name: {parent.first_name} {parent.last_name}')
        
        print(f'\nparent object: {self.parents}\n')


    def add_parent(self, parent):
        self.parents.append(parent)
        parent.childrens.append(self)

class Parent:

    counter = 500

    def __init__(self, first_name, last_name, phone_no):
        self.first_name = first_name
        self.last_name  = last_name
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
        

if __name__ == "__main__":

    # create children
    juli = Child("juli", "", "00/00/00")
    matt = Child("matt", "", "00/00/00")
    tomm = Child("tomm", "", "00/00/00")

    # create parent
    bern  = Parent("bern", "", "04000000000")

    # add child to parent
    bern.add_child(juli)
    bern.add_child(matt)

    # add parent to a child
    tomm.add_parent(bern)

    juli.print_info()
    matt.print_info()
    tomm.print_info()
    bern.print_info()
    
    # create a volunteer
    ankit = Volunteer("ankit", "sejwal", "0452405206")
    ankit.print_info()
