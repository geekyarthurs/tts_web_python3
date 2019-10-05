from flask import Flask, request, send_file, send_from_directory, safe_join, abort, render_template
from voice_recog import TTS

app = Flask(__name__)
app.config["audio_files"] = "./audios/"


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_audio/<string:msg>/', methods=['GET', 'POST'])
def get_audio(msg):
    
    
    audioPath = TTS(msg).sendAudio()
    return send_file(audioPath)
    


if __name__ == "__main__":
    app.run(debug=True)