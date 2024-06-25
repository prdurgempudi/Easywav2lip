import os
import subprocess
import inference
import run_program
import subprocess

def run_model(video_file, vocal_file,quality):
  run_program.save_easy_wav2lip_config(
    video_file,
    vocal_file,  # Optional
    quality,
    output_height="full resolution",
    use_previous_tracking_data=True,
    wav2lip_version="Wav2Lip_GAN",
    nosmooth=True,
    )
  subprocess.run(['python', 'run.py' ])
        # '--checkpoint_path', checkpoint_path,
#         '--face', face_path,
#         '--audio', audio_path,
#         '--outfile', output_path,
#         '--quality', 'Fast',
#         '--out_height', '720'
    # ])
  return True
video_file='preeti_zinta_hi.mp4' #'/content/drive/MyDrive/integreation/Easy-Wav2Lip/Priyanka_Chopra_input.mp4'
vocal_file='preeti_zinta_hi.mp4' #'/content/drive/MyDrive/integreation/Easy-Wav2Lip/temp.wav'
quality='Enhanced'
run_model(video_file, vocal_file,quality)
# def run_inference(checkpoint_path, face_path, audio_path,output_path):
#     # Change directory to Easy-Wav2Lip
#     os.chdir('/content/drive/MyDrive/integreation/Easy-Wav2Lip')
#     # output_path="result_voice.mp4"
#     # Run the inference command
#     subprocess.run([
#         'python', 'inference.py',
#         '--checkpoint_path', checkpoint_path,
#         '--face', face_path,
#         '--audio', audio_path,
#         '--outfile', output_path,
#         '--quality', 'Fast',
#         '--out_height', '720'
#     ])
#     return True
    # # Check if the detected face file exists and delete it
    # if os.path.isfile(detected_face_file):
    #     os.remove(detected_face_file)
    #     print(f"{detected_face_file} has been deleted.")
    # else:
    #     print(f"{detected_face_file} not found.")

# if __name__ == "__main__":
#     # Define the paths
#     checkpoint_path = '/content/drive/MyDrive/integreation/Easy-Wav2Lip/checkpoints/wav2lip_gan.pth'
#     face_path = r'/content/drive/MyDrive/integreation/Easy-Wav2Lip/singer.mp4'
#     audio_path = r'/content/drive/MyDrive/integreation/Easy-Wav2Lip/translated.wav'
#     output_path = '/content/drive/MyDrive/singer_test_3.mp4'
#     # detected_face_file = '/content/drive/MyDrive/wav2lip/Easy-Wav2Lip/last_detected_face.pkl'

#     # Call the function with the defined paths
#     run_inference(checkpoint_path, face_path, audio_path, output_path)




# import os
# import subprocess

# def run_inference():
#     # Define the paths
#     # checkpoint_path = '/content/drive/MyDrive/integreation/Easy-Wav2Lip/checkpoints/wav2lip_gan.pth'
#     # face_path = '/content/drive/MyDrive/integreation/Easy-Wav2Lip/singer.mp4'
#     # audio_path = '/content/drive/MyDrive/integreation/Easy-Wav2Lip/singer_tel.wav'
#     # output_path = '/content/drive/MyDrive/singer_test33.mp4'
#     # detected_face_file = '/content/drive/MyDrive/wav2lip/Easy-Wav2Lip/last_detected_face.pkl'

#     # Change directory to Easy-Wav2Lip

#     # Run the inference command
#     subprocess.run([
#         'python', 'inference.py',
#         '--checkpoint_path', checkpoint_path,
#         '--face', face_path,
#         '--audio', audio_path,
#         '--outfile', output_path,
#         '--quality', 'Improved',
#         '--out_height', '720'
#     ])

#     # # Check if the detected face file exists and delete it
#     # if os.path.isfile(detected_face_file):
#     #     os.remove(detected_face_file)
#     #     print(f"{detected_face_file} has been deleted.")
#     # else:
#     #     print(f"{detected_face_file} not found.")

# if __name__ == "__main__":
    
#     checkpoint_path = '/content/drive/MyDrive/integreation/Easy-Wav2Lip/checkpoints/wav2lip_gan.pth'
#     face_path = '/content/drive/MyDrive/integreation/Easy-Wav2Lip/singer.mp4'
#     audio_path = '/content/drive/MyDrive/integreation/Easy-Wav2Lip/singer_tel.wav'
#     output_path = '/content/drive/MyDrive/singer_test444.mp4'
#     # detected_face_file = '/content/drive/MyDrive/wav2lip/Easy-Wav2Lip/last_detected_face.pkl'

#     run_inference(checkpoint_path, face_path, audio_path, output_path)