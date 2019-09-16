bill=input('Enter bill')
if int(bill)<=1000 :
    tip = float(bill) * (1.5 / 100)
    print('Tip for your bill will be 1.5% of your bill and it is : '+str(tip))
else:
    tip = float(bill) * (2.5 / 100)
    print('Tip for your bill will be 2.5% of your bill and it is : '+str(tip))



