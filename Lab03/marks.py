students = [
    {
        "name": "Matt",
        "homework": [90.0, 97.0, 75.0, 92.0],
        "quizzes": [88.0, 40.0, 94.0],
        "tests": [75.0, 90.0],
    },
    {
        "name": "Mich",
        "homework": [100.0, 92.0, 98.0, 100.0],
        "quizzes": [82.0, 83.0, 91.0],
        "tests": [89.0, 97.0],
    },
    {
        "name": "Mark",
        "homework": [0.0, 87.0, 75.0, 22.0],
        "quizzes": [0.0, 75.0, 78.0],
        "tests": [100.0, 100.0],
    }
]

if __name__ == '__main__':
    home_ave = 0
    quiz_ave = 0
    test_ave = 0
    
    for student in students:
        home_ave += sum(student["homework"]) / len(student["homework"])
    home_ave /= len(students)
    print(f"Average homework mark: {home_ave}")

    for student in students:
        quiz_ave += sum(student["quizzes"]) / len(student["quizzes"])
    quiz_ave /= len(students)
    print(f"Average quiz mark: {quiz_ave}")

    for student in students:
        test_ave += sum(student["tests"]) / len(student["tests"])
    test_ave /= len(students)
    print(f"Average test mark: {test_ave}")