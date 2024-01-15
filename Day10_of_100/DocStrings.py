def name_formatter(fname , lname):
    """Takes a first and last name and format it to a Title Cased Version of a formatted name type."""

    if fname == "" or lname == "":
        return "Provide Valid Input's. "
    return fname.title()+lname.title()



# hover on Function call to check the Documentation done 

print(name_formatter(input("Enter Your Name : "),input("Enter Your Clan Name :")))