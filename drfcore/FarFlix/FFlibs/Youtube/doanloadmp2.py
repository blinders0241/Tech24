import os
import pytube
import subprocess

def download_video(url, output_path):
    # Create a YouTube object
    youtube = pytube.YouTube(url)

    # Get the highest resolution video stream
    video_stream = youtube.streams.get_highest_resolution()

    # Download the video
    video_stream.download(output_path=output_path)

def convert_to_mp3(input_file, output_file):
    # Run FFmpeg to convert the video file to MP3
    subprocess.call(['ffmpeg', '-i', input_file, output_file])

# Example usage
video_url = 'https://www.youtube.com/watch?v=2OvZtdwe30s'
output_directory = './output'
output_filename = 'video.mp4'
output_file_path = os.path.join(output_directory, output_filename)

# Download the video
download_video(video_url, output_directory)

# Convert the downloaded video to MP3
output_mp3_filename = 'audio.mp3'
output_mp3_file_path = os.path.join(output_directory, output_mp3_filename)
convert_to_mp3(output_file_path, output_mp3_file_path)

print('Video downloaded and converted to MP3 successfully.')
