def interview(lst, tot):
    if len(lst) <8:
        return 'disqualified'
        pass
    if lst[0] <=5 and lst[1] <=5 and lst[2] <= 10 and lst[3] <= 10 and lst[4] <= 15 and lst[5] <= 15 and lst[6] <= 20 and lst[7] <= 20 and tot <= 120:
        return 'qualified'
    else:
        return 'disqualified'

print(interview([5, 5, 10, 10, 15, 15, 20, 20], 120))
print(interview([2, 3, 8, 6, 5, 12, 10, 18], 120))
print(interview([2, 3, 8, 6, 5, 12, 10, 18], 64))
print(interview([5, 5, 10, 10, 25, 15, 20, 20], 120))
print(interview([5, 5, 10, 20, 15, 15, 20, 20], 140))
print(interview([10, 10, 15, 15, 20, 20], 150))
