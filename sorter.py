# Simple File Sorter in Python - Version 1.0
# Learning Goals: Lists, Loops, Conditionals, String Methods

# Example list of files to sort
files = ["image1.jpg", "text1.txt", "song1.mp3", "video1.mp4", "unknown.xyz"]

# File type categories as an example
images = [".jpg", ".png"]
documents = [".txt", ".pdf"]
music = [".mp3", ".wav"]
videos = [".mp4", ".mov"]

# Sort and categorize files
for file in files:
    # Check file extension and categorize
    if file.endswith(tuple(images)):
        print(file, "belongs to: IMAGES")
    elif file.endswith(tuple(documents)):
        print(file, "belongs to: DOCUMENTS")
    elif file.endswith(tuple(music)):
        print(file, "belongs to: MUSIC")
    elif file.endswith(tuple(videos)):
        print(file, "belongs to: VIDEOS")
    else:
        print(file, "belongs to: UNKNOWN")