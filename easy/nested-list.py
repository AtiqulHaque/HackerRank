if __name__ == '__main__':
    student = []
    for _ in range(int(input())):
        student.append([input(),float(input())])
    second_highest = sorted(list(set([marks for name, marks in student])))[1]
    print('\n'.join([a for a,b in sorted(student) if b == second_highest]))
