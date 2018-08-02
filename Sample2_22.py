'''Write a python code to generate grade using dictionary. Dictionary should have student names as keys
(assuming names are unique) and subject_name and mark as value. There are 5 subjects for each student.
 Marks should be converted to grades (90 – 100 A+, 80-89 A etc).'''

Student = {'Batman':{'CC':90,'OS':80,'ML':100,'CS':95,'CO':100},
'Superman':{'CC':80,'OS':70,'ML':60,'CS':55,'CO':20},
'Joker':{'CC':70,'OS':60,'ML':60,'CS':55,'CO':100},
'Doomsday':{'CC':60,'OS':80,'ML':60,'CS':55,'CO':20}}

def calc_marks(S):
    for key in S:
        for key1 in S[key]:
            if  int(S[key][key1]) in range(90,101):
                S[key][key1] = S[key][key1],'A+'
            elif int(S[key][key1]) in range(80,89):
                S[key][key1] = S[key][key1],'A'
            elif int(S[key][key1]) in range(70,79):
                S[key][key1] = S[key][key1],'B+'
            elif int(S[key][key1]) in range(60,69):
                S[key][key1] = S[key][key1],'B'
            elif int(S[key][key1]) in range(50,59):
                S[key][key1] = S[key][key1],'C+'
            else:
                S[key][key1] = S[key][key1],'MakeUP'
    print(S)
calc_marks(Student)
