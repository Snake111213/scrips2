import collections
import fileinput
import os
from pstats import Stats

def find_files(path='.', ext= '.py'):
    for root, dirs, filenames in os.walk(path):
        for filename in filename:
            if filename.endswith(ext):
                yield(os.path.join(root, filename))

def is_line(line):
    return True

def has_class(line):
    return line.startswith('class')

def has_funcion(line):
    return 'def ' in line

COUNTERS = dict(lines=is_line, classes=has_class, function=has_funcion)


def find_gods():
    stats = collections.defaultdict(collections.Counter)
    for line in fileinput.input(find_files()):
        for key, func in COUNTERS.items():
            if func(line):
                stats[key][fileinput.filename()] += 1 
    
    for filename, lines in stats['lines'].most_common():
        classes = stats['classes'][filename]
        functions = stats['functions'][filename]

        try:
            ratio = "=> {0}:1".format(function / classes)
        except ZeroDivisionError:
            ratio = "=> n/a"
        print (filename, lines, functions, classes, ratio)

if __name__=='__main__':
    find_gods