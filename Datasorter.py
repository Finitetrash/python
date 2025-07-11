data = [1, 0, 7, 4, -9, 4, 2]

def sort_data(data):
    data.sort()
    return data

sorted_data = sort_data(data)

def run_sorted(data):
    for DataSet in data:
        if DataSet == 0:
            print("no income or loss")
        elif DataSet > 0:
            print(f"income: {DataSet}")
        else:
            print(f"loss: {DataSet}")

run_sorted(sorted_data)

print(f"total income: {sum(data)}")
 