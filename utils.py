"""Utility functions for student data processing."""
import statistics

def highest_score(students):
    if not students:
        return 0
    return max(students, key=lambda student: student.score)


def lowest_score(students):
    if not students:
        return 0
    return min(students, key=lambda student: student.score)


def average_score(students_list=None):
    if not students_list:
        return 0
    return sum(student.score for student in students_list) / len(students_list)

def median_score(students):
    if not students:
        return 0
    return statistics.median(student.score for student in students)

def format_report(students):
    report_lines = ["=== Student Report ==="]
    for student in students:
        report_lines.append(f"{student.name: <10}: {student.score:>5}")
    return "\n".join(report_lines)
