import io
import csv

def read_csv(file_input):
    data = file_input.read().decode('UTF-8')
    stream = io.StringIO(data)
    return csv.DictReader(stream)

def make_csv(time_group):
    with io.StringIO() as csvfile:
        fieldnames = ['member_id', 'main_contact', 'phone', 'uid']
        writer = csv.DictWriter(csvfile, 
                                fieldnames=fieldnames, 
                                extrasaction='ignore')

        writer.writeheader()
        for row in time_group:
            writer.writerow(row)

        return csvfile.getvalue()