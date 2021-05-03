import sys
import pathlib
# base.pyのあるディレクトリの絶対パスを取得
current_dir = pathlib.Path(__file__).resolve().parent
parent_dir = current_dir.joinpath('..')
# モジュールのあるパスを追加
sys.path.append( str(parent_dir) )

# sys.path.insert(0,'../')
# sys.path.append('../')
# print(sys.path)
from hello import hello

def test_hello_default(capsys):
    hello()
    out, err = capsys.readouterr()
    assert out == "Hello,World!\n"

def test_hello_with_name(capsys):
    hello("サザエ")
    hello("カツオ")
    out, err = capsys.readouterr()
    assert out == "Hello,サザエ!\n" "Hello,カツオ!\n"