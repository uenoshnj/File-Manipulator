import sys

def main():
    args = sys.argv
    argValidateCheck(args)
    executeFunc(args)


# 引数チェック
def argValidateCheck(argument):
    if len(argument) < 4:
        raise ValueError("Usage: python3 file_manipulator.py <arg1> <arg2> <arg3>(If arg1 is 'replace-string', add <arg4>)")
    elif argument[1] == "replace-string" and len(argument) < 5:
        raise ValueError("Usage: python3 file_manipulator.py <arg1> <arg2> <arg3> <arg4>")

# 引数１の値をもとに関数を実行
def executeFunc(args):
    func = args[1]

    if func == "reverse":
        reverse(args[2], args[3])
    elif func == "copy":
        copy(args[2], args[3])
    elif func == "duplicate-contents":
        duplicateContents(args[2], args[3])
    elif func == "replace-string":
        replaceString(args[2], args[3], args[4])

# インプットファイルの文字を反転する
def reverse(inputpath, outputpath):
    list = []
    with open(inputpath, 'r') as input:
        list = input.read().splitlines()

    with open(outputpath, 'w') as output:
        for i in range(len(list) - 1, -1, -1):
            for j in range(len(list[i]) - 1, -1, -1):
                output.write(list[i][j])
            output.write("\n")

# インプットファイルの内容をコピーする
def copy(inputpath, outputpath):
    with open(inputpath, 'r') as input:
        contents = input.read()
    
    with open(outputpath, 'w') as output:
        output.write(contents)

# インプットファイルの内容を指定した回数複製する
def duplicateContents(inputpath, n):
    with open(inputpath, 'w') as input:
        contents = input.read()
        for i in range(n+1):
            input.write(contents)

# インプットファイル内の指定した文字列を指定した文字列に変換する
def replaceString(inputpath, targetStr, replaceStr):
    lines = []
    with open(inputpath, 'r') as input:
        lines = input.read().splitlines()
    
    res = []
    for i in range(len(lines)):
        tgt = lines[i].find(targetStr)
        if tgt != -1:
            while tgt != -1:
                content = lines[i][:tgt] + replaceStr
                tgt = lines[i][tgt + len(targetStr) + 1].find(targetStr)
                res.append(content)
            res.append(lines[i][tgt + 1:])
        else:
            res.append(lines[i])
        res.append('\n')
    
    with open(inputpath, 'w') as input:
        input.write(res)

main()