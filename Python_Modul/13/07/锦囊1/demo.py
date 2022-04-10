import csv
csv.register_dialect('mr',delimiter='|',quoting=csv.QUOTE_NONE)
print(csv.get_dialect('excel'))
print(csv.get_dialect('mr'))
print(csv.list_dialects())
