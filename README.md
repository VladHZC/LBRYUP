# LBRY UPLOADERS		
---

Lbry community has awesome projects and tools to improve the users experience we have very smart upload tool as :

[Turbosharekit](https://github.com/apenasrr/lbry_turbosharekit) by: @Rip8
[MassUploader](https://open.lbry.com/@MassUploader:f?r=587XHbBRBftaXBcauWBHBaTMspyu1ojN) by: @Blanxs

This tools are very helpfull if you need to upload several files of educational courses. You could even reencode, autofill the metadata (as descripton, title...) of your posts, see the image example of TurboShareKit:

![](https://media.discordapp.net/attachments/714535111374405632/722146553099190322/unknown.png?width=580&height=456)

They are uploaders, but some times I need to **rescue content** from the internet, sometimes we lose access of some youtube, vimeo or any stream account and in order to restore this content I use [youtube-dl](https://open.lbry.com/@vlad:e/Youtube-DL:6?r=587XHbBRBftaXBcauWBHBaTMspyu1ojN) and then I upload in Lbry Using the desktop app or the API. 

So, I thought that could be a time-saver if I could do both actions at once. 
Then I made the following **Python Script** : 

**Please watch the video**

<iframe id="lbry-iframe" width="560" height="315" src="https://lbry.tv/$/embed/lbryuploader/c738bacc2d7b263b676dac0326ed64d156ea4350" allowfullscreen></iframe>

(video soundtrack : [FreeMusicArchive](https://open.lbry.com/@MusicBrasil:0?r=587XHbBRBftaXBcauWBHBaTMspyu1ojN))

My goal is to make this script the first step to a more accessible online tool, maybe a website where you just put the URL and fill a form the parameters of the file you are uploading, something like that: 
![](https://i.postimg.cc/1R2R69Bg/Screenshot-2.png)

----
- PS1: 
It requires [lbrynet.exe](https://github.com/lbryio/lbry-sdk/releases) in the same folder of the [LBRYUPdemo.py](https://open.lbry.com/@SHORTCUT:b/LBRYupdemo:4?r=587XHbBRBftaXBcauWBHBaTMspyu1ojN) and I have [youtube-dl](https://open.lbry.com/@vlad:e/Youtube-DL:6?r=587XHbBRBftaXBcauWBHBaTMspyu1ojN) in my OS.path directory, if you don't ffmpeg.exe must be in the same folder as well   
![](https://i.postimg.cc/PJSw-zNXv/Screenshot-3.png)
- PS2.: 
You can skip some inputs if you insert your "channel_id", for example, directly in the script and then run it

 
<iframe id="lbry-iframe" width="560" height="315" src="https://lbry.tv/$/embed/LBRYupdemo/4ba683cbe0ff872993bcf7be0bfb4d6d6cf40de1" allowfullscreen></iframe>
