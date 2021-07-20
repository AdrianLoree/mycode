#!/usr/bin/env python3

message = 'Your grade for the exam is '

examscore = float(input('What was your exam score?'))

if examscore >= 90:
    message = message + 'an A.'
elif examscore >= 80:
    message = message + 'a B.'
elif examscore >= 70:
    message = message + 'a C.'
elif examscore >= 60:
    message = message + 'a D.'
else:
    message = message + 'a F.'
print(message)
