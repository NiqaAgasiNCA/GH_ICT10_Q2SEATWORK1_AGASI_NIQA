# Student Club Member Checker
from pyscript import display, document

def student_club(e):
    document.getElementById('meta').innerHTML = ''

    studentfirstname = document.getElementById('firstName').value
    studentlastname = document.getElementById('lastName').value

    glee_members = [
        ('Niqa', 'Agasi'),
        ('Cady', 'Bower'),
        ('Mia', 'Marajas'),
        ('Gabbi', 'Riofrio'),
        ('Alexa', 'Salcedo'),
        ('Clara', 'Sabanal')
    ]

    member_checker = (studentfirstname, studentlastname) in glee_members

    display_message = (f'sorry, you are not good enough. Practice more', f'Congratulations {studentfirstname} {studentlastname}, you are now part of the OBMC Glee Club led by Ms. Margery Teola, the club moderator!')

    display(display_message[member_checker], target='meta')
