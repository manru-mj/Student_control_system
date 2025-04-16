def print_menu():
    print("""Select an option:
        1. Add new Student
        2. Students report
        3. Student's Top 3
        4. Average grade
        5. Export to file
        6. Import from File
        7. Exit""")
    
def select_option():
    print_menu()
    option = int(input("Type your option: "))
    return option



def print_student_report():
    print("Students Report")

def calculate_top3():
    print("Students Top3")

def calculate_average_grade():
    print("Students average grade")

def export_to_file():
    print("Export to File")

def import_from_file():
    print("Import from File")
