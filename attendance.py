# Global Values
STUDENTS = []
TOTAL_CLASSES = 50


# Add student function
def ADD_STUDENT():
    print("-" * 50)
    print(f"{'Add Student Attendance':^50}")
    print("-" * 50)

    STUDENT_ID = input("Enter Student ID (0001 - 9999): ").strip()

    # Validate ID before asking for the name
    if not STUDENT_ID.isdigit() or not (1 <= int(STUDENT_ID) <= 9999):
        print("❌ Invalid ID. Must be a number between 0001 and 9999.")
        return

    STUDENT_ID = STUDENT_ID.zfill(4)  # Pads with zeros, e.g., "1" becomes "0001"

    if any(STUDENT["ID"] == STUDENT_ID for STUDENT in STUDENTS):
        print("❌ A student with this ID already exists.")
        return

    # Name is now asked only after the ID has been validated
    NAME = input("Enter Student Name: ").strip()

    if not NAME:
        print("❌ Invalid name. Try again.")
        return

    try:
        CLASSES_ATTENDED = int(input("Classes Attended (Out of 50): ").strip())
    except ValueError:
        print("⚠️ Invalid input. Please enter a number for classes attended.")
        return

    if CLASSES_ATTENDED < 0 or CLASSES_ATTENDED > TOTAL_CLASSES:
        print("❌ Invalid number of classes attended. Try again.")
        return

    STUDENTS.append({
        "ID": STUDENT_ID,
        "NAME": NAME,
        "ATTENDED": CLASSES_ATTENDED
    })
    print("-" * 50)
    print("✅ Student registered successfully.")


# Calculate percentage function
def CALCULATE_PERCENTAGE(CLASSES_ATTENDED):
    return (CLASSES_ATTENDED / TOTAL_CLASSES) * 100


# Search student function
def SEARCH_STUDENT():
    print("-" * 50)
    print(f"{'Search Student':^50}")
    print("-" * 50)

    STUDENT_ID = input("Enter Student ID to search: ").strip()

    # Validate that input is a digit and within range
    if not STUDENT_ID.isdigit() or not (1 <= int(STUDENT_ID) <= 9999):
        print("❌ Invalid ID. Try again.")
        return

    # Zero-pad so "1" matches stored "0001"
    STUDENT_ID = STUDENT_ID.zfill(4)

    for STUDENT in STUDENTS:
        if STUDENT["ID"] == STUDENT_ID:
            PERCENTAGE = CALCULATE_PERCENTAGE(STUDENT["ATTENDED"])

            print("\nAttendance Record")
            print("-" * 50)
            print(f"{'ID':<10} {'NAME':<20} {'ATTENDED':<10} {'PERCENTAGE':<10}")
            print("-" * 50)
            print(f"{STUDENT['ID']:<10} {STUDENT['NAME']:<20} {STUDENT['ATTENDED']:<10} {PERCENTAGE:.1f}%")
            print("-" * 50)
            return

    print("-" * 50)
    print("❌ Student not found.")


# View attendance records function
def VIEW_RECORDS():
    print("-" * 50)
    print(f"{'Attendance Records':^50}")
    print("-" * 50)

    if not STUDENTS:
        print("⚠️ No students registered.")
        return

    print(f"{'ID':<10} {'NAME':<20} {'ATTENDED':<10} {'PERCENTAGE':<10}")
    print("-" * 50)

    for STUDENT in STUDENTS:
        PERCENTAGE = CALCULATE_PERCENTAGE(STUDENT["ATTENDED"])
        print(f"{STUDENT['ID']:<10} {STUDENT['NAME']:<20} {STUDENT['ATTENDED']:<10} {PERCENTAGE:.1f}%")

    print("-" * 50)


# Highest attendance function
def HIGHEST_ATTENDANCE():
    print("-" * 50)
    print(f"{'Highest Attendance':^50}")
    print("-" * 50)

    if not STUDENTS:
        print("⚠️ No students registered.")
        return

    HIGHEST_STUDENT = STUDENTS[0]

    for STUDENT in STUDENTS:
        if STUDENT["ATTENDED"] > HIGHEST_STUDENT["ATTENDED"]:
            HIGHEST_STUDENT = STUDENT

    PERCENTAGE = CALCULATE_PERCENTAGE(HIGHEST_STUDENT["ATTENDED"])

    print(f"{'ID':<10} {'NAME':<20} {'ATTENDED':<10} {'PERCENTAGE':<10}")
    print("-" * 50)
    print(f"{HIGHEST_STUDENT['ID']:<10} {HIGHEST_STUDENT['NAME']:<20} "
          f"{HIGHEST_STUDENT['ATTENDED']:<10} {PERCENTAGE:.1f}%")
    print("-" * 50)


# Lowest attendance function
def LOWEST_ATTENDANCE():
    print("-" * 50)
    print(f"{'Lowest Attendance':^50}")
    print("-" * 50)

    if not STUDENTS:
        print("⚠️ No students registered.")
        return

    LOWEST_STUDENT = STUDENTS[0]

    for STUDENT in STUDENTS:
        if STUDENT["ATTENDED"] < LOWEST_STUDENT["ATTENDED"]:
            LOWEST_STUDENT = STUDENT

    PERCENTAGE = CALCULATE_PERCENTAGE(LOWEST_STUDENT["ATTENDED"])

    print(f"{'ID':<10} {'NAME':<20} {'ATTENDED':<10} {'PERCENTAGE':<10}")
    print("-" * 50)
    print(f"{LOWEST_STUDENT['ID']:<10} {LOWEST_STUDENT['NAME']:<20} "
          f"{LOWEST_STUDENT['ATTENDED']:<10} {PERCENTAGE:.1f}%")
    print("-" * 50)


# Display menu
def DISPLAY_MENU():
    print("-" * 50)
    print(f"{'Main Menu':^50}")
    print("-" * 50)

    print("1. Add Student Attendance")
    print("2. View Attendance Records")
    print("3. Search Student")
    print("4. Show Highest Attendance")
    print("5. Show Lowest Attendance")
    print("6. Exit")

    print("-" * 50)


# Main loop
def MAIN():
    while True:
        DISPLAY_MENU()

        CHOICE = input("Enter your choice: ").strip()

        if CHOICE == "1":
            ADD_STUDENT()

        elif CHOICE == "2":
            VIEW_RECORDS()

        elif CHOICE == "3":
            SEARCH_STUDENT()

        elif CHOICE == "4":
            HIGHEST_ATTENDANCE()

        elif CHOICE == "5":
            LOWEST_ATTENDANCE()

        elif CHOICE == "6":
            print("Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    MAIN()