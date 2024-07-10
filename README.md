# File-Manipulator
コマンドライン引数を受け取り、引数によって異なる処理を実行するプログラム。

# 引数
・reverse inputpath outputpath:
　inputpath にあるファイルを受け取り、outputpath に inputpath の内容を逆にした新しいファイルを作成します。

・copy inputpath outputpath:
　inputpath にあるファイルのコピーを作成し、outputpath として保存します。

・duplicate-contents inputpath n:
　inputpath にあるファイルの内容を読み込み、その内容をinputpath に n 回複製します。

・replace-string inputpath str1 str2:
　inputpath にあるファイルの内容から文字列 str1 を検索し、str1 を全て str2 に置き換えます。
