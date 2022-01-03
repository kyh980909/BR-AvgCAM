import os
import shutil

path = './0526_paper_dataset/pitching'
dst = './0526_paper_dataset/not_pitching'
dataset = os.listdir(path)

for data in dataset:
    if data == 'classes.txt':
        continue
    if data.endswith('.txt'):
        with open(f'{path}/{data}', 'r') as f:
            read_line = f.readlines()
            if len(read_line) == 1:
                shutil.move(f'{path}/{data}', f'{dst}/{data}')
                shutil.move(
                    f'{path}/{data.replace(".txt", ".jpg")}', f'{dst}/{data.replace(".txt", ".jpg")}')
