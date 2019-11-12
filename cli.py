from __future__ import print_function, unicode_literals
from PyInquirer import prompt
from pprint import pprint
questions = [
    {
        'type': 'input',
        'name': 'team_members',
        'message': 'Team members',
    },
    {
        'type': 'input',
        'name': 'sprint_days',
        'message': 'Sprint days',
    },
    {
        'type': 'input',
        'name': 'work_days',
        'message': 'Work days',
    },
    {
        'type': 'input',
        'name': 'daily_working_time',
        'message': 'Daily working time (h)',
    },
    {
        'type': 'input',
        'name': 'daily_rest_time',
        'message': 'Daily rest time (m)',
    },
    {
        'type': 'input',
        'name': 'meeting_time',
        'message': 'Meeting time (h)',
    }

]
answers = prompt(questions)

def calcTotalTime(answers):
    tm = int(answers['team_members'])
    sd = int(answers['sprint_days'])
    wd = int(answers['work_days'])
    dwt = int(answers['daily_working_time'])
    drt = int(answers['daily_rest_time'])
    mt = float(answers['meeting_time'])

    member_sprint_time = ((dwt-drt/60)*sd)-mt
    
    total_time_in_weeks = (member_sprint_time*tm)/dwt/wd
    rest_time_in_days = total_time_in_weeks%wd * wd
    rest_time_in_hours = rest_time_in_days%dwt

    return str(int(total_time_in_weeks)) + 'w ' + str(int(rest_time_in_days)) + 'd ' + str(int(rest_time_in_hours)) + 'h' 


total_time = calcTotalTime(answers)

print(total_time)
