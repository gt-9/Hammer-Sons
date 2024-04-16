hours = 41.5
#Street Snoop
if hours <=2:
  street_snoop_cost = hours * 100 + 200
elif hours <=6:
  street_snoop_cost = hours * 80 + 20
elif hours <=10:
  street_snoop_cost = hours * 60 + 20
else:
  street_snoop_cost = hours * 55 + 20
#print street_snoop_cost
print(street_snoop_cost)
#Street Snoop Premium
street_snoop_premium = 1250.00
print(street_snoop_premium)
#Digital Deep Snoop
if hours <=2:
  digital_deep_snoop_cost = hours * 300 + 200
elif hours <=6:
  digital_deep_snoop_cost = hours * 240 + 20
elif hours <=10:
  digital_deep_snoop_cost = hours * 180 + 20
else:
  digital_deep_snoop_cost = hours * 165 + 20
print(digital_deep_snoop_cost)
print(street_snoop_cost)
print(street_snoop_premium)
print(digital_deep_snoop_cost)
print(street_snoop_cost)
print(street_snoop_premium)
print(digital_deep_snoop_cost)