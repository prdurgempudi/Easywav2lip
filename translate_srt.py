import pysrt
from translate import Translator

def translate_srt(input_file, output_file, from_lang, to_lang):
    print('translating srt')
    # Load the .srt file
    # lang_code = "hi_IN"
    # from_lang = from_lang.split("-")[0]  # Split at the underscore and get the first element
    # to_lang = to_lang.split("-")[0]  # Split at the underscore and get the first element
    print(f"from={from_lang}, to={to_lang}")
    input_file="video_subtitles.srt"
    subs = pysrt.open(input_file)
    # print("processing")
    # Set up the translator
    translator = Translator(from_lang=from_lang, to_lang=to_lang)

    # Translate each subtitle text
    for sub in subs:
        translated_text = translator.translate(sub.text)
        sub.text = translated_text

    # Save the translated subtitles to a new .srt file
        print("processing")
        subs.save(output_file, encoding='utf-8')
    return True #subs.save(output_file, encoding='utf-8')

# # Example usage
# if __name__ == "__main__":
#     input_srt = r"path\to\input.srt"
#     output_srt = r"path\to\output.srt"
#     from_language = 'te'  # Telugu
#     to_language = 'en'    # English
