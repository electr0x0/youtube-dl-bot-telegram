from __future__ import unicode_literals
import yt_dlp as youtube_dl

#Collector for the downloaded file name
class FilenameCollectorPP(youtube_dl.postprocessor.common.PostProcessor):
    def __init__(self):
        super(FilenameCollectorPP, self).__init__(None)
        self.filenames = []

    def run(self, information):
        self.filenames.append(information["filepath"])
        return [], information
    
#Video Downloader
def downloadVideo(url):
    youtube_dl_options = {
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best",
        "outtmpl": "%(title)s.%(ext)s",
        "restrictfilenames": True,
        "nooverwrites": True,
        "writedescription": True,
        "writeinfojson": True,
        "writeannotations": True,
        "writethumbnail": True,
        "writesubtitles": True,
        "writeautomaticsub": True
    }
    ydl = youtube_dl.YoutubeDL(youtube_dl_options)
    filename_collector = FilenameCollectorPP()
    ydl.add_post_processor(filename_collector)
    ydl.download([url])
    return filename_collector.filenames[0]
