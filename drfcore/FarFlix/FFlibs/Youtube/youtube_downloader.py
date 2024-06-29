import pytube
import ffmpeg
import sys
sys.path.append(r"C:\SIMPLY_Official\\2024\\TechHome24\drfcore\\FarFlix")

from FFlibs.Youtube.Globster import *

BASePath = Globster().returnBasePath() +  r"\media_downloaded"

output_video = BASePath + r'\video'
output_audio = BASePath + r'\audio'
DownloadPath = BASePath + r'\YoutubeDirectDownloads\\'

def on_progress(stream, chunk, bytes_remaining):
    """Callback function"""
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    pct_completed = bytes_downloaded / total_size * 100
    print(f"Status: {round(pct_completed, 2)} %")


def get_Stream(url):
    yt = pytube.YouTube(url, on_progress_callback=on_progress)
    title = yt.title
    title = title.replace("|", "_").replace(" ", ".")
    filename = title[0:25]
    return yt, filename


def get_best_quality(url, category="video"):
    yt, file_name = get_Stream(url)

    file_name = file_name.replace("(","")
    file_name = file_name.replace(".","_")
    file_name = file_name.replace("\"","")
    # print("#################")
    # print(file_name)
    streams = set()
    for stream in yt.streams.filter(type=category):  # Only look for video streams to avoid None values
        streams.add(stream.resolution)
    video_quality_list = list(streams)
    final_list = []
    for item in video_quality_list:
        if item.isalnum():
            item = item.replace('p', '')
            # print(item)
            final_list.append(int(item))
        else:
            final_list = video_quality_list
    best_quality = sorted(final_list, key=int, reverse=True)[0]
    print(best_quality)
    print(str(best_quality))
    return str(best_quality)


def download_video(url):
    best = get_best_quality(url)
    yt, file_name = get_Stream(url)
    
    file_name = file_name.replace("(","")
    file_name = file_name.replace(".","_")
    file_name = file_name.replace("\"","")
    tmp_video = yt.streams.filter(res=get_best_quality(url) + 'p', progressive=False).first().download(
        output_path=output_video, filename=file_name + '.mp4')
    video = ffmpeg.input(tmp_video)
    return video


def download_audio(url):
    yt, file_name = get_Stream(url)
    file_name = file_name.replace("(","")
    file_name = file_name.replace(".","_")
    file_name = file_name.replace("\"","")
    
    if yt.streams.get_by_itag(251):
        print("Downloading Best Audio Available")
        yt.streams.get_by_itag(251).download(output_path=output_audio, filename=file_name + '.mp3')
        audio = ffmpeg.input(
            yt.streams.get_by_itag(251).download(output_path=output_audio, filename=file_name + '.mp3'))
        return audio

    else:
        audio = ffmpeg.input(
            yt.streams.filter(abr="160kbps", progressive=False).first().download(output_path=output_audio,
                                                                                 filename=file_name + '.mp3'))
        return audio


def merge_Audio_Video(url):
    yt, file_name = get_Stream(url)
    file_name = file_name.replace("(","")
    file_name = file_name.replace(".","_")
    file_name = file_name.replace("\"","")
    video = download_video(url)
    audio = download_audio(url)
    print("########")
    print(DownloadPath)
    # ffmpeg.concat(video, audio, v=1, a=1).output('finished_video.mp4').run(overwrite_output=True)
    ffmpeg.output(audio, video, DownloadPath + file_name + ".mp4").run(overwrite_output=True)
        # Delete intermediate files
    # os.remove(video)


def download_videos(urls, resolution):
    for url in urls:
        download_video(url)


def download_playlist(url):
    playlist = pytube.Playlist(url)
    download_videos(playlist.video_urls)


def choose_resolution(resolution):
    print("#######Resolution Received:",resolution)
    if resolution in ["low", "360", "360p"]:
        itag = 18
    elif resolution in ["medium", "720", "720p", "hd"]:
        itag = 22
    elif resolution in ["b", "1080", "1080p", "fullhd", "full_hd", "full hd"]:
        itag = 137
    elif resolution in ["bb", "2160", "2160p", "4K", "4k"]:
        itag = 313
    else:
        itag = 18
    return itag


def input_links():
    print("Enter the links of the videos (end by entering 'STOP'):")
    links = []
    link = ""
    while link != "STOP" and link != "stop":
        link = input()
        links.append(link)
    links.pop()
    return links
