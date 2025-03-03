import os
import ffmpeg

def compress_video(input_file, output_file, crf=23, resolution="1280x720", bitrate="1500k"):
    """
    動画を圧縮する関数

    :param input_file: 入力動画ファイルのパス
    :param output_file: 出力動画ファイルのパス
    :param crf: 圧縮率（0-51、低いほど高画質、デフォルト=23）
    :param resolution: 解像度（例：'1280x720'）
    :param bitrate: ビットレート（例：'1500k'）
    """
    try:
        # FFmpegコマンドを実行して動画を圧縮
        ffmpeg.input(input_file).output(output_file, vcodec="libx264", crf=crf, s=resolution, b=bitrate).run()
        print(f"動画の圧縮が完了いたしました!出力ファイル: {output_file}")
    except ffmpeg.Error as e:
        print(f"エラーが発生しました: {e}")

def compress_video_in_directory(input_dir, output_dir, crf=23, resolution="1280x720", bitrate="1500k"):
    """
    ディレクトリ内の動画ファイルを圧縮する関数

    :param input_dir: 入力ディレクトリのパス
    :param output_dir: 出力ディレクトリのパス
    :param crf: 圧縮率（0-51、低いほど高画質、デフォルト=23）
    :param resolution: 解像度（例：'1280x720'）
    :param bitrate: ビットレート（例：'1500k'）
    """
    # 出力ディレクトリが存在しない場合は作成
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 入力ディレクトリ内の動画ファイルを検索 (拡張子が動画ファイル)
    video_extensions = (".mp4", ".mov", ".avi", ".mkv") # 対応する動画ファイルの拡張子
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(video_extensions):
            input_file_path = os.path.join(input_dir, filename)
            output_file_path = os.path.join(output_dir, f"compressed_{filename}")
            compress_video(input_file_path, output_file_path, crf, resolution, bitrate)

input_directory = "./input"
output_directory = "./output"

compress_video_in_directory(input_directory, output_directory)