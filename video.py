
import os
import random
import cv2
from tkinter import Tk, filedialog
from datetime import datetime
import shutil

def extract_frames(video_path, output_folder, fps=15):
    """Extract frames from a video at the specified FPS."""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Could not open video file {video_path}.")
        return []

    video_fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_interval = max(1, int(video_fps / fps))

    frame_count = 0
    extracted_frames = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % frame_interval == 0:
            frame_name = os.path.join(output_folder, f"frame_{frame_count:06d}.jpg")
            cv2.imwrite(frame_name, frame)
            extracted_frames.append(frame_name)

        frame_count += 1

    cap.release()
    print(f"Extracted {len(extracted_frames)} frames from {video_path}.")
    return extracted_frames

def save_random_frames(frame_paths, output_folder, percentage=50):
    """Save a random percentage of frames to a separate folder with unique filenames."""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    num_frames_to_save = int(len(frame_paths) * (percentage / 100))
    selected_frames = random.sample(frame_paths, num_frames_to_save)

    for frame_path in selected_frames:
        # Generate a unique filename using the current timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        frame_name = os.path.basename(frame_path)
        name, ext = os.path.splitext(frame_name)
        new_frame_name = f"{name}_{timestamp}{ext}"
        output_path = os.path.join(output_folder, new_frame_name)

        # Move the file to the output folder with the new unique name
        shutil.move(frame_path, output_path)
        print(f"Moved {frame_name} to {output_path}")

def main():
    print("Select a video file to process:")
    Tk().withdraw()  # Hide the root window
    video_path = filedialog.askopenfilename(
        title="Select Video File",
        filetypes=[("Video Files", "*.mp4;*.avi;*.mov;*.mkv")]
    )

    if not video_path:
        print("No file selected. Exiting.")
        return

    base_output_folder = "extracted_frames"

    # Step 1: Extract frames
    frames_folder = os.path.join(base_output_folder, "all_frames")
    print("Extracting frames...")
    frame_paths = extract_frames(video_path, frames_folder)

    if not frame_paths:
        print("No frames extracted. Exiting.")
        return

    # Step 2: Save random 50% of the frames
    random_frames_folder = os.path.join(base_output_folder, "random_50_frames")
    print("Saving random 50% of frames...")
    save_random_frames(frame_paths, random_frames_folder)

    print(f"Random frames saved in: {random_frames_folder}")

if __name__ == "__main__":
    main()