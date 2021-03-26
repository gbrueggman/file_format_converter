import os


def main():
    new_ext = ".jpg"

    folder_path = "/Users/gbrueggman/Documents/_School/CMU/2021_Spring/16681_MRSD_Project_1/Salus/hotspot_custom_dataset/"
    folder = os.listdir(folder_path)
    num_files = len(folder)
    idx = 1
    for filename in folder:
        print("Converting %s/%s" % (idx, num_files))
        idx += 1

        filename_base = os.path.splitext(filename)[0]
        file_path_orig = folder_path + filename
        file_path_des = folder_path + filename_base + new_ext
        os.rename(file_path_orig, file_path_des)


if __name__ == '__main__':
    main()
