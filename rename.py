#!/usr/bin/env python
import sys
import os
import glob
from typing import Any
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS

RENAME_FORMAT = "%Y%m%d_%H%M%S"  # 新しいファイル名


def read_exif(exif: dict[int, Any], tag_name: str) -> Any:
    """exifの辞書から値を取得する"""
    for tag, value in exif.items():
        if TAGS.get(tag, tag) == tag_name:
            return value
    return None


def convert_format(dt_str: str, format: str) -> str:
    """「%Y:%m:%d %H:%M:%S」形式の日付文字列を別の形式に変換する"""
    return datetime.strptime(dt_str, '%Y:%m:%d %H:%M:%S').strftime(format)


def rename_path(file_path: str, new_name: str) -> str:
    """file_pathのファイル名をnew_nameに変更する"""
    path, name = os.path.split(file_path)
    _, ext = os.path.splitext(name)
    return f"{path}/{new_name}{ext}"


def main():
    # パラメータチェック
    if len(sys.argv) == 1:
        print("Usage: rename.py path")
        return
    # ディレクトリチェック
    tgt_path = sys.argv[1]
    if not os.path.exists(tgt_path):
        print(f"【Directory not found】 {tgt_path}")
        return
    for file_path in sorted(glob.glob(f"{tgt_path}/*")):
        if os.path.isdir(file_path):
            continue
        # 画像からexifを取得
        try:
            with Image.open(file_path) as image:
                exif = image._getexif()
        except:
            continue
        if not exif:
            print(f"【Exifdate not found】 {file_path}")
            continue
        # 撮影日時を取得
        dt_original = read_exif(exif, "DateTimeOriginal")
        if not dt_original:
            print(f"【DateTimeOriginal not found】 {file_path}")
            continue
        # 撮影日時から新しいファイル名を取得
        converted_dt = convert_format(dt_original, RENAME_FORMAT)
        renamed_path = rename_path(file_path, converted_dt)
        # 同名のファイルが存在する場合は変更しない
        if renamed_path in glob.glob(f"{tgt_path}/*"):
            continue
        os.rename(file_path, renamed_path)
        print(f"{file_path} → {renamed_path}")


if __name__ == '__main__':
    main()
