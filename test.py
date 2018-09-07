from classes import *

if __name__ == "__main__":


    # create a term
    term3_2018 = Term("2018.3", "00/00/0000", "00/00/0000")

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
    ankit = Volunteer("ankit", "sejwal", "0400000000")
    ankit.print_info()

    # add members to a term
    term3_2018.add_member(ankit)
    term3_2018.add_member(bern)
    term3_2018.add_member(juli)
    term3_2018.add_member(matt)

    term3_2018.print_info()
