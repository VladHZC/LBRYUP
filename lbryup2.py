from tkinter import *
import os 
requests = "pip install requests"
os.system(requests)

import requests
from platform import system
root = Tk()
platformD = system()

if platformD == 'Windows':
    root.iconbitmap(default='images/2.ico')
    image = PhotoImage(file='images/1.png') 
    
else: 
    root.iconbitmap(os.path.dirname(os.path.abspath(__file__))+'/images/2.ico')
    image = PhotoImage(os.path.dirname(os.path.abspath(__file__))+'/images/1.png')

label = Label(root, image = image)
label.pack(side= TOP)
root.title("LBRYUP 0.2")


# width and height variables
can_width = 300
can_height = 500
root.geometry(f"{can_width}x{can_height}")
root.title("Event handling")
# video weblink 
video_entry = Entry(root, width =40)
video_entry.insert(0, "Insert video Link")
video_entry.pack()
video_url= ""
# lbryname
name_entry = Entry(root,width =40)
name_entry.insert(0, "Insert Lbry Name")
name_entry.pack()
name = ""
# post title
title_entry = Entry(root,width= 40)
title_entry.insert(0, "Insert Post Title")
title_entry.pack()
title =""
# thumbnail entry 
thumb_entry = Entry(root , width =40)
thumb_entry.insert(0, "Insert Thumbnail URL")
thumb_entry.pack()
# Bid Entry
bid_entry = Entry(root , width=40 )
bid_entry.insert(0, "Enter Bid Value")
bid_entry.pack()
bid=""
# Tag selection
tags_entry = Entry(root , width =40)
tags_entry.insert(0 ,'Insert TAGS (Use comma to separate tags)')
tags_entry.pack()
tags=[]
# ChannelId Entry
channel_entry = Entry(root , width = 40)
channel_entry.insert(0, 'Insert Channel Claim ID')
channel_entry.pack()
channel_id=r""

def Click():
    global video_url
    video_url = str(video_entry.get())
    global name 
    name =  str(name_entry.get())
    Label(root, text = "lbry://@yourchannel/" + name).pack()
    global title
    title = str(title_entry.get())
    global thumbnail_url
    thumbnail_url = str(thumb_entry.get())
    global bid
    bid = str(bid_entry.get())
    global tags
    global tags_entry    
    tags_str = str(tags_entry.get())
    tags= tags_str.split(',')
    global channel_id
    channel_id = str(channel_entry.get())
    
download_path = os.getcwd()
file_path = ""
audio_answer=""
audio_= IntVar()
def audio():
    if audio_.get() == 1:
        global audio_answer
        audio_answer = "--extract-audio --audio-format mp3"
        global download_path
        global file_path
        file_path = os.path.join(download_path, "video.mp3")
        print(file_path)
    else:
        audio_answer = ""
        file_path = os.path.join(download_path, "video.mp4")
        print(file_path)
audio()
audiobtn =Checkbutton(root, text="audio only", variable =audio_, command = audio)
audiobtn.pack()
win = Button(root, text="OK", command = Click)
win.pack()        
def download(): 

    stringa = f'youtube-dl -22 {video_url} -o "video.%(ext)s" {audio_answer}'
    os.system(stringa) 
    return_stream_create = requests.post("http://localhost:5279",
                    json={"method": "stream_create",
                        "params": {"name": name,
                                    "title": title,
                                    "bid": bid,
                                    "file_path": file_path,
                                    "validate_file": False, 
                                    "optimize_file": True, 
                                    "tags": tags,
                                    "languages": [], 
                                    "locations": [],
                                    "channel_id": channel_id,
                                    "channel_account_id": "",
                                    "funding_account_ids": [],
                                    "preview": False,
                                    "thumbnail_url": thumbnail_url,
                                    "blocking": False}}).json()
    print(return_stream_create)    

download_btn = Button(root , text="Upload" ,command = download)
download_btn.pack()

root.mainloop()