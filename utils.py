"""Utility functions for student data processing."""


def highest_score(students):
    return max(students, key=lambda student: student["score"])


def lowest_score(students):
    return min(students, key=lambda student: student["score"])


def average_score(students):
    return sum(student["score"] for student in students) / len(students)