# Video Frame Extractor

## Overview
This script extracts frames from a selected video file and saves a random 50% of those frames with unique filenames. The extracted frames are saved in organized folders for further processing.

## Features
- Extracts frames from a video file at a specified FPS (default: 15 FPS).
- Saves frames in an organized folder structure.
- Selects and moves 50% of the extracted frames to a separate folder with unique filenames.
- Uses a GUI file picker to select the video file.

## Dependencies
Ensure you have the following dependencies installed before running the script:

- Python 3.x
- OpenCV (`cv2`)
- Tkinter (built-in with Python)
- shutil
- os
- datetime
- random

You can install OpenCV using:
```bash
pip install opencv-python
```

## Installation & Usage
1. Clone this repository or download the script.
2. Open a terminal or command prompt.
3. Run the script using:
```bash
python script.py
```
4. A file selection window will appear; choose a video file.
5. The script will extract frames and save them in the `extracted_frames/all_frames` folder.
6. 50% of the frames will be randomly selected and moved to `extracted_frames/random_50_frames`.

## Output Structure
After execution, the script generates the following folder structure:
```
extracted_frames/
  ├── all_frames/         # All extracted frames
  ├── random_50_frames/   # Randomly selected 50% frames with unique names
```

## Customization
- Modify the `fps` value in `extract_frames(video_path, output_folder, fps=15)` to adjust frame extraction rate.
- Change the percentage in `save_random_frames(frame_paths, output_folder, percentage=50)` to modify the selection ratio.

## License
This project is open-source and available for modification and distribution.

