
def main():
    local_oct = 0;
    travel_oct = 0;
    goods_oct = 0;
    total_oct = 0;
    
    units_local_oct = 0;
    units_travel_oct = 0;
    units_goods_oct = 0;
    
    local_nov = 0;
    travel_nov = 0;
    goods_nov = 0;
    total_nov = 0;

    units_local_nov = 0;
    units_travel_nov = 0;
    units_goods_nov = 0;
    
    local_dec = 0;
    travel_dec = 0;
    goods_dec = 0;
    total_dec = 0;

    units_local_dec = 0;
    units_travel_dec = 0;
    units_goods_dec = 0;
    
    total = 0;
    
    inFile = open("Q4_2013_Groupon_North_America_Data.csv", "r");
    for line in inFile:
        parts = line.split(',');
        dates = parts[3].split('/');
        if ((dates[0] == '10') and (dates[2] == '2013')):
            if (parts[5] == "Local"):
                local_oct += float(parts[2]);
                units_local_oct += float(parts[1]);
            if (parts[5] == "Travel"):
                travel_oct += float(parts[2]);
                units_travel_oct += float(parts[1]);
            if (parts[5] == "Goods"):
                goods_oct += float(parts[2]);
                units_goods_oct += float(parts[1]);

            total_oct += float(parts[2]);
            total += float(parts[2]);
            
        elif ((dates[0] == '11') and (dates[2] == '2013')):
            if (parts[5] == "Local"):
                local_nov += float(parts[2]);
                units_local_nov += float(parts[1]);
            if (parts[5] == "Travel"):
                travel_nov += float(parts[2]);
                units_travel_nov += float(parts[1]);
            if (parts[5] == "Goods"):
                goods_nov += float(parts[2]);
                units_goods_nov += float(parts[1]);

            total_nov += float(parts[2]);
            total += float(parts[2]);
            
        elif ((dates[0] == '12') and (dates[2] == '2013')):
            if (parts[5] == "Local"):
                local_dec += float(parts[2]);
                units_local_dec += float(parts[1]);
            if (parts[5] == "Travel"):
                travel_dec += float(parts[2]);
                units_travel_dec += float(parts[1]);
            if (parts[5] == "Goods"):
                goods_dec += float(parts[2]);
                units_goods_dec += float(parts[1]);

            total_dec += float(parts[2]);
            total += float(parts[2]);
            
    print("--------------------4Q13 BILLINGS OCTOBER--------------------\n")
    print("Local total billings: " + str(local_oct));
    print("Goods total billings: " + str(goods_oct));
    print("Travel total billings: " + str(travel_oct) + "\n");
    print("Total billings: " + str(total_oct) + "\n");
    print("Local units sold: " + str(units_local_oct));
    print("Goods units sold: " + str(units_goods_oct));
    print("Travel units sold: " + str(units_travel_oct) + "\n");

    print("--------------------4Q13 BILLINGS NOVEMBER--------------------\n")
    print("Local total billings: " + str(local_nov));
    print("Goods total billings: " + str(goods_nov));
    print("Travel total billings: " + str(travel_nov) + "\n");
    print("Total billings: " + str(total_nov) + "\n");
    print("Local units sold: " + str(units_local_nov));
    print("Goods units sold: " + str(units_goods_nov));
    print("Travel units sold: " + str(units_travel_nov) + "\n");

    print("--------------------4Q13 BILLINGS DECEMBER--------------------\n")
    print("Local total billings: " + str(local_dec));
    print("Goods total billings: " + str(goods_dec));
    print("Travel total billings: " + str(travel_dec) + "\n");
    print("Total billings: " + str(total_dec) + "\n");
    print("Local units sold: " + str(units_local_dec));
    print("Goods units sold: " + str(units_goods_dec));
    print("Travel units sold: " + str(units_travel_dec) + "\n\n\n");

    print("Total billings in 4Q13: " + str(total));
    inFile.close();
    

main()
