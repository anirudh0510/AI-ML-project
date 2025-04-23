from flask import Flask, request, jsonify, send_from_directory
import os
from main import run_analysis_and_show

app = Flask(__name__, static_folder="frontend")

@app.route('/')
def serve_index():
    return send_from_directory('frontend', 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('frontend', filename)

@app.route('/analyze', methods=['POST'])
def analyze():
    uploaded_file = request.files.get('video')
    if uploaded_file:
        input_path = os.path.join('input_videos', 'input_video.mp4')
        output_path = os.path.join('output_videos', 'output_video.mp4')
        uploaded_file.save(input_path)

        # Trigger the analysis and show video in OpenCV window
        run_analysis_and_show(input_path, output_path)

        return jsonify({'status': 'success'})
    return jsonify({'error': 'No video uploaded'}), 400

if __name__ == '__main__':
    app.run(debug=True)
