import youtube_downloader
import file_converter
print('''
(1) Download YouTube Videos Manually
(2) Download a YouTube Playlist
(3) Download YouTube Videos and Convert Into MP311
''')
choice = input("Choice: ")
if choice == "1" or choice == "2":
    if choice == "2":
        link = input("Enter the link to the playlist: ")
        print("Downloading playlist...")
        youtube_downloader.download_playlist(link)
        print("Download finished!")
    if choice == "1":
        links = youtube_downloader.input_links()
        for link in links:
            youtube_downloader.merge_Audio_Video(link)
            print("Download finished!")
    elif choice == "3":
        links = youtube_downloader.input_links()
        for link in links:
            print("Downloading...")     
            filename = youtube_downloader.download_video(link)
            print("Converting...")
            file_converter.convert_to_mp3(filename)
    else:
        print("Invalid input! Terminating...")