from audio_notification import Audio_Notification
from time import sleep

buzzer = Audio_Notification(27, True)

while True:
    buzzer.warning_on()