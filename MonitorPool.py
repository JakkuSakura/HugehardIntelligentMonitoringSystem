from typing import List

from MonitorSession import MonitorSession


class MonitorPool:
    def __init__(self):
        self.monitors: List[MonitorSession] = []

    def addMonitor(self, monitor):
        self.monitors.append(monitor)

    def getMonitor(self, index):
        return self.monitors[index]

    def getMonitors(self):
        return self.monitors

    def remove(self, monitor):
        self.monitors.remove(monitor)
