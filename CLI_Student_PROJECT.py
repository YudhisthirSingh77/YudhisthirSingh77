import csv


studentlist = []
stu_header = ['Name','Branch','Age','Id']

def funinput():
    stu_name = input('Enter Student Name:')
    stu_branch = input('Enter Student Branch:')
    stu_age = int(input('Enter Student Age:'))
    studentlist.append([stu_name,stu_branch,stu_age])
funinput()
addmore = input('Add More Students Data:  y/n')

def exportcsv():
    with open("student.csv",'w') as f:
        writer = csv.writer(f)
        writer.writerows([stu_header])
        writer.writerows(studentlist)
    
while addmore == "y":
    funinput()
    addmore = input('Add More Students Data:  y/n')
else:
    print('csv exported')
    exportcsv()



