def print_course_details(user_course):
    course_list = {
        'CSC101': { 'Room': 3004, 'Instructor': 'Haynes', 'Time': '8:00 a.m.'},
        'CSC102': { 'Room': 4501, 'Instructor': 'Alvarado', 'Time': '9:00 a.m.'},
        'CSC103': { 'Room': 6755, 'Instructor': 'Rich', 'Time': '10:00 a.m.'},
        'NET110': { 'Room': 1244, 'Instructor': 'Burke', 'Time': '11:00 a.m.'},
        'COM241': { 'Room': 1411, 'Instructor': 'Lee', 'Time': '1:00 p.m.'}}

    print('Details for: {}'.format(user_course))
    for key1, value1 in course_list.items():
        if key1 == user_course:
            for key2, value2 in value1.items():
                print('{}: {}'.format(key2, value2))
        break

def main():
    user_input = input('Enter course name: ')

    print_course_details(user_input)

if __name__ == '__main__':main()