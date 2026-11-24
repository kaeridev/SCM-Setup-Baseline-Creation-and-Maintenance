"""Demo application entry point."""

from students import students
from utils import highest_score, lowest_score, average_score

def main():
    print("=== Student Report ===")
    for student in students:
        print(f"{student["name"]}: {student["score"]}")

    print(f"\nHighest score: {highest_score(students)}")
    print(f"Lowest score: {lowest_score(students)}")
    print(f"Average score: {average_score(students):.2f}")

if __name__ == "__main__":
    main()