import os
import shutil
from base64 import b64encode
import moviepy.editor as mp
import cv2
import os
from flask import Flask, request, session, send_file, render_template
from werkzeug.utils import secure_filename
import audio_video_handler
import pathlib
import subprocess
from pathlib import Path

# def get_video_resolution(video_path):
#     """Function to get the resolution of a video"""
#     video = cv2.VideoCapture(video_path)
#     width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
#     height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
#     return (width, height)

# def resize_video(video_path, new_resolution):
#     """Function to resize a video"""
#     video = cv2.VideoCapture(video_path)
#     fourcc = int(video.get(cv2.CAP_PROP_FOURCC))
#     fps = video.get(cv2.CAP_PROP_FPS)
#     width, height = new_resolution
#     output_path = os.path.splitext(video_path)[0] + '_720p.mp4'
#     writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
#     while True:
#         success, frame = video.read()
#         if not success:
#             break
#         resized_frame = cv2.resize(frame, new_resolution)
#         writer.write(resized_frame)
#     video.release()
#     writer.release()


app = Flask(__name__, static_folder='static')
app.config['SECRET_KEY']="abcdefg"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/language', methods=['POST'])
def translate_text():
    try:
        selected_language = request.form.get('language')
        if selected_language in ['English_female','English_male','Hindi_female','Hindi_male','Bengali_male','Bengali_female','Gujarati_female','Gujarati_male','Kannada_female','Kannada_male','Malayalam_female','Malayalam_male','Marathi_female','Marathi_male','Punjabi_female','Punjabi_male','Tamil_female','Tamil_male','Telugu_female','Telugu_male']:  # Add more languages as needed
            session['selected_language'] = selected_language
            return "Language selected successfully"
        else:
            return "Invalid language selected", 400
    except KeyError:
        return "No language selected", 400


@app.route('/upload_video', methods=['POST'])
def upload_video():
    try:
        media_folder = "D:/new/sample_data"
        if not os.path.exists(media_folder):
            os.makedirs(media_folder)
        file = request.files['videoFile']
        filename = secure_filename(file.filename)
        extension = pathlib.Path(filename).suffix
        filename = 'uploaded' + extension
        destination = "/".join([media_folder, filename])
        # video_duration = mp.VideoFileClip(destination).duration
        # if video_duration > 360:
        #     print("WARNING: Video duration exceeds 60 seconds. Please upload a shorter video.")
        #     raise SystemExit(0)

        # video_resolution = get_video_resolution(destination)
        # print(f"Video resolution: {video_resolution}")
        # if video_resolution[0] >= 1920 or video_resolution[1] >= 1080:
        #     print("Resizing video to 720p...")
        #     os.system(f"ffmpeg -i {destination} -vf scale=1280:360 D:/new/sample_data/input_vid.mp4")
        #     destination = "D:/new/sample_data/input_vid.mp4"
        #     print("Video resized to 720p")
        # else:
        #     print("No resizing needed")
        # start = 35
        # end = 62
        # interval = end - start
        # ffmpeg_path= 'D:/new/Wav2Lip/ffmpeg.exe'
        # subprocess.run([ffmpeg_path, '-y', '-i', destination, '-ss', str(start), '-t', str(interval), '-async', '1', 'input_vid.mp4'])

        file.save(destination)
        return 'Video uploaded successfully'
    except Exception as e:
        return f'Error occurred: {e}', 500


@app.route('/generate', methods=['POST'])
def generate_result():
    try:
        print("covnerting video .. ")
        selected_language = session.get('selected_language')  # Get selected language from session
        if not selected_language:
            return "Language not selected. Please select a language first.", 400
        else:
            print( "Language selected")
        # Assuming convert_video accepts the language as an argument
        conversion=audio_video_handler.convert_video(language=selected_language)
        print("conversion .. completed .. ")
        if conversion:
            return "video genereated"
        else:
            return "error"
    except Exception as e:
        return f'Error occurred: {e}', 500

@app.route('/download_generated_video', methods=['GET'])
def get_generated_video():
    output_video_path ="D:/new/converted_videos/output.mp4" # Replace this with the actual path of the generated video
    try:
        return send_file(output_video_path, as_attachment=True)
    except:
        return "Generated video file not found!", 404

