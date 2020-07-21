import requests
import os 




lbrynet = f'lbrynet.exe start'
os.system(lbrynet)


def downl():

    video_url = input('Copy video URL: ')
    audio_answer = input('(Enter = No) Extract audio only?')
    download_path = input('Choose a folder to download the file: ')
    
    audio_only_str = ''
    
    if audio_answer == '':
        audio_only = False
    else:
        audio_only = True
        audio_only_str = '--extract-audio --audio-format mp3'
        
    
    stringa = f'youtube-dl -22 {video_url} -o {os.path.join(download_path,r"%(title)s.%(ext)s")} --write-info-json {audio_only_str}'
    os.system(stringa)
    lista_pasta= os.listdir(download_path)
    for index, i in enumerate(lista_pasta, 1):
        print(index,"-",i)
    posicao = int(input('Choose the file (int - use the index): '))   
    file_path = os.path.join(download_path,lista_pasta[posicao-1]) 
    print("File chosen: " + lista_pasta[posicao-1])
    name = input("Insert Lbry url: ")
    title= input('File Title: ') 
    thumbnail_url = str(input("Insert thumbnail URL: ")) 
    bid = str(input("Insert BID: "))
    str_list_tag = input('Insert TAGS (Use comma to separate tags): ')
    tags = str_list_tag.split(',')                                       
    channel_account_id = input('Insert you channel_account_id: ')                 
    channel_id = input("Insert your channel_id: ")
    
    
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


downl()
