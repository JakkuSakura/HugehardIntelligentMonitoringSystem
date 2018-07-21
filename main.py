from MonitorPool import  MonitorPool
import MonitorSession
import Database


class Backend:
    def __init__(self):
        self.is_running = True
        self.monitor_pool = MonitorPool()
        self.delay = 0.1
    def read_config(self):
        monitors = Database.Monitor.fetch_all()
        for e in monitors:
            self.monitor_pool.addMonitor(e)


    def run(self):
        def operate(monitor):
            if monitor.type == 'entrance':
                pass
            else:
                pass
        while self.is_running:
           self.monitor_pool.foreachMonitor(operate)

if __name__ == '__main__':
    backend = Backend()
