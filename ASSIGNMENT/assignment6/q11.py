class Notification:
    def send(self):
        pass


class EmailNotification(Notification):
    def send(self):
        print("Email Notification Sent")


class SMSNotification(Notification):
    def send(self):
        print("SMS Notification Sent")


class PushNotification(Notification):
    def send(self):
        print("Push Notification Sent")


notifications = [
    EmailNotification(),
    SMSNotification(),
    PushNotification()
]

for notification in notifications:
    notification.send()