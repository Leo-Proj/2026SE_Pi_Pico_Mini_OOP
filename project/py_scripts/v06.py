from audio_notification import Audio_Notification
from time import sleep

buzzer = Audio_Notification(27, True)

print("Testing high frequency short beep")
buzzer.beep(5000, 100)
sleep(2)