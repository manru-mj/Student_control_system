data_list=["Full name", "Class", "Spanish grade","English grade", "History grade","Science grade", "Average grade"]
keys_list=["full_name", "class", "spanish_grade","english_grade", "history_grade","science_grade","average"]

def add_student(student_list):
    while True:
        temp_student={}
        temp_average=0
        for i in range(0, len(data_list)-1):
            if i<2 :
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
        for i in range(0, len(student_list)):
            for j in range(0, len(data_list)):
                print(f"{data_list[j]}: {student_list[i][keys_list[j]]}")


def show_top3(student_list):
    if not student_list:
            print("""No records have been added yet!
                """)
    else:
        student_list.sort(key=lambda k:k["average"],reverse=True)
        for i in range(0, 3):
            for j in range(0, len(data_list)):
                print(f"{data_list[j]}: {student_list[i][keys_list[j]]}")







#student=[]
#add_student(student)  
#show_students_records(student)
#print(student)

