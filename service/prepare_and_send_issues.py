import os

import re

from service.fetch_issues import fetch_project_issues
from service.send_issues import send_email_with_attachment

# vars for stmp email addresses
file_report_name = os.getenv('FILE_REPORT_NAME')
email_password = os.getenv('EMAIL_PASSWORD')
email_user = os.getenv('EMAIL_USERNAME')
email_sender = os.getenv('EMAIL_SENDER')
email_recipient = os.getenv('EMAIL_RECIPIENT')
email_file_name = os.getenv('FILE_REPORT_NAME')
email_file_path = './' + email_file_name + '.txt'
email_smtp = os.getenv('EMAIL_SMTP')
email_body = os.getenv('EMAIL_BODY')
email_subject = os.getenv('EMAIL_SUBJECT')
email_port = os.getenv('EMAIL_PORT')

# Regular expression for validating an Email
email_regex = '^(\\w|\\.|\\_|\\-)+[@](\\w|\\_|\\-|\\.)+[.]\\w{2,}$'


def validate_email(email):
    if re.search(email_regex, email):
        return True
    else:
        return False


def fetch_issues():
    project_issues = fetch_project_issues()
    print(project_issues)
    return project_issues


def extract_title(issue):
    return issue.get('title', 'Generic')


def extract_description(issue):
    return issue.get('description', None)


def send_email_with_project_issues(receiver_email):
    while not validate_email(receiver_email):
        print("Invalid email! \n😜Dont' be like 👋nis \nPlease try again.")
        receiver_email = input("Please enter the receiver's email: ")

    send_email_with_attachment(email_smtp,
                               email_port,
                               email_user,
                               email_password,
                               receiver_email,
                               email_subject,
                               email_body.replace('NEWLINE', '\n\n'),
                               email_file_path,
                               email_sender,
                               receiver_email)

    return 'Email sent to {0}'.format(receiver_email)


def check_and_remove_null(description):
    if description is None:
        return ''
    else:
        return description.replace('null', '')


def check_for_empty_string(input_list):
    return "" not in input_list


def remove_spaces(input_list):
    return [item.strip() for item in input_list]


def format_as_doc(data):
    formatted_data = ""
    for key, values in data.items():
        formatted_data += f"{key}:\n"
        for value in values:
            formatted_data += f"- {value.strip()}\n"
        formatted_data += "\n"
    return formatted_data


def write_to_file(report_name: str, filter_list, title):
    with open(report_name, 'w') as file:
        file.write(f"{title}\n\n")
        formatted_data = format_as_doc(filter_list)
        file.write(formatted_data)


def create_issue_list():
    project_issues_list = fetch_project_issues()

    issue_list = {}
    filter_list = {}
    for issue in project_issues_list:
        title = extract_title(issue)
        description = extract_description(issue)

        (issue_list.setdefault(title, [])
         .append(check_and_remove_null(description)))

        filter_list = {key: remove_spaces(value) for key, value in issue_list.items()
                       if check_for_empty_string(value)}

    file_path = f"{file_report_name}.txt"
    write_to_file(file_path, filter_list, "LISTA ISSUES")

    return project_issues_list
