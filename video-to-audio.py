import os
import subprocess


def convert_video_to_mp3(input_file, output_file):
    ffmeg_cmd = [
        'ffmpeg',
        "-i", input_file,
        "-vn",
        "-acodec", "libmp3lame",
        "-ab", "192k",
        "-ar", "44100",
        "-y",
        output_file
    ]

    try:
        subprocess.run(ffmeg_cmd, check=True)
        print("Successfully Converted!!")
    except subprocess.CalledProcessError as e:
        print("Conversion failed!")

# convert_video_to_mp3("sample.mp4", "sample.mp3")
convert_video_to_mp3("sample.mp4", "sample.wav")
