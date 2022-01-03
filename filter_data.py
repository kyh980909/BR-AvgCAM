import os

path = './0526_paper_dataset/0526_dataset'
dataset = os.listdir(path)

for data in dataset:
    if data == 'classes.txt':
        continue
    if data.endswith('.txt'):
        filter_list = list()
        with open(f'{path}/{data}', 'r') as f:
            filter_list = list(filter(lambda x: x[0] != '1', f.readlines()))
            print(filter_list)

        with open(f'{path}/{data}', 'w') as f:
            f.writelines(filter_list)
