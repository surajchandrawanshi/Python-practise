gradebook={
    "Alice": {
        "English": 89,
        "Hindi": 80
    },
    "Malice": {
        "English": 85,
        "Hindi": 81
    }
}

student_name=input("\n Enter student name:")
if student_name in gradebook:
    print("Student found.")
else: 
    print("Student not found")
    exit()

student_subject=input("\n Enter the subject:")

if student_subject in gradebook[student_name]:
    print("Subject found.\n The marks is as follows: ")
    print(gradebook[student_name][student_subject])
else:
    print("Subject not found.")

decision=input("would you like to have the average score of any student:(Y/N):").upper()
subject_number=len(gradebook[name])
if decision=="Y":
    average_score=0
    name=input("Enter student name:")
    if name in gradebook:
        print("Student found.")
        for i,j in gradebook[name].items():
            print("Subject: " + i + "   " + "Marks: " + str(j))
            average_score+=j
        print(f"Average score of {name} is :{average_score/subject_number}")

