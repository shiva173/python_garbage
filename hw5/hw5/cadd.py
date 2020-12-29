import os

def create_dirs():
    for i in range(1, 10):
        new_path = os.path.join(os.getcwd(), 'dir_{}'.format(i))
        os.mkdir(new_path)

def delete_dirs():
    for i in range(1, 10):
        new_path = os.path.join(os.getcwd(), 'dir_{}'.format(i))
        os.rmdir(new_path)
