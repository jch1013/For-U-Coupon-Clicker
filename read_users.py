import csv

def read_users(file_name):
    user_list = []
    with open('users.csv', 'r') as csvfile:
        user_reader = csv.reader(csvfile)
        for row in user_reader:
            user_list.append(row)
    return user_list

