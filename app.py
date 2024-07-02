from email_validator import EmailNotValidError
from flask import Flask, request, render_template

from service.prepare_and_send_issues import create_issue_list, validate_email, send_email_with_project_issues

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('routes.html')


@app.route('/report', methods=['GET', 'POST'])
def report():
    if request.method == 'POST':
        receiver_email = request.form['email']

        try:
            validate_email(receiver_email)
        except EmailNotValidError as e:
            return render_template('report.html', error=True)

        # Fetch project issues (replace with actual function)
        project_list = create_issue_list()

        # Send email with project issues
        send_email_with_project_issues(receiver_email)

        return render_template('report_sent.html', email=receiver_email, project_list=project_list)
    else:
        return render_template('report.html', error=False)


if __name__ == '__main__':
    app.run(debug=True)
