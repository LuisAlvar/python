# pip install ez_setup
# pip install moviepy
from moviepy.editor import VideoFileClip
import imageio
import numpy as np

# Load the video
video = VideoFileClip("C:\Workstation\python\projects\input\combining_probabilites_brilliant_animation.mp4")

# Extract frames and save as GIF
frames = []
for t in np.arange(0, video.duration, 1/30):  # Adjust frame rate
    frames.append(video.get_frame(t))

# Repeat frames for looping effect 
looped_frames = frames * 3; # Adjust the mulitple for the number fo loops

imageio.mimsave('./output/output.gif', looped_frames, fps=30)

# pip uninstall moviepy
# pip uninstall ez_setup
