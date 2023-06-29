import glob
import multitasking
import os
import csv
import pandas as pd
import time

state = 0


def reset_csv():
    with open('multitasking.csv', 'w') as f:
        f.write('id,name,ext\n')

reset_csv()

def write_csv(file, newrow):
    with open(file, mode='a') as f:
        f_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        f_writer.writerow(newrow)

@multitasking.task
def generate_set(data, process_name, filename):
    print("The number of files: ", len(data))
    for idx, file in enumerate(data):
        if idx % 100 == 0:
            print("[{}/{}]".format(idx, len(data) - 1))
        extension = file.split('.')[-1]
        face_id = os.path.basename(file).split('.')[0]
        face_label = os.path.basename(os.path.dirname(file))
        write_csv('multitasking.csv', [face_id, face_label, extension])
    print("Process", process_name, 'finished!')
    check_and_format(filename)

def check_and_format(filename):
    global state
    state += 1
    if state == 4:
        format_data(filename)

def format_data(filename):
    df = pd.read_csv('multitasking.csv')
    df = df.sort_values(by=['name', 'id']).reset_index(drop=True)
    df['class'] = pd.factorize(df['name'])[0]
    df.to_csv(filename, index=False)
    print('final file saved to', filename)

def main():

    root_dir = "./lfw"
    filename = "train_dataset.csv"
    files = glob.glob(root_dir + "/*/*")

    div = len(files) // 4

    chunk1 = files[0:div]
    chunk2 = files[div:div + div]
    chunk3 = files[div + div:div + div + div]
    chunk4 = files[div + div + div:]

    generate_set(chunk1, 'chunk1', filename)
    generate_set(chunk2, 'chunk2', filename)
    generate_set(chunk3, 'chunk3', filename)
    generate_set(chunk4, 'chunk4', filename)


main()