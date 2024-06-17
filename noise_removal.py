import os
import subprocess
import tempfile
from moviepy.editor import VideoFileClip, AudioFileClip
import spleeter

def noiseremoval(video_name, output_path):
    # Create a temporary directory for spleeter output
    with tempfile.TemporaryDirectory() as temp_dir:
        # Construct the spleeter command
        command = ["spleeter", "separate", "-o", temp_dir, "-c", "mp3", video_name]
        try:
            # Run the spleeter command
            result = subprocess.run(command, capture_output=True, text=True, check=True)
        except subprocess.CalledProcessError as e:
            raise Exception(f"Spleeter failed with error: {e.stderr}")
        except FileNotFoundError as e:
            raise Exception(f"Spleeter executable not found: {e}")

        # Load the video clip without audio
        clip = VideoFileClip(video_name).without_audio()

        # Construct the path to the extracted vocals audio file
        audio_path = os.path.join(temp_dir, os.path.basename(video_name)[:-4], 'vocals.mp3')

        # Load the audio clip
        audioclip = AudioFileClip(audio_path)

        # Set the audio to the video clip
        clip = clip.set_audio(audioclip)

        # Write the final video file to the output path
        clip.write_videofile(output_path)

    return True
# video_file=r"/content/drive/MyDrive/integreation/singer.mp4"
# noiseremoval="noise_remove.mp4"
# noiseremoval()
