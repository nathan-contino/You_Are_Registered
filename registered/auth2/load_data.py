# This whole tutorial to take CSV to Models is from:
#  http://mitchfournier.com/2011/10/11/how-to-import-a-csv-or-tsv-file-into-a-django-model/

# Full path and name to your csv file
csv_filepathname="/Users/kevingerami/Desktop/2015-Fall/CSC210/git/You_Are_Registered/registered/auth2/data2.csv"
# Full path to your django project directory
your_djangoproject_home="/Users/kevingerami/Desktop/2015-Fall/CSC210/git/You_Are_Registered/registered"

import sys,os
sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'registered.settings'

from auth2.models import Courses

import csv
dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')

for row in dataReader:
    course = Courses()
    course.crn = row[0].decode('utf-8')
    course.crsnum = row[1].decode('utf-8')
    course.title = row[2].decode('utf-8')
    course.credits = row[3].decode('utf-8')
    course.day = row[4].decode('utf-8')
    course.start = row[5].decode('utf-8')
    course.end = row[6].decode('utf-8')
    course.building = row[7].decode('utf-8')
    course.room = row[8].decode('utf-8')
    course.cap = row[9].decode('utf-8')
    course.prof = row[10].decode('utf-8')
    course.current = 0
    print row[2]

    course.save()