if __name__ == '__main__':
    app.run(debug=False, port=500)

# import os
# import pathlib
# from flask import Flask, request, session, send_file, render_template
# from werkzeug.utils import secure_filename
# import audio_video_handler

# app = Flask(__name__)
# app.config['SECRET_KEY'] = "abcdefg"

# # Configure the upload folder
# UPLOAD_FOLDER = "D:/new/sample_data"
# if not os.path.isdir(UPLOAD_FOLDER):
#     os.makedirs(UPLOAD_FOLDER)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# @app.route('/')
# def index():
#     return render_template('index1.html')

# @app.route('/language', methods=['POST'])
# def translate_text():
#     try:
#         selected_language = request.form.get('language')
#         if selected_language in ['en', 'hi', 'mr', 'te', 'ta', 'ml', 'kn', 'as', 'bn', 'bho', 'pa']:
#             session['selected_language'] = selected_language
#             return "Language selected successfully"
#         else:
#             return "Invalid language selected", 400
#     except Exception as e:
#         return f"Error: {e}", 500

# @app.route('/uploadImage', methods=['POST'])
# def imageUpload():
#     try:
#         selected_language = session.get('selected_language')
#         if not selected_language:
#             return "Error: Language not selected", 400
#         file = request.files['file']
#         if file:
#             filename = secure_filename(file.filename)
#             destination = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#             file.save(destination)
#             text = request.form.get('text')
#             audio_video_handler.convert_image(language=selected_language, text_input=text)
#             return 'Success: Image uploaded and processed'
#         else:
#             return 'Error: No file uploaded', 400
#     except Exception as e:
#         return f"Error: {e}", 500

# @app.route('/upload_video', methods=['POST'])
# def upload_video():
#     try:
#         media_folder = "D:/new/sample_data"
#         if not os.path.exists(media_folder):
#             os.makedirs(media_folder)
#         file = request.files['videoFile']
#         filename = secure_filename(file.filename)
#         extension = pathlib.Path(filename).suffix
#         filename = 'uploaded' + extension
#         destination = "/".join([media_folder, filename])
#         # video_duration = mp.VideoFileClip(destination).duration
# #         # if video_duration > 360:
# #         #     print("WARNING: Video duration exceeds 60 seconds. Please upload a shorter video.")
# #         #     raise SystemExit(0)

# #         # video_resolution = get_video_resolution(destination)
# #         # print(f"Video resolution: {video_resolution}")
# #         # if video_resolution[0] >= 1920 or video_resolution[1] >= 1080:
# #         #     print("Resizing video to 720p...")
# #         #     os.system(f"ffmpeg -i {destination} -vf scale=1280:360 D:/new/sample_data/input_vid.mp4")
# #         #     destination = "D:/new/sample_data/input_vid.mp4"
# #         #     print("Video resized to 720p")
# #         # else:
# #         #     print("No resizing needed")
# #         # start = 35
# #         # end = 62
# #         # interval = end - start
# #         # ffmpeg_path= 'D:/new/Wav2Lip/ffmpeg.exe'
# #         # subprocess.run([ffmpeg_path, '-y', '-i', destination, '-ss', str(start), '-t', str(interval), '-async', '1', 'input_vid.mp4'])

#         file.save(destination)
#         return 'Video uploaded successfully'

#     except Exception as e:
#         return f"Error: {e}", 500

# @app.route('/generate', methods=['POST'])
# def generate_result():
#     try:
#         selected_language = session.get('selected_language')
#         if not selected_language:
#             return "Error: Language not selected", 400
#         conversion = audio_video_handler.convert_video(language=selected_language)
#         if conversion:
#             return "Success: Video generated"
#         else:
#             return "Error: Video generation failed", 500
#     except Exception as e:
#         return f"Error: {e}", 500

# @app.route('/download_generated_video', methods=['GET'])
# def get_generated_video():
#     try:
#         output_video_path = "D:/new/converted_videos/output.mp4"  # Path to the generated video
#         if os.path.isfile(output_video_path):
#             return send_file(output_video_path, as_attachment=True)
#         else:
#             return "Error: Generated video file not found", 404
#     except Exception as e:
#         return f"Error: {e}", 500

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)
