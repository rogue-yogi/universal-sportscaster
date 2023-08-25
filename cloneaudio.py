import os
import subprocess

def clone_voice_from_folder(folder_path):
    files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.mp3')]

    files_command_part = " ".join([f"-F files=@{file};type=audio/mpeg" for file in files])

    curl_command = [
        "curl",
        "-X", 'POST',
        'https://api.elevenlabs.io/v1/voices/add',
        "-H", 'accept: application/json',
        "-H", 'Content-Type: multipart/form-data',
        "-H", 'xi-api-key: f32cdf9a020fa4876db905c2641836bd',
        "-F", f'name=Stephen Curry',
    ] + files_command_part.split() + [
        "-F", 'description=',
        "-F", 'labels=',
    ]

    result = subprocess.run(curl_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    response = result.stdout.decode().strip()
    voice_id = subprocess.run(["jq", "-r", ".voice_id"], input=response.encode(), stdout=subprocess.PIPE).stdout.decode().strip()

    print(voice_id)
    return voice_id

if __name__ == "__main__":
    folder_path = "/Users/livestream/Desktop/synclabs/Audio"
    voice_id = clone_voice_from_folder(folder_path)

    print("Voice cloning completed. Voice ID:", voice_id)
