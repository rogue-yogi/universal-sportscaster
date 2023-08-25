from moviepy.editor import VideoFileClip
import os

def split_video(video_path, max_size_MB=100):
    clip = VideoFileClip(video_path)
    total_duration = clip.duration
    total_size_MB = os.path.getsize(video_path) / (1024 * 1024)
    
    # Calculate the approximate duration for each chunk
    chunk_duration = (max_size_MB / total_size_MB) * total_duration

    output_folder = "/Users/livestream/Desktop/synclabs/Chunks"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    part_number = 1
    for start_time in range(0, int(total_duration), int(chunk_duration)):
        end_time = min(start_time + chunk_duration, total_duration)
        final_output_path = os.path.join(output_folder, f"part{part_number}.mp4")
        clip.subclip(start_time, end_time).write_videofile(final_output_path, codec="libx264", audio_codec="aac")
        print(f"Saved {final_output_path}")
        part_number += 1

    print("Video splitting completed.")

if __name__ == "__main__":
    video_path = '/Users/livestream/Desktop/synclabs/video.mp4'
    split_video(video_path)
