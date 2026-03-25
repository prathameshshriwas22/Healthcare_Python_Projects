print("🏥 Hospital Patient Record System")

patients = []

while True:

    print("\n1. Add Patient")
    print("2. View Patients")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter patient name: ")
        age = input("Enter patient age: ")
        disease = input("Enter disease: ")

        patient = {"Name": name, "Age": age, "Disease": disease}
        patients.append(patient)

        print("Patient record added successfully!")

    elif choice == "2":
        print("\nPatient Records:")
        for p in patients:
            print(p)

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice")