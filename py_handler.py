import os
import inference
import wav2lip_inference
import sys
import traceback
import create_a_dub_from_file
from werkzeug.utils import secure_filename
import pathlib

DEFAULT_VIDEO_FILE ="uploaded.mp4"

def convert_video(from_lang,to_lang,video_file):
    try:
        print("started converting")
        # filename = secure_filename(video_file.filename)
        file_format ='video/mp4' #pathlib.Path(video_file).suffix
        
        print(file_format)
        translated_output= create_a_dub_from_file.create_dub_from_file(video_file,file_format,from_lang,to_lang)
        print("synchronising lip movement")
        try:
            translated_output_path=f'{translated_output}' #'data/3ZaVFyDo9vTN1QkX2sV2/hi.mp4'
            conversion_completed=wav2lip_inference.run_model(video_file,translated_output_path,quality='Enhanced')
            if conversion_completed:
                return True
        except Exception as e:
            print("error")
            print(e)
            print("deleting_files")
        else:
            return "Error in wav2lip model"
    except Exception as e:
        print("Exception has occured ...  convert_video() ")
        print(e)
        traceback_obj = sys.exc_info()[2]
        # Extract line information from the traceback
        line_info = traceback.extract_tb(traceback_obj)[-1]
        # Access the filename and line number
        filename, line_number, function_name, source_code = line_info
        print(f"Error on line {line_number} in {filename}: {source_code.strip()}")
        return False


from_lang="en"
language="hi"
video_file=r"Individual_health1.mp4" #/content/drive/MyDrive/integreation/singer.mp4"
final_output_directory="wav2lip_imaginary_speech.mp4"
convert_video(from_lang,language,video_file=video_file)

