import os
import subprocess
import ffmpeg
class VideoMerger:
    def __init__(self, src_folder, dest_folder):
        self.src_folder = src_folder
        self.dest_folder = dest_folder

    # def merge_videos(self, video1, video2):
    #     # Merge videos

    #     input1 = ffmpeg.input(os.path.join(self.src_folder, video1))
    #     input2 = ffmpeg.input(os.path.join(self.src_folder, video2))
    #     print("########",type(input1))
    #     print("########",input1)
    #     merged_video = ffmpeg.concat(input1,input2, v=1, a=1).output(output_file)

    #         # Check if the command was successful
    #     if ffmpeg.run(merged_video):
    #         print(f'Merged video saved at {output_file}')
    #     else:
    #         print('Error: Failed to merge videos')
    #         print(f'Merged video saved at {output_file}')
            
    def merge_videos(self,video1, video2, output_path=""):
        try:
            output_file = os.path.join(self.dest_folder, 'merge_video.mp4')
            input1 = ffmpeg.input(os.path.join(self.src_folder, video1))
            input2 = ffmpeg.input(os.path.join(self.src_folder, video2))
        except Exception as e:
            print(e)
        

        # Get the video and audio streams from both inputs
        video1 = input1.video
        audio1 = input1.audio
        video2 = input2.video
        audio2 = input2.audio

        # Concatenate the video and audio streams
        tmpVideo = os.path.join(self.dest_folder,'temp_video.mp4')
        print("#######",tmpVideo)
        tmpAudio = os.path.join(self.dest_folder,'temp_audio.mp4')
        merged_video = ffmpeg.concat(video1, video2, v=1, a=0).output(tmpVideo)
        merged_audio = ffmpeg.concat(audio1, audio2, v=0, a=1).output(tmpAudio)
        
        print("#######",merged_video)

        # Run the commands
        ffmpeg.run(merged_video)
        ffmpeg.run(merged_audio)

        # Merge the temporary video and audio files
        input_video = ffmpeg.input('temp_video.mp4')
        input_audio = ffmpeg.input('temp_audio.mp4')
        final_output = ffmpeg.output(input_video, input_audio, output_path)
        ffmpeg.run(final_output)




# Example usage
merger = VideoMerger(r'C:\Users\simpl\Videos\Source', r'C:\Users\simpl\Videos\DestinationMerge')
merger.merge_videos('Fair.Play.DanceWelcome.mp4', 'I_WannaSeeYouDance.mp4')
