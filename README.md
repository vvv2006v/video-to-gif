# video-to-gif
*Program for converting video to GIF*

# Install the lib:
`pip install moviepy`

# Usage:
1. Specify the path to the video file.
```
clip = VideoFileClip('<your path>')
```
2. Specify the path to the GIF file.
```
clip.write_gif('<your path>', fps=10)
```
