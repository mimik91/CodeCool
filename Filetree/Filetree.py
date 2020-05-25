import os


def print_decorline(chars, length):
    decorline = ""
    while len(decorline) < length:
        decorline += chars
    print(decorline)


def file_filer(files, path):
    files_filtered=[]
    for item in files:
        if not item.endswith('.py'):
            files_filtered=files_filtered+[item]
    return files_filtered


def filetree(root, path=""):

    # Stop if this is not a folder:
    if not os.path.isdir(root):
        return

    # Get files in current folder:
    files = sorted(os.listdir(root))
    files_filtered = file_filer(files, path)
    len_files = len(files_filtered)

    # Print the content of the current folder:
    newpath = path + "|   "
    arrow = "|-- "
    for i in range(len_files):
        if i == len_files - 1:
            newpath = path + "    "
            arrow = "`-- "
        print("{}{}{}".format(path, arrow, files_filtered[i]))
        # Recursive call to print the content of sub-folders:
        if os.path.isdir("{}/{}".format(root, files_filtered[i])):
            filetree("{}/{}".format(root, files_filtered[i]), newpath)



def main():
    print("The contents of the current folder are:")
    print_decorline("*--*", 30)
    filetree(".")
    print_decorline("*--*", 30)


if __name__ == '__main__':
    main()