from moviepy.editor import VideoFileClip

clip = VideoFileClip('')  # path to video file
clip.write_gif('', fps=10)  # path to gif file
