# encoding:utf-8
import os


def write_file(path, content, append=False):
    model = 'a' if append else 'w'
    with open(path, model, newline='') as f:
        f.write(content + os.linesep)


