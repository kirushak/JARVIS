import os
query = input("enter query: ")
if "music folder" in query:
    os.startfile("music directory")
elif "document folder" in query:
    os.startfile("document directory")
elif "downloads folder" in query:
    os.startfile("downloads directory")
elif "videos folder" in query:
    os.startfile("videos directory")