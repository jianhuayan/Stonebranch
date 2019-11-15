#!/usr/bin/python3
import csv

infile1 = 'CUSTOMER_orig.csv'
infile2 = 'INVOICE_orig.csv'
infile3 = 'INVOICE_ITEM_orig.csv'
infile4 = 'CUSTOMER_1000_INPUT.csv'
outfile0 = 'CUSTOMER_hash.csv'
outfile1 = 'CUSTOMER_new.csv'
outfile2 = 'INVOICE_new.csv'
outfile3 = 'INVOICE_ITEM_new.csv'


def main():
    customer_map = {}
    # header row
    header = []
    # first hash the 500k entries
    with open(infile1, 'r') as in1:
        csv_reader1 = csv.reader(in1, delimiter=',')
        for i, row in enumerate(csv_reader1):
            if i != 0:
                customer_map[row[0]] = [row[1], row[2]]
            else:
                # keep track of correct header row format
                header = row

    # then look up each customer code in customer_map
    with open(infile4, 'r') as in4:
        csv_reader4 = csv.reader(in4, delimiter=',')
        with open(outfile1, 'w') as out:
            csv_writer = csv.writer(out, delimiter=',')
            for i, row in enumerate(csv_reader4):
                if i != 0:
                    cust_id = row[0]
                    csv_writer.writerow([cust_id, customer_map[cust_id][0], customer_map[cust_id][1]])
                else:
                    # write the first header column
                    csv_writer.writerow(header)


if __name__ == '__main__':
    main()
