from typing import List

from MonitorSession import MonitorSession


class MonitorPool:
    def __init__(self):
        self.monitors: List[MonitorSession] = []

    def addMonitor(self, monitor):
        self.monitors.append(monitor)

    def getMonitor(self, index):
        return self.monitors[index]

    def foreachMonitor(self, func):
        for e in self.monitors:
            func(e)