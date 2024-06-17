import os
import noise_removal
import speech_to_srt
import translate_srt
import generate_audio_from_subtitle
import inference
import sys
import traceback

CHECKPOINT_PATH = "Wav2Lip/checkpoints/wav2lip_gan.pth" 
DEFAULT_VIDEO_FILE ="uploaded.mp4"
NOISE_REMOVE_VIDEO="noise_remove.mp4"
SRT_FILE= "video_subtitles.srt"
TRANSLATED_SRT="translated.srt"
OUTPUT_TRANSLATED_AUDIO_LOCATION = "translated.wav"
FINAL_OUTPUT_DIRECTOR = "wav2lip_output.mp4"
DEFAULT_VIDEO_FILE_NAME ="video"
DEFAULT_LANGAUGE = "English"
DEFAULT_IMAGE_FILE= "D:/new/sample_data/uploaded.jpg"

# Interaction method with the actual Wav2Lip model
# def get_conversions(audio_file, video_file, file_name, final_output_directory):
#     try:
#             checkpoint_path = CHECKPOINT_PATH
#             inference.get_conversion(audio_file, video_file,  file_name,  checkpoint_path, final_output_directory)

#     except Exception as e:
#         print("Exception has occured.. get_conversion")
#         print(e)
#         return False
#     return True

# for finding langauge code
def find_language_code(language):
    langcode_audio = {
                      'English_female': 'en-EN',
                      'English_male': 'en-EN',
                      'Hindi_female': 'hi-IN',
                      'Hindi_male' : 'hi-IN',
                      'Bengali_male': 'bn-IN',
                      'Bengali_female':'bn-IN',
                      'Gujarati_female': 'gu-IN',
                      'Gujarati_male': 'gu-IN',
                      'Kannada_female': 'kn-IN',
                      'Kannada_male': 'kn-IN',
                      'Malayalam_female':'ml-IN',
                      'Malayalam_male':'ml-IN',
                      'Marathi_female':'mr-IN',
                      'Marathi_male': 'mr-IN',
                      'Punjabi_female': 'pa-IN',	
                      'Punjabi_male': 'pa-IN',
                      'Tamil_female': 'ta-IN',	
                      'Tamil_male': 'ta-IN',
                      'Telugu_female': 'te-IN',	
                      'Telugu_male': 'te-IN',	
                      'Mandarin': 'cmn-CN',
                      'Mandarin_female': 'cmn-CN',
                      'Spanish': 'es-ES',
                      'Spanish_female': 'es-ES',
                      'French': 'fr-FR',
                      'French_female': 'fr-FR',
                      'German':'de-DE',
                      'German_female':'de-DE'
                      }

    voice_name = {

        'English_female': 'en-IN-Standard-A',
        'English_male': 'en-IN-Standard-B',
        'Hindi_male': 'hi-IN-Standard-B',
        'Hindi_female': 'hi-IN-Standard-A',
        'Bengali_male': 'bn-IN-Standard-D',
        'Bengali_female': 'bn-IN-Wavenet-A',
        'Gujarati_female': 'gu-IN-Standard-A',
        'Gujarati_male': 'gu-IN-Standard-B',
        'Kannada_female': 'kn-IN-Standard-A',
        'Kannada_male': 'kn-IN-Standard-B',
        'Malayalam_female':'ml-IN-Standard-A',
        'Malayalam_male':'ml-IN-Standard-B',
        'Marathi_female':'mr-IN-Standard-A',
        'Marathi_male': 'mr-IN-Standard-B',
        'Punjabi_female': 'pa-IN-Standard-A',
        'Punjabi_male': 'pa-IN-Standard-B',
        'Tamil_female': 'ta-IN-Standard-A',
        'Tamil_male': 'ta-IN-Standard-B',
        'Telugu_female': 'te-IN-Standard-A',
        'Telugu_male': 'te-IN-Standard-B',
        'Mandarin': 'cmn-CN-Standard-B',
        'Mandarin_female': 'cmn-CN-Standard-A',
        'Spanish': 'es-ES-Standard-B',
        'Spanish_female': 'es-ES-Standard-A',
        'French': 'fr-FR-Standard-B',
        'French_female': 'fr-FR-Standard-A',
        'German': 'de-DE-Standard-B',
        'German_female': 'de-DE-Standard-A'

    }
    return langcode_audio[language], voice_name[language]


