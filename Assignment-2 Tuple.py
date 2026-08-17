courses = ("Python", "Data Science", "Cloud Computing", "Cyber Security", "AI")

print("1. Display the second course selected by the student.")
print(courses[1]) #Data Science

print("2. Display the last two courses using tuple slicing.")
print(courses[-2:])

print("3. Check whether 'python' is present in tuple")
if "Python" in courses:
    print("Python is present")
else:
    print("Python is not present")

print("4. Find the position (index) of 'Cloud Computing'.")
print("Index of 'Cloud Computing' is:", courses.index("Cloud Computing"))

print("5. Find the total number of courses selected.")
print("Total number of courses:", len(courses))

print("6.The student decides to additionally enroll in 'Machine Learning' and 'Web Development'.")
courses = courses + ("Machine Learning", "Web Developement") 
print(courses)

print(" 7. Remove 'Cyber Security' by creating a new tuple")
courses = tuple(course for course in courses if course != 'Cyber Security')
print(courses)

print("8. Arrange courses alphabetically")
sorted_courses = tuple(sorted(courses))
print(sorted_courses)

print("9. Create a backup copy")
backup_courses = sorted_courses
print(backup_courses)

print("10. Friend Courses are:")
friend_courses = ("AI", "Blockchain", "Python")
print(friend_courses)

print("11. Combine the student's courses and friend's courses into a new tuple called combined_courses.")
combined_courses = courses + friend_courses
print(combined_courses)

print("Display final results") 

print("\nFinal course tuple:", courses)
print("Sorted course tuple:", sorted_courses)
print("Backup tuple:", backup_courses)
print("Combined tuple:", combined_courses)