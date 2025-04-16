import utilities.menu as menu
import utilities.other as other
option=0
student=[]

if __name__ == "__main__":
    while True:
        try:    
            option = menu.select_option() 
            if option == 1:
                other.add_student(student)
                #1break
            elif option == 2:
                other.show_students_records(student)
            elif option == 3:
                other.show_top3(student)
            elif option == 7:
                break
            else:
                print ("***Invalid Entry***")
                print ("Please enter a number (1 - 7)")
        except ValueError as error:
            print ("***Invalid Entry***")
            print("Please enter a number (1 - 7)")
