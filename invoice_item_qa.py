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
    invoice_map = {}

    # header row
    header = []
    # first hash the 5M entries
    with open(infile3, 'r') as in3:
        csv_reader3 = csv.reader(in3, delimiter=',')
        for i, row in enumerate(csv_reader3):
            # print(row)
            if i != 0:
                # if invoice code already exists in the map, append to existing list of lists
                if row[0] in invoice_map:
                    invoice_map[row[0]].append([row[1], row[2], row[3]])
                else:
                    # otherwise, add entry in map and initialize as list of lists
                    invoice_map[row[0]] = []
                    invoice_map[row[0]].append([row[1], row[2], row[3]])
            else:
                # keep track of correct header row format
                header = row
    print(invoice_map)
    # then look up each invoice code in invoice_map
    with open(outfile2, 'r') as out2:
        csv_reader4 = csv.reader(out2, delimiter=',')
        with open(outfile3, 'w') as out:
            csv_writer = csv.writer(out, delimiter=',')
            for i, row in enumerate(csv_reader4):
                print(row[1])
                if i != 0:
                    invoice_code = row[1]
                    invoice_item_list = invoice_map[invoice_code]
                    # now each entry in invoice map can potentially have multiple invoice items so we loop through those
                    for invoice in invoice_item_list:
                        csv_writer.writerow([invoice_code, invoice[0],
                                             invoice[1], invoice[2]])
                else:
                    # write the first header column
                    csv_writer.writerow(header)


if __name__ == '__main__':
    main()
