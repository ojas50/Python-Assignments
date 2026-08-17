students = ["Aarav", "Isha", "Rohan", "Sneha", "Kabir"]

print("1. Display the third student's name")
print("Third student:", students[2])

print('2. Change "Rohan" to "Rohan Patil"')
students[2] = "Rohan Patil"

print('3. Add new students "Ananya" and "Vihaan"')
students.extend(["Ananya", "Vihaan"])

print("4. Remove 'Kabir'' from the list")
students.remove("Kabir")

print("5. Display the total number of registered students")
print("Total registered students:", len(students))

print("6. Check whether 'Isha' is registered")
if "Isha" in students:
    print("Isha is registered.")
else:
    print("Isha is not registered.")

print("7. Arrange the list in alphabetical order")
sorted_students = students.sort()
print(sorted_students)

print("8. Create a copy of the final student list")
backup_students = students.copy()
print(backup_students)

print("9. AI Hackathon participants")
hackathon = ["Meera", "Arjun", "Isha"]
print(hackathon)

all_participants = students + hackathon
print(all_participants)

print("10. Display the final lists")

print("\nFinal Tech Fest Student List:")
print(students)
print("\nBackup Student List:")
print(backup_students)
print("\nCombined Participant List:")
print(all_participants)
