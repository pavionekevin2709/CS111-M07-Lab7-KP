#CS111 - M07 Lab7
#Lists and Tuples
#Author: Kevin Pavione
#Date: September 22, 2025

#Global list to store all grades
grades = []

#Display the main menu options to the user via console
def display_menu():
    print("\n"+"="*25)
    print("Student Grades Analyzer")
    print("=" *25)
    print("1. Add a new grade")
    print("2. Remove a grade")
    print("3. Show all grades")
    print("4. Calculate and show the statistics (average, highest, lowest)")
    print("5. Convert grades list to tuple and display")
    print("=" *25)

#Add a new grade to the grades list
def add_grade():
    grade = float(input("Enter grade to add (0-100): "))
    
    #validate grade is within an acceptable range
    if 0 <= grade <= 100:
        grades.append(grade)
        print("Added grade:", grade)
    else:
        print("Invalid grade")

#Remove a specific grade from the grades list
def remove_grade():
    #check if grades list is empty
    if not grades:
        print("No grades to remove. This list is empty.")
        return 
    
    print("\nCurrent Grades: ", grades)
    
    try:
        grade = float(input("Enter grade to remove (0-100): "))
        
        #check if the grade inputted by user exists in the list
        if grade in grades:
            grades.remove(grade)
            print("Removed grade:", grade)
        else: 
            print("Grade not found in list")
    except ValueError:
        print("ERROR: Invalid Input. Please ensure you are entering a number.")

#Display all grades in the list
def display_grades():
    if not grades:
        print("No grades to display")
    else:
        print("ALL GRADES:")
        print("Grades:", grades)

#Calculate and display statistical info about the grades
def calculate_stats():
    if not grades:
        print("No grades to calculate")
        return
    
    #Calculations
    avg = sum(grades) / len(grades)
    highest = max(grades)
    lowest = min(grades)
    
    #Display stats
    print("\n" + "-" * 25)
    print("GRADE STATISTICS INFORMATION")
    print("-" * 25)
    print(f"Average Grade: {avg:.2f}")
    print(f"Highest Grade: {highest}")
    print(f"Lowest Grade: {lowest}")
    print("-" * 25)

#Convert grades list to a tuple and display said tuple
def convert_to_tuple():
    if not grades: 
        print("No grades to convert.")
        return
    
    #convert the grades list to a tuple
    grades_tuple = tuple(grades)
    
    #Display tuple
    print('\n' + '-'*25)
    print("GRADES AS A TUPLE")
    print('-' * 25)
    print(f"Grades List: {grades}")
    print(f"Grades Tuple: {grades_tuple}")
    print('-' * 25)

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5) or 'q' to quit: ")
        
        if choice == '1':
            add_grade()
        elif choice == '2':
            remove_grade()
        elif choice == '3':
            display_grades()
        elif choice == '4':
            calculate_stats()
        elif choice == '5':
            convert_to_tuple()
        elif choice.lower() == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
        
        input("\nPress Enter to continue...")

#Entry point of program 
if __name__ == "__main__":
    main()