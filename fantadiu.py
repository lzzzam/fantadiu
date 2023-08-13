import csv

# open output file
outFile = open('quotazioni_2023.csv', 'w', newline="")
output = csv.writer(outFile, delimiter=';')

# insert header
output.writerow(["name", "role", "pma", "pfc", "slot", "grade", "expBonus", "dpfcpma", "Id", "R", "RM", "Squadra","Qt.A", "Qt.I", "Diff.", "Qt.A M", "Qt.I M", "Diff.M", "FVM", "FVM M"])

with open("./Fantaculo.csv", 'r') as file1:
    fantaculo = csv.reader(file1, delimiter=';')
    
    # iterate through 1st file
    for row1 in fantaculo:
        name1 = row1[0].lower()
        
        with open("./Quotazioni.csv", 'r') as file2:
            quotazioni = csv.reader(file2, delimiter=';')
            
            # iterate through 2nd file
            for row2 in quotazioni:
                name2 = row2[3].lower()
                
                # search match
                if name1 == name2:
                    
                    # remove 'name'
                    row2.pop(3)
                    
                    # merge rows and add new line in output
                    data = row1 + row2
                    output.writerow(data)





