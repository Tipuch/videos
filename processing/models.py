import ffmpeg
from django.conf import settings
from django.db import models


class Video(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    upload = models.FileField(upload_to='uploads/%Y/%m/%d/')

    def convert_to_web_format(self):
        #TODO check quality of output
        # change file name
        # keep subtitles
        # do different quality versions
        ffmpeg.input(self.upload.path)\
            .output(str(settings.MEDIA_ROOT / 'target.mp4'), vcodec=settings.DEFAULT_VIDEO_ENCODER,
                    acodec=settings.DEFAULT_AUDIO_ENCODER)\
            .run(capture_stdout=True, capture_stderr=True)
