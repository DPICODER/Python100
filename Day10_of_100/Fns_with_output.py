# Functions with outputs


def fromat_name(fname , lname):
    # if input is empty 
    if fname == "" or lname == "":
        return "Provide Valid Inputs ."

    return fname.title()+lname.title()


print(fromat_name(input("Enter fname :"),input("Enter lname :")))