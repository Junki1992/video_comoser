# 動画圧縮ツール

## 概要
このツールは、指定したディレクトリ内全ての動画ファイルを圧縮し、ファイルサイズを削減します。FFmpegを使用して、動画の解像度やビットレートを調整します。

## 使い方
1. 必要なライブラリをインストール
'''bash
pip install ffmpeg-python
'''
2. FFmpegをインストール
このツールは、動画の圧縮にFFmpegを使用します。FFmpegをインストールしてください。
・Windowsの場合: FFMpeg公式サイトからダウンロードし、パスを通します。
・macOSの場合: 以下のコマンドを使用してインストールできます。
brew install ffmpeg
・Linuxの場合: 以下のコマンドを使用してインストールできます。
sudo apt update
sudo apt install ffmpeg

3. スクリプトを実行
python video_compressor.py