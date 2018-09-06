from classes import *

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
