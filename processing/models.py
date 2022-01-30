import os
import ffmpeg
from django.conf import settings
from django.db import models


class Video(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    upload = models.FileField(upload_to='uploads/%Y/%m/%d/')

    def convert_to_web_format(self):
        # TODO do hardware encoding
        # make different formats
        filename_with_extension = os.path.basename(self.upload.path)
        filename = filename_with_extension.split('.', 1)[0]
        try:
            f_input = ffmpeg.input(self.upload.path)
            audio = f_input.audio
            video = f_input.video.filter(
                "scale", size="1920x1080")
            subtitles = f_input['s']
            ffmpeg.output(video, audio, subtitles, str(settings.MEDIA_ROOT / f'{filename}.mp4'),
                          vcodec=settings.DEFAULT_VIDEO_ENCODER,
                          acodec=settings.DEFAULT_AUDIO_ENCODER,
                          scodec='mov_text') \
                .run(capture_stdout=True, capture_stderr=True)
        except ffmpeg.Error as e:
            print('stdout:', e.stdout.decode('utf8'))
            print('stderr:', e.stderr.decode('utf8'))
            raise e
