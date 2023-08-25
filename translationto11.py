import requests
import io
from pydub import AudioSegment
import textwrap

def send_chunk_to_elevenlabs(chunk, voice_id):
    print(f"Sending chunk to ElevenLabs. Length: {len(chunk)} characters.")
    url = 'https://api.elevenlabs.io/v1/text-to-speech/' + voice_id + '?optimize_streaming_latency=0'
    headers = {
        'accept': 'audio/mpeg',
        'xi-api-key': 'f32cdf9a020fa4876db905c2641836bd',
        'Content-Type': 'application/json',
    }
    data = {"text": chunk}
    response = requests.post(url, json=data, headers=headers)
    return AudioSegment.from_file(io.BytesIO(response.content), format='mp3')

def main():
    voice_id = 'HwzveJsFPKdjsh80dfSG'
    input_file_name = "translations.txt"

    part_number = None
    text_buffer = ''

    with open(input_file_name, 'r') as input_file:
        for line in input_file:
            if line.startswith("Part"):
                if part_number is not None:
                    print(f"Processing Part {part_number}.")
                    chunks = textwrap.wrap(text_buffer, 1000, break_long_words=False)

                    current_audio = AudioSegment.empty()
                    for chunk in chunks:
                        print(f"Processing chunk for Part {part_number}.")
                        audio_chunk = send_chunk_to_elevenlabs(chunk, voice_id)
                        current_audio += audio_chunk

                    output_filename = f"part{part_number}.mp3"
                    print(f"Saving {output_filename}.")
                    current_audio.export(output_filename, format="mp3")
                    text_buffer = ''

                part_info = line.split(":")[0]
                part_number = int(part_info.split()[1].strip(','))
                print(f"Starting Part {part_number}.")

            else:
                text_buffer += ' ' + line.strip()

        if text_buffer.strip():
            print(f"Processing final Part {part_number}.")
            chunks = textwrap.wrap(text_buffer, 1000, break_long_words=False)

            current_audio = AudioSegment.empty()
            for chunk in chunks:
                print(f"Processing chunk for Part {part_number}.")
                audio_chunk = send_chunk_to_elevenlabs(chunk, voice_id)
                current_audio += audio_chunk

            output_filename = f"part{part_number}.mp3"
            print(f"Saving {output_filename}.")
            current_audio.export(output_filename, format="mp3")

    print("All audio files saved.")

if __name__ == "__main__":
    main()