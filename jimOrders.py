def jimOrders(lst):
    p = []
    res_dct = {i+1:lst[i][0]+lst[i][1] for i in range(0, len(lst))} 
    print(res_dct)
    sort_orders = sorted(res_dct.items(), key=lambda x: x[1])
    print(sort_orders)
    for i in range(0,len(sort_orders)):
        p.append(sort_orders[i][0])
    return p
