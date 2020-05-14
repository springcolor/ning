# -*- coding: utf-8 -*
import os
import shutil


# 盘符大小写注意了


def read_tx_name(root_dir):
    lines = []
    with open(root_dir, 'r') as file_to_read:
        while True:
            line = file_to_read.readline()
            if not line:
                break
            line = line.strip('\n')
            lines.append(line)
    return lines


def write_tx_name(root_dir, lines):
    with open(root_dir, 'w') as file_to_write:
        for lin in lines:
            file_to_write.write(lin+".fs1\n")
    # with open(root_dir, 'a') as file_to_add:
    #     file_to_add.write(lin + "Add a word\n")


def sys_out(my_list):
    for lines in my_list:
        print(lines)


def search_file(path, str, other):  # other传-1时为相对路径，否则为相对路径
    for file in os.listdir(path):
        this_path = os.path.join(path, file)
        if os.path.isfile(this_path):
            filename = os.path.splitext(file)[0]
            # print(type(os.path.splitext(file)[0]))
            # if this_path.find(str) != -1:
            # if file.find(str) != -1:
            # print('\033[0;95m' + os.path.splitext(file)[0] + '\033[0m')
            print('\033[0;95m' + os.path.splitext(file)[0] + '\033[0m')
            if filename == str:
                # print('This is a \033[1;34m' + str + '\033[0m!')
                print('This is a' + str)
                if other == -1:
                    the_path = this_path.replace(Path, "")[1:]
                    Aggregate_list.append(the_path)
                else:
                    Aggregate_list.append(this_path)
                    # print(Aggregate_list)
        else:
            search_file(this_path, str, 1)
    return Aggregate_list


def all_path(dirname):
    result = []
    for maindir, subdir, file_name_list in os.walk(dirname):
        for filename in file_name_list:
            apath = os.path.join(maindir, filename)
            result.append(apath)
    return result


def GetExtNamesList(fileslist, ext):
    filenames = []
    for file in fileslist:
        # fileinfo = os.path.splitext(file)[0:]
        fileinfo = file.split('.')[0:]
        print(fileinfo)
        if fileinfo[1] == ext:
            filenames.append(file)
    return filenames


if __name__ == '__main__':
    # read
    result_path = r'c:\Users\Admin\Desktop\wosi\c.txt'
    lines_list = read_tx_name(result_path)
    sys_out(lines_list)

    # write
    result_path1 = r'c:\Users\Admin\Desktop\wosi\c1.txt'
    write_tx_name(result_path1, lines_list)

    # read_again
    result_path = r'c:\Users\Admin\Desktop\wosi\c1.txt'
    lines_list = read_tx_name(result_path)
    sys_out(lines_list)

    # listen
    Path = r"c:\Users\Admin\Desktop\wosi1"
    path = r"c:\Users\Admin\Desktop\wosi"
    str_name_one = "p5"
    # Aggregate_list_all = []
    Aggregate_list = []
    for str_name in lines_list:
        search_file(path, str_name, 1)
        # Aggregate_list_all.append(Aggregate_list)
    print("111111111111111111111")
    print(Aggregate_list)
    # copy
    sourcefolder = r'c:\Users\Admin\Desktop\wosi'
    # sourcefolder = 'c:\\Users\\Admin\\Desktop\\a'
    desfolder = r'c:\Users\Admin\Desktop\wosi1'
    # desfolder = 'c:\\Users\\Admin\\Desktop\\b'
    print('=============================2')
    for file in Aggregate_list:
        print(file)
        desfilename = file.replace(sourcefolder, desfolder)
        # print(desfilename)
        desfilename = desfilename.replace('\\', '/')
        print(desfilename)
        if not os.path.exists(os.path.dirname(desfilename)):
            os.makedirs(os.path.dirname(desfilename))
        if not os.path.exists(desfilename):
            shutil.copy(file, desfilename)  # 如果要改为移动，而不是拷贝，可以将copy改为move
