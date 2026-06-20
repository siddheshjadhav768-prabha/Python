class Device:
    def operate(self):
        print("Operating Device")


class Camera(Device):
    def operate(self):
        print("Taking Photos")


class Phone(Device):
    def operate(self):
        print("Making Calls")


class SmartPhone(Phone):
    def operate(self):
        print("Calling, Browsing Internet and Taking Photos")


devices = [
    Camera(),
    Phone(),
    SmartPhone()
]

for device in devices:
    device.operate()