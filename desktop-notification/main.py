from plyer import notification
import time

if __name__ == "__main__":
    while True:
       notification.notify(
        title="Scheduled Notification",
        message="This is your scheduled notification.",
        app_name="NotifierApp",
        timeout=10  
                         )
       time.sleep(15)
   