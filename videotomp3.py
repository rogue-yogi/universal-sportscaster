import os
from pydub import AudioSegment
import tempfile

def split_audio(input_path, output_path):
    audio = AudioSegment.from_file(input_path)
    total_length = len(audio)
    max_file_size = 10 * 1024 * 1024  # 10 MB
    max_segments = 25

    segments = []
    start = 0
    duration = total_length // max_segments
    for i in range(max_segments):
        segments.append(audio[start:start+duration])
        start += duration

    final_segments = []
    for segment in segments:
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        segment.export(temp_file.name, format="mp3")
        size = os.path.getsize(temp_file.name)

        if size > max_file_size:
            parts = segment[::len(segment) // (size // max_file_size + 1)]
            final_segments.extend(parts)
        else:
            final_segments.append(segment)

        os.unlink(temp_file.name)

    for count, segment in enumerate(final_segments, 1):
        file_name = f"{output_path}/segment_{count}.mp3"
        segment.export(file_name, format="mp3")

input_path = '/Users/livestream/Desktop/synclabs/video.mp4'
output_path = '/Users/livestream/Desktop/synclabs/Audio'
split_audio(input_path, output_path)
