user_input = ""


def print_pool_table_title():
    print("---------------------")
    print("UH Pool Table Manager")
    print("---------------------")


def pool_table_menu():
    print("Press [1] to View Pool Tables")
    print("Press [2] to Occupy Pool Table")
    print("Press [3] to Un-Occupy Pool Table")


print_pool_table_title()


while user_input != "q":
    user_input == input("What would you like to do? ")
    pool_table_menu()
