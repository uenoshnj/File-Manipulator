import sys

def main():
    args = sys.argv
    argValidateCheck(args)
    executeFunc(args)


# 引数チェック
def argValidateCheck(argument):
    argLength = len(argument)

    # 引数の個数チェック
    if argLength < 4:
        raise ValueError("Usage: python3 file_manipulator.py <arg1> <arg2> <arg3>(If arg1 is 'replace-string', add <arg4>)")
    
    # 1つめの引数のチェック
    arg1Lists = ["reverse", "copy", "duplicate-contents", "replace-string"]
    arg1 = argument[1]
    if arg1 not in arg1Lists:
        raise ValueError(f"invalid argument '{arg1}'. Must be one of 'reverse', 'copy', 'duplicate-contents', 'replace-string'.")
    
    # 1つめの引数がreplace-stringの場合のチェック
    if arg1 == "replace-string" and argLength < 5:
        raise ValueError(f"Usage: python3 file_manipulator.py {arg1} <arg2> <arg3> <arg4>")


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
    with open(inputpath, 'r') as input:
        contents = input.read()
        
    with open(inputpath, 'w') as input:
        for i in range(int(n)+1):
            input.write(contents)


# インプットファイル内の指定した文字列を別の指定した文字列に変換する
def replaceString(inputpath, targetStr, replaceStr):
    print(targetStr)
    print(replaceStr)
    with open(inputpath, 'r') as input:
        contents = input.read()
    
    newContents = contents.replace(targetStr, replaceStr)

    with open(inputpath, 'w') as input:
        input.write(newContents)

main()
