import csv

csv.register_dialect('mr', delimiter='|', quoting=csv.QUOTE_NONE)
print(csv.list_dialects())
csv.unregister_dialect('mr')
print(csv.list_dialects())
