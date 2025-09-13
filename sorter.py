# Simple File Sorter in Python - Version 1.0
# Learning Goals: Lists, Loops, Conditionals, String Methods

# Example list of files to sort
files = ["bild1.jpg", "text1.txt", "lied1.mp3", "film1.mp4", "unbekannt.xyz"]

# File type categories as an example
bilder = [".jpg", ".png"]
dokumente = [".txt", ".pdf"]
musik = [".mp3", ".wav"]
videos = [".mp4", ".mov"]

# Sort and categorize files
for file in files:
    # Check file extension and categorize
    if file.endswith(tuple(bilder)):
        print(file, "gehört zu: BILDER")
    elif file.endswith(tuple(dokumente)):
        print(file, "gehört zu: DOKUMENTE")
    elif file.endswith(tuple(musik)):
        print(file, "gehört zu: MUSIK")
    elif file.endswith(tuple(videos)):
        print(file, "gehört zu: VIDEOS")
    else:
        print(file, "gehört zu: UNBEKANNT")