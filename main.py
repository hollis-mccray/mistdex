from sources import options

def menu():
    options = {
        "C": "Add Challenge",
        "P": "Add Power Sets",
        "R": "Generate Reports",
        "S": "Settings",
        "X": "Exit"
    }
    choice = '?'
    while choice not in options:
        print("Mist Games Index Manager")
        print()
        for key, value in options.items():
            print(f"{key}. {value}")
        print()
        choice = input("Select an Option: ").upper()
    return choice


def main():
    src_list = options()
    option = menu()
    while option != "X":
        match option:
            case "C":
                print("\nAdding Challenge...\n")
            case "P":
                print("\nAdding Power Set...\n")
            case "R":
                print("\nGenerating Reports...\n")
            case "S":
                src_list.menu()
        option = menu()

main()