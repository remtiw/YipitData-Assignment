def main():
    local = 0;
    travel = 0;
    goods = 0;
    total = 0;
    inFile = open("Q4_2013_Groupon_North_America_Data.csv", "r");
    for line in inFile:
        parts = line.split(',');
        #print(parts);
        dates = parts[3].split('/');
        #print(dates)
        if (((dates[0] == '10') or (dates[0] == '11') or (dates[0] == '12')) and (dates[2] == '2013')):
            if (parts[5] == "Local"):
                local += float(parts[2]);
            if (parts[5] == "Travel"):
                travel += float(parts[2]);
            if (parts[5] == "Goods"):
                goods += float(parts[2]);

            total += float(parts[2]);
    print("--------------------4Q13 BILLINGS--------------------\n")
    print("Local total billings: " + str(local));
    print("Goods total billings: " + str(goods));
    print("Travel total billings: " + str(travel) + "\n");
    print("Total billings: " + str(total) + "\n");
    inFile.close();
