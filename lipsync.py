import requests
from concurrent.futures import ThreadPoolExecutor
def process_video(audio_uri, video_uri, id):
    try:
        # [1] Synchronize (Lipsync)
        synchronize_url = "https://rogue-yogi--synchronize-v0-1-1-synchronize.modal.run/"
        payload_synchronize = {
            "audio_uri": audio_uri,
            "video_uri": video_uri,
            "wav2lip_batch_size": 128
        }

        response_synchronize = requests.post(synchronize_url, json=payload_synchronize)
        if response_synchronize.status_code == 200:
            result_path = response_synchronize.text[1:-1]  # Remove the quotes around the filepath
            print("Result Path:", result_path)  # Print the result path

            # [2] Synergize (Artifact Cleanup / Post Processing)
            synergize_url = "https://rogue-yogi--synergize-v0-1-1-synergize.modal.run/"
            output_path = f"/tmp/59676e5a-f9b1-451a-aaae-21da1540582e{id}_result.mp4"
            payload_synergize = {
                "input_path": result_path,
                "output_path": output_path
            }

            response_synergize = requests.post(synergize_url, json=payload_synergize)
            if response_synergize.status_code == 200:
                final_url = response_synergize.text  # Assigning the response text directly
                print("Final URL:", final_url)
            else:
                print("Synergize response content:", response_synergize.text)  # Debugging line

        else:
            print(f"Synchronize request failed with status code: {response_synchronize.status_code}")
            print("Response content:", response_synchronize.text)
    except Exception as e:
        print(f"An error occurred while processing audio {audio_uri} and video {video_uri}: {str(e)}")

# List of audio and video URIs
audio_video_pairs = [
    ("http://dl.dropboxusercontent.com/s/scl/fi/mb7ue99gbdalrgjcl6j9k/part1.mp3?rlkey=g2fpl2g18513jn3si5x4v03x1&dl=0", "http://dl.dropboxusercontent.com/s/scl/fi/oe8lffnwpc7ic3hh2ka4u/part1.mp4?rlkey=6q5xzapd9uy73m7ou94xy6q0h&dl=0"),
    ("http://dl.dropboxusercontent.com/s/scl/fi/6iq1pvy88w6zqy7oyylkv/part2.mp3?rlkey=7trc5cg8fyivbb1qwgt8sfnw6&dl=0", "http://dl.dropboxusercontent.com/s/scl/fi/u9fx3r1qia25kxwzcvgpo/part2.mp4?rlkey=4ogmb0wfgbgytfkt56d6tucqr&dl=0"),
    ("http://dl.dropboxusercontent.com/s/scl/fi/2qljfzgrxp4mom6arjwna/part3.mp3?rlkey=swi6acpdremkgrtgno83h2d2x&dl=0", "http://dl.dropboxusercontent.com/s/scl/fi/1yl9fzz4xm310cbmu72qw/part3.mp4?rlkey=sqvnxcmn6zkbizw9hb22onw4y&dl=0"),
    ("http://dl.dropboxusercontent.com/s/scl/fi/omnq1x9lg02jyr7r0zwy1/part4.mp3?rlkey=d68607tugg2no975rs2wzgqgu&dl=0", "http://dl.dropboxusercontent.com/s/scl/fi/75oa26nf7428rwc31n3u7/part4.mp4?rlkey=aqr2xyeeu67cgqh53h568erjn&dl=0"),
    ("http://dl.dropboxusercontent.com/s/scl/fi/1amyokfsayw3uxqakqnz7/part5.mp3?rlkey=glyfqpjz625ju4mrq87psdipe&dl=0", "http://dl.dropboxusercontent.com/s/scl/fi/w1c4ipzpumdh0uzvld0fx/part5.mp4?rlkey=4ui6w7y1f3wmtfwej34fofgme&dl=0"),
    ("http://dl.dropboxusercontent.com/s/scl/fi/ybrrqtw9u43eva5of01xv/part6.mp3?rlkey=wyg429pi2ck4z6vk1j04446vf&dl=0", "http://dl.dropboxusercontent.com/s/scl/fi/210wlvjshx0qfqcido16z/part6.mp4?rlkey=v73bkb8111t1idbsvqc2v0wct&dl=0"),
    ("http://dl.dropboxusercontent.com/s/scl/fi/11c9uq84dgjrpffgl0kpe/part7.mp3?rlkey=h7mc7z9ps1ily76desxt627pq&dl=0", "http://dl.dropboxusercontent.com/s/scl/fi/d4ks66q1hl8ywotnzu914/part7.mp4?rlkey=s2fmas057p0svtd1ymejqklig&dl=0"),
    ("http://dl.dropboxusercontent.com/s/scl/fi/d0darlt5o7iq5g0e2rewz/part8.mp3?rlkey=gwohkthpg963jhn0k8fynoz2r&dl=0", "http://dl.dropboxusercontent.com/s/scl/fi/7642aelkpcn5h6yc25j5y/part8.mp4?rlkey=won94g6xi6g18gw1lozjro2f6&dl=0"),
    ("http://dl.dropboxusercontent.com/s/scl/fi/qf13vz9euptebnfuizhc6/part9.mp3?rlkey=i25aoary59duld1i8lcyuhwib&dl=0", "http://dl.dropboxusercontent.com/s/scl/fi/iompau2gca6qxqqu7adar/part9.mp4?rlkey=y2x9rxen7bojsue3yvky5aeau&dl=0"),
    ("http://dl.dropboxusercontent.com/s/scl/fi/z7fbo38z4i5vc638q1ylk/part10.mp3?rlkey=rvfstnizpvc6a89qddkrqro52&dl=0", "http://dl.dropboxusercontent.com/s/scl/fi/2ckqnspbv1mms490jlym1/part10.mp4?rlkey=umgywoptsp98o82401vy0cvu5&dl=0"),
    ("http://dl.dropboxusercontent.com/s/scl/fi/7kehkdueumcqw6r7kzzgj/part11.mp3?rlkey=lnczf3oj2vj4op97x8mtyh0kb&dl=0", "http://dl.dropboxusercontent.com/s/scl/fi/xc2k6wk2hog4k9uaoeeqi/part11.mp4?rlkey=e6ac0jzsxy30dpncvtj4n5oad&dl=0"),
    ("http://dl.dropboxusercontent.com/s/scl/fi/2u2ga7qyaqa92lrys6c1s/part12.mp3?rlkey=r7y2w4pfwpogbsq22sq1mbs7r&dl=0", "http://dl.dropboxusercontent.com/s/scl/fi/mr087mnwti3oz0evwz63u/part12.mp4?rlkey=ytlada1natn889uzgv18phm1m&dl=0"),
    ("http://dl.dropboxusercontent.com/s/scl/fi/fpe19rb1im8megy1esf94/part13.mp3?rlkey=cx66r0t5jcmqz0l5df14612ek&dl=0", "http://dl.dropboxusercontent.com/s/scl/fi/ou9ctj0xins8nlvq6yp3o/part13.mp4?rlkey=s7zup1tar1hm1ujm5yqpyfoai&dl=0")
]

with ThreadPoolExecutor() as executor:
    futures = [executor.submit(process_video, audio_uri, video_uri, id) for id, (audio_uri, video_uri) in enumerate(audio_video_pairs)]

    for future in futures:
        future.result()