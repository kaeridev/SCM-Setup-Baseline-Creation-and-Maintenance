"""Utility functions for student data processing."""
from students import Student
import statistics

def highest_score(students_list: list[Student] | None = None):
    if not students_list:
        return 0
    return max(students_list, key=lambda student: student.score)


def lowest_score(students_list: list[Student] | None = None):
    if not students_list:
        return 0
    return min(students_list, key=lambda student: student.score)


def average_score(students_list: list[Student] | None = None):
    if not students_list:
        return 0
    return sum(student.score for student in students_list) / len(students_list)

def median_score(students_list: list[Student] | None = None):
    if not students_list:
        return 0
    return statistics.median(student.score for student in students_list)

def format_report(students_list: list[Student] | None = None):
    report_lines = ["=== Student Report ==="]
    for student in students_list or []:
        report_lines.append(f"{student.name: <10}: {student.score:>5}")
    return "\n".join(report_lines)
