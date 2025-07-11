def read_data_from_file(dataset):
    with open(dataset, 'r') as file:
        content = file.read()
        # Split by comma and convert each item to an integer
        data = [int(x.strip()) for x in content.split(',')]
    return data

def sort_data(data):
    return sorted(data)

def run_sorted(data):
    for dataset in data:
        if dataset == 0:
            print("no income or loss")
        elif dataset > 0:
            print(f"income: {dataset}")
        else:
            print(f"loss: {dataset}")

# Read from dataset.txt
data = read_data_from_file('dataset.txt')
sorted_data = sort_data(data)
run_sorted(sorted_data)

print(f"total: {sum(data)}")
 