import sys

def main():
    args = sys.argv
    argValidateCheck(args)


def argValidateCheck(argument):
    if len(argument) < 4:
        raise ValueError("Usage: python3 file_manipulator.py <arg1> <arg2> <arg3>(If arg1 is 'replace-string', add <arg4>)")
    elif argument[1] == "replace-string" and len(argument) < 5:
        raise ValueError("Usage: python3 file_manipulator.py <arg1> <arg2> <arg3> <arg4>")


def funcCheck(args):
    func = args[1]

    if func == "reverse":
        reverse(args[2], args[3])
    elif func == "copy":
        copy(args[2], args[3])
    elif func == "duplicate-contents":
        duplicateContents(args[2], args[3])
    elif func == "replace-string":
        replaceString(args[2], args[3], args[4])


def reverse(inputpath, outputpath):
    list = []
    with open(inputpath, 'r') as input:
        list = input.read().splitlines()

    with open(outputpath, 'w') as output:
        for i in range(len(list) - 1, -1, -1):
            for j in range(len(list[i]) - 1, -1, -1):
                output.write(list[i][j])
            output.write("\n")


def copy(inputpath, outputpath):
    with open(inputpath, 'r') as input:
        contents = input.read()
    
    with open(outputpath, 'w') as output:
        output.write(contents)


def duplicateContents(inputpath, n):
    with open(inputpath, 'w') as input:
        contents = input.read()
        for i in range(n+1):
            input.write(contents)


def replaceString(inputpath, targetStr, replaceStr):
    with open(inputpath, 'r') as input:
        

