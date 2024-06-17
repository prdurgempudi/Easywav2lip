# main cell to convert speech to srt Azure

def speech_to_srt(audio,srt_path,language_code):
  !python captioning.py --key f1f6c22860e349b0a618dd60eee1f1a8 --region centralus --language language_code --input audio --format any --offline --output srt_path --srt