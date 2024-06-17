import os
import tempfile
from pysubparser import parser
from pydub import AudioSegment
from google.cloud import texttospeech

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] =r"/content/drive/MyDrive/integreation/Easy-Wav2Lip/Srt_to_speech.json" # "Srt_to_speech.json"

def time_to_ms(time):
    return ((time.hour * 60 + time.minute) * 60 + time.second) * 1000 + time.microsecond / 1000

def generate_audio(input_path, output_path, language_code, rate, voice_name):
    
    print(f"Generating audio file for {input_path} with Google Cloud Text-to-Speech")

    subtitles = parser.parse(input_path)

    client = texttospeech.TextToSpeechClient()

    audio_sum = AudioSegment.empty()

    with tempfile.TemporaryDirectory() as tmpdirname:
        print('Created temporary directory', tmpdirname)

        temp_file_path = os.path.join(tmpdirname, "temp.wav")
        prev_subtitle = None
        prev_audio_duration_ms = 0

        for subtitle in subtitles:
            synthesis_input = texttospeech.SynthesisInput(text=subtitle.text)
            voice = texttospeech.VoiceSelectionParams(
                language_code=language_code,
                name=voice_name
            )
            audio_config = texttospeech.AudioConfig(
                audio_encoding=texttospeech.AudioEncoding.LINEAR16,
                speaking_rate=rate
            )

            response = client.synthesize_speech(
                input=synthesis_input, voice=voice, audio_config=audio_config
            )

            with open(temp_file_path, "wb") as out:
                out.write(response.audio_content)

            audio_segment = AudioSegment.from_wav(temp_file_path)

            print(subtitle.start, subtitle.text)

            if prev_subtitle is None:
                silence_duration_ms = time_to_ms(subtitle.start)
            else:
                silence_duration_ms = time_to_ms(subtitle.start) - time_to_ms(prev_subtitle.start) - prev_audio_duration_ms

            audio_sum = audio_sum + AudioSegment.silent(duration=silence_duration_ms) + audio_segment

            prev_subtitle = subtitle
            prev_audio_duration_ms = len(audio_segment)

        with open(output_path, 'wb') as out_f:
            audio_sum.export(out_f, format='wav')

        return True

# if __name__ == "__main__":
#     subtitle_file_path = r"/content/drive/MyDrive/integreation/singer_tel.srt"  # Replace with the path to your subtitle file
#     output_audio_path = r"/content/drive/MyDrive/integreation/singer_tel_1.wav"  # Replace with the desired output path
#     language_code = 'te-IN'  # Replace with your desired language code
#     speech_rate = 1.0  # Normal speed
#     voice_name ='te-IN-Standard-A'  # Voice selection

#     # Generate the audio
#     output_audio_path = generate_audio(subtitle_file_path, output_audio_path, language_code=language_code, rate=speech_rate, voice_name=voice_name)
#     print(f"Generated audio file saved at: {output_audio_path}")
