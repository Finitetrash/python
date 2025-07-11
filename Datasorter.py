data = [1,0,7,4,-9,4,2]

for DataSet in data:
  if DataSet == 0:
    print("no income")
  elif DataSet > 0:
    print(f"income: {DataSet}")
  else:
    print(f"loss: {DataSet}")
  
  
print(f"total income: {sum(data)}")
