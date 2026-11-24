"""Demo application entry point."""

from students import Student, students
from utils import highest_score, lowest_score, average_score, median_score

def main(students_list: list[Student] | None = None):
    if students_list is None:
        students_list = students

    print("=== Student Report ===")
    for student in students_list:
        print(f"{student.name: <10}: {student.score:>5}")

    print(f"\nHighest score: {highest_score(students_list)}")
    print(f"Lowest score: {lowest_score(students_list)}")
    print(f"Average score: {average_score(students_list):.2f}")
    print(f"Median score: {median_score(students_list):.2f}")

if __name__ == "__main__":
    main()