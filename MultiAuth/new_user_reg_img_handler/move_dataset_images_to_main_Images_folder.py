import argparse
import os
import shutil
import numpy as np


# This prog moves the training data from the temp directory to the target folder when the user agrees to
# save the train data
# todo: ensure when registering the user tests how well the program identifies his face and should
# allow retry in saving the data again. a retry will clear the temp directory to start-a-new
# todo: write a mini face recognition to test how well user's face is deectable with a match percentage
# displayed at top end


def get_files_from_folder(path):
    files = os.listdir(path)
    return np.asarray(files)


def main(path_to_data, path_to_test_data, train_ratio):
    # get dirs
    global path_to_origin
    _, dirs, _ = next(os.walk(path_to_data))

    # calculates how many train data per class
    data_counter_per_class = np.zeros(len(dirs))

    for i in range(len(dirs)):
        path = os.path.join(path_to_data, dirs[i])
        # print("path to durs %s"%path)
        files = get_files_from_folder(path)
        # print("gotten files are %s"%files)

        # Forms a matrix from the classes containing the number of images in that directory

        data_counter_per_class[i] = len(files)
        # print(data_counter_per_class)
        test_counter = np.round(data_counter_per_class * (1 - train_ratio))
        # print(test_counter)
    # transfer files

    for i in range(len(dirs)):
        path_to_origin = os.path.join(path_to_data, dirs[i])
        # print(path_to_origin)
        path_to_save = os.path.join(path_to_test_data, dirs[i])
        # print("The path to save is %s"%path_to_test_data)
        print(path_to_save)

    # creates dir
    if not os.path.exists(path_to_save):
        # global path_to_save
        os.makedirs(path_to_save)
        files = get_files_from_folder(path_to_origin)
        # file = get_files_from_folder("images/Happy/")
        print(files.all())

    # moves data
    for j in range(int(test_counter[i])):
        dst = os.path.join(path_to_save, files[j])
        print(dst)
        src = os.path.join(path_to_origin, files[j])
        print(src)
        shutil.move(src, dst)

    # def parse_args():
    #     parser = argparse.ArgumentParser(description="Dataset divider")
    #
    #     parser.add_argument("--data_path", required=True, help="Path to data")
    #     parser.add_argument("--test_data_path_to_save", required=True, help="Path to test data where to save")
    #     parser.add_argument("--train_ration", required=True,
    #                         help="70% Train ratio-0.7 means splitting data in 70% train and 30% test")
    #
    #     return parser.parse_args()


if __name__ == "__main__":
    # args = parse_args()
    args = argparse
    datapath = "images/"
    dest_path = "../img_tmp_dir/cheserem"
    main(datapath, dest_path, 0.7)
    # main(args.data_path, args.test_data_path_to_save, float(args.train_ratio))
