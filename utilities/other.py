data_list=["Full name", "Last name","First name","Class", "Spanish grade","English grade", "History grade","Science grade", "Average grade"]
keys_list=["full_name", "last_name","first_name","class", "spanish_grade","english_grade", "history_grade","science_grade","average"]

def add_student(student_list):
    while True:
        temp_student={}
        temp_average=0
        for i in range(1, len(data_list)-1):
            if i<4 :
                temp_student[keys_list[i]] = input(f"Enter the {data_list[i]}: ")
            else:
                while True:
                    try:
                        temp_student[keys_list[i]] = int(input(f"Enter the {data_list[i]}: "))
                        if 0 <= temp_student[keys_list[i]] <=100:
                            temp_average += temp_student[keys_list[i]]
                            break
                        else:
                            print("Invalid Entry, type a value (0-100)")
                    except ValueError as error:
                        print("Invalid Entry, type a value (0-100)")
        temp_student["full_name"] = f"{temp_student["last_name"]} {temp_student["first_name"]}"
        temp_student["full_name"] = temp_student["full_name"].title()
        temp_student["average"] = temp_average/4
        student_list.append(temp_student)
        option = str(input("Add another student?(Y/N): "))    
        if option == "N" or option == "n":
            break
    return temp_student


def show_students_records(student_list):
    if not student_list:
        print("""No records have been added yet!
            """)
    else:
        student_list.sort(key=lambda k:k["full_name"])
        print("Students Report")
        print()
        for i in range(0, len(student_list)):
            for j in range(0, len(data_list)):
                if j == 1 or j == 2:
                    continue
                print(f"{data_list[j]}: {student_list[i][keys_list[j]]}")
            print()


def show_top3(student_list):
    if not student_list:
            print("""No records have been added yet!
                """)
    else:
        try:
            student_list.sort(key=lambda k:k["average"],reverse=True)
            print("Student's Top 3")
            for i in range(0, 3):
                print()
                for j in range(0, len(data_list)):
                    if 0<j< len(data_list)-1:
                        continue
                    print(f"{data_list[j]}: {student_list[i][keys_list[j]]}")
            print()
        except IndexError:
            print("End of the list")
            print()





#student=[]
#add_student(student)  
#show_students_records(student)
#print(student)

