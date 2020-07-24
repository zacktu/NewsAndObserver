'''

Add leading zeros to dates in CSV files related to Coronavirus
provided by Raleigh News & Observer.  The files have a header
row, and the column in question is named 'Date'

'''

import csv

def read_write_file(inputfile, outputfile):

    print('input file is ', inputfile)
    print('outputfile is ', outputfile)
    with open(inputfile, 'rt') as filein:
        with open(outputfile, mode='w') as fileout:
            filewriter = csv.writer(fileout, delimiter=',',
                         quotechar=",", quoting=csv.QUOTE_MINIMAL)
            rows = csv.reader(filein)
            headers = next(rows)
            filewriter.writerow(headers)

            for row in rows:
                try:
                    date = row[1]
                    mdy = date.split('/')
                    newdate = mdy[0].zfill(2) + '/' + mdy[1].zfill(2) + '/' + mdy[2]
                    row[1] = newdate
                    filewriter.writerow(row)
                except ValueError:
                    print('Bad row:', row)

inputfile = '/home/bob/Downloads/data-oEP7U (11).csv'
outputfile = '/home/bob/Downloads/outfile.csv'
read_write_file(inputfile, outputfile)

# if len(sys.argv) == 3:
#      inputfile = sys.argv[1]
#      outputfile = sys.argv[2]
# else:
#     inputfile = input('Enter name of input file:')
#     outputfile = input('Enter name of output file:')