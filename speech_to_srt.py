import subprocess
import platform

def convert_to_wav(input_file, output_wav_file):
    """
    Converts an audio file to WAV format using ffmpeg.

    Parameters:
    - input_file (str): Path to the input audio file.
    - output_wav_file (str): Path to the output WAV file.

    Returns:
    - output (str): The standard output from the command.
    - error (str): The standard error from the command.
    - returncode (int): The return code from the command.
    """
    command = ['ffmpeg', '-i', input_file, output_wav_file]
    subprocess.call(command, shell=platform.system() != 'Windows')
   #result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    return True

def generate_captions(input_file, output_file, language_code):
    """
    Generates captions for a given audio file using Azure's speech-to-text service.

    Parameters:
    - input_file (str): Path to the input audio file.
    - output_file (str): Path to the output SRT file.
    - language_code (str): The language code for the speech-to-text service.

    Returns:
    - output (str): The standard output from the command.
    - error (str): The standard error from the command.
    - returncode (int): The return code from the command.
    """
    # Convert the input file to WAV format
    wav_file = 'temp.wav'
    output_file_file='video_subtitles.srt'
    convert_to_wav(input_file, wav_file)

    # if convert_returncode != 0:
    #     return convert_output, convert_error, convert_returncode

    # Fixed parameters
    api_key = 'f1f6c22860e349b0a618dd60eee1f1a8'
    region = 'centralus'
    format = 'any'
    offline = True
    srt = True

    command = [
        'python', 'captioning.py',
        '--key', api_key,
        '--region', region,
        '--language', language_code,
        '--input', wav_file,
        '--format', format,
        '--output', output_file
    ]

    if offline:
        command.append('--offline')

    if srt:
        command.append('--srt')

    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    return result.stdout


# input_file = r'/content/drive/MyDrive/integreation/singer.mp4'
# output_file = r"/content/drive/MyDrive/integreation/singer_test_1.srt"
# language_code= 'hi-IN'


# generate_captions(input_file, output_file, language_code)
