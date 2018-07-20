class NotCompleted(Exception):
    def __init__(self):
        super().__init__("Not completed")


class CamException(Exception):
    def __init__(self, st):
        super().__init__(st)


class CamConnectError(CamException):
    def __init__(self):
        super().__init__("Camera connect error")
