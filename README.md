# rename

フォルダ内の画像ファイルの名前を一括で変更するツールです。  
画像ファイルから撮影日時を取得して、指定したフォーマットのファイル名に変更します。  
新しい名前と同名のファイルが存在する場合はファイル名を変更しません。  

# 使い方

```
$ ls -1 ./Pictures/
0001.jpg
0002.jpg
0003.jpg
$ rename.py ./Pictures/
./Pictures/0001.jpg → ./Pictures/20150116_182236.jpg
./Pictures/0002.jpg → ./Pictures/20170615_131002.jpg
./Pictures/0003.jpg → ./Pictures/20201023_114017.jpg
```
