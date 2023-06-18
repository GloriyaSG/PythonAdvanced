def gather_credits(min_credits,*args):
    enrollment = 0
    courses = set()
    for course, points in args:
        if enrollment >= min_credits:
            break
        if course not in courses:
            enrollment += points
            courses.add(course)

    if enrollment < min_credits:
        return f"You need to enroll in more courses! You have to gather {min_credits-enrollment} credits more."
    else:
        return f"Enrollment finished! Maximum credits: {enrollment}.\nCourses: {', '.join(sorted([x for x in courses]))}"






print(gather_credits(
    80,
    ("Basics", 27),
))
print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))
print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))
