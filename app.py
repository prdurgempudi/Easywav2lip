from flask import Flask, render_template, request, send_file
import inference
import os

os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    video_file = request.files['video']
    audio_file = request.files['audio']

    # Save uploaded files
    video_path = 'D:/ALL_DD_APIs/Easy-Wav2Lip/' + video_file.filename
    audio_path = 'D:/ALL_DD_APIs/Easy-Wav2Lip/' + audio_file.filename
    video_file.save(video_path)
    audio_file.save(audio_path)
    checkpoint_path='D:/ALL_DD_APIs/Easy-Wav2Lip/checkpoints/wav2lip_gan.pth'
    # Generate output
    output_path = 'D:/ALL_DD_APIs/Easy-Wav2Lip/output_video.mp4'
    wav2lip_model = inference()
    print("conversion .. completed .. ")
    if wav2lip_model:
        return send_file(output_path, as_attachment=True)
    else:
        return "error"

@app.route('/download_generated_video', methods=['GET'])
def get_generated_video():
    output_video_path ="D:/ALL_DD_APIs/Wav2Lip_API/sample_data/output.mp4" # Replace this with the actual path of the generated video
    try:
        return send_file(output_video_path, as_attachment=True)
    except:
        return "Generated video file not found!", 404
        

if __name__ == '__main__':
    app.run(debug=True)
