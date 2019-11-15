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
    with open(infile2, 'r') as in2:
        csv_reader2 = csv.reader(in2, delimiter=',')
        for i, row in enumerate(csv_reader2):
            # print(row)
            if i != 0:
                # if customer code already exists in the map, append to existing list of lists
                if row[0] in customer_map:
                    customer_map[row[0]].append([row[1], row[2], row[3]])
                else:
                    # otherwise, add entry in map and initialize as list of lists
                    customer_map[row[0]] = []
                    customer_map[row[0]].append([row[1], row[2], row[3]])
            else:
                # keep track of correct header row format
                header = row


    # then look up each customer code in customer_map
    with open(infile4, 'r') as in4:
        csv_reader4 = csv.reader(in4, delimiter=',')
        with open(outfile2, 'w') as out:
            csv_writer = csv.writer(out, delimiter=',')
            for i, row in enumerate(csv_reader4):
                print(row)
                if i != 0:
                    cust_code = row[0]
                    invoice_list = customer_map[cust_code]
                    # now each entry in customer map can potentially have multiple invoices so we loop through those
                    for invoice in invoice_list:
                        csv_writer.writerow([cust_code, invoice[0],
                                             invoice[1], invoice[2]])
                else:
                    # write the first header column
                    csv_writer.writerow(header)


if __name__ == '__main__':
    main()
