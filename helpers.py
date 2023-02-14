from os import listdir


def find_csv_filenames( path_to_dir, suffix=".txt" ):
    filenames = sorted(listdir(path_to_dir))
    return [ filename for filename in filenames if filename.endswith( suffix ) ]
