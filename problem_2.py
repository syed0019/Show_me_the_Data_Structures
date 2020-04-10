import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    # if suffix is empty or nothing is provided
    if suffix is None or suffix is '':
        print('suffix is not provided.')
    # if there is no directory in current path
    elif not os.path.isdir(path):
        if suffix == path[-2:]:
            print(path)
    # if there is a directory, diving into it to find file
    elif os.path.isdir(path) == True:
        # iterating through directory list
        for folder in os.listdir(path):
            # using recursive approach to call function
            find_files(suffix, os.path.join(path, folder))

###### Test Cases ######
print('Test Case 1:')
find_files('.h', './testdir')
# would print below output:
# ./testdir\subdir1\a.h
# ./testdir\subdir3\subsubdir1\b.h
# ./testdir\subdir5\a.h
# ./testdir\t1.h
print('\n')

print('Test Case 2:')
find_files('.c', './testdir')
# would print below output:
# ./testdir\subdir1\a.c
# ./testdir\subdir3\subsubdir1\b.c
# ./testdir\subdir5\a.c
# ./testdir\t1.c
print('\n')

print('Test Case 3:')
find_files('', './testdir')
# would print 'suffix is not provided.'