def convert_video(from_lang,language,video_file, noiseremoval=NOISE_REMOVE_VIDEO,srt_file=SRT_FILE,translated_srt=TRANSLATED_SRT, output_translated_audio_location=OUTPUT_TRANSLATED_AUDIO_LOCATION, video_file_name=DEFAULT_VIDEO_FILE_NAME , final_output_directory=FINAL_OUTPUT_DIRECTOR):
    try:
        print("started converting")
        print(f"to_lang={language}")
        rate=1.0
        print(rate)
        try:
          # print("ssss")
          from_language_code, name = find_language_code(from_lang)
          language_code, name = find_language_code(language)
          print(f'from_lang={from_lang}')
        except:
          return "Language code error"
        # conversion_completed=inference.convert()
        video = noise_removal.noiseremoval(video_file,noiseremoval)
        if video==True:
            print("generating srt")
            # audio_file_id = "/" + video_file_name +".wav"
            # output_audio_file_location = output_audio_file_location + audio_file_id
            # print(output_audio_file_location)
            # audio_extraction.extract_audio(video_path, output_audio_file_location)
            srt_file1 = speech_to_srt.generate_captions(noiseremoval,srt_file,from_language_code)
            print("translating srt")
            translated_srt1 = translate_srt.translate_srt(srt_file,translated_srt,from_language_code,language_code)
            if translated_srt1==True:
                print("generating audio")
                srt_audio_gen= generate_audio_from_subtitle.generate_audio(translated_srt,output_translated_audio_location,language_code,rate, name )
                if srt_audio_gen == True:
                    print("synchronising lip movement")
                    
                    conversion_completed=inference.convert()
                    if conversion_completed:
                        return True
                    else:
                        return "Error in wav2lip model"
                else:
                    return "error in audio generation"
            else:
                return "error in translating srt"
        else:
            return "error in srt_file generation"
        # print("audio extracted")
        # # output_audio_file_location = output_audio_file_location + audio_file_id
        # transation_completed =audio_translation.translate_voice(language,output_audio_file_location,
        #                                                                       output_translated_audio_location
        #                                                                       )
        
        # transation_completed=True
        # print("translation completed")
        # output_translated_audio_location=output_audio_file_location #"D:/new/translated_audio/translated.wav"
        # transation_completed=True
        # if transation_completed:
            
        #     try:
        #         conversion_completed=inferenc.convert(output_translated_audio_location, video_file, CHECKPOINT_PATH, final_output_directory)
        #         # conversion_completed=inference.convert()
        #         if conversion_completed:
        #             return True
        #     except Exception as e:
        #         print(e)
        # else:
        #     return False   


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


from_lang="English_male"
language="Telugu_male"
video_file="input.mp4" #/content/drive/MyDrive/integreation/singer.mp4"
noiseremoval=NOISE_REMOVE_VIDEO,
srt_file=SRT_FILE,
translated_srt=TRANSLATED_SRT, 
output_translated_audio_location=OUTPUT_TRANSLATED_AUDIO_LOCATION,
video_file_name=DEFAULT_VIDEO_FILE_NAME , 
final_output_directory=FINAL_OUTPUT_DIRECTOR
convert_video(from_lang,language,video_file=video_file, noiseremoval=NOISE_REMOVE_VIDEO,srt_file=SRT_FILE,translated_srt=TRANSLATED_SRT, output_translated_audio_location=OUTPUT_TRANSLATED_AUDIO_LOCATION, video_file_name=DEFAULT_VIDEO_FILE_NAME , final_output_directory=FINAL_OUTPUT_DIRECTOR)

# def convert_image(video_file=DEFAULT_IMAGE_FILE, output_audio_file_location=OUTPUT_AUDIO_FILE_LOCATION, output_translated_audio_location=OUTPUT_TRANSLATED_AUDIO_LOCATION, video_file_name=DEFAULT_VIDEO_FILE_NAME , language=DEFAULT_LANGAUGE, final_output_directory=FINAL_OUTPUT_DIRECTOR, text_input='Hello'):
#     try:
#         print("Using convert image...")
#         print(text_input)
#         language_code, voice_name = find_language_code(language)
#         print("fetched langauge code ...")
#         video_file_name = video_file_name + "_" +language
#         audio_file_id = "/" + video_file_name +".wav"
#         output_audio_file_location = output_audio_file_location + audio_file_id
# #         extract_audio_from_video.extract_audio(video_file, output_audio_location=output_audio_file_location)
#         transation_completed = automated_transcription_script.translate_text_only(text_input,
#                                                                               output_translated_audio_location,
#                                                                               language_code=language_code,
#                                                                               voice_name = voice_name
#                                                                               )
#         if transation_completed:
#             get_conversions(output_translated_audio_location, video_file, video_file_name, final_output_directory)
#         return True
#     except Exception as e:
#         print("Exception has occured ...  convert_image() ")
#         print(e)
#         return False

