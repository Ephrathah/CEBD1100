exchage_rate = 1.377
us_exchage_rate = 19.99
can_exc_rate =  exchage_rate * us_exchage_rate
item_name = 'Bluray Movie'

#print ("item name :%s" + str(can_exc_rate))
#print ("purchaed price: " + format(can_exc_rate))

#can_conv = usd_exchange_rates['CAD']
#can_price = can_conv * us_exchage_rate
can_price = exchage_rate * us_exchage_rate
real_price = round(can_price,2)

print("Item name is : " + item_name)
print("Purchase price in Canadian money is : $" + str(round(can_price,2)))

