import multiprocessing
from oslo_service import service
from oslo_config import cfg


class MyService(service.Service):
    def __init__(self, conf):
        # called before os.fork()
        self.conf = conf
        self.queue = multiprocessing.Queue()

    def start(self):
        # called when application start (parent process start)
        # and
        # called just after os.fork()
        if self.master_pid == os.getpid():
            do_master_process_start()
        else:
            task = self.queue.get()
            do_child_process_start(task)

    def stop(self):
        # called when children process stop
        # and
        # called when application stop (parent process stop)
        if self.master_pid == os.getpid():
            do_master_process_stop()
        else:
            do_child_process_stop()

    def restart(self):
        # called on SIGHUP
        if self.master_pid == os.getpid():
            do_master_process_reload()
        else:
            # Can't be reach oslo.service currently prefers to
            # kill the child process for safety purpose
            do_child_process_reload()


class MyOtherService(service.Service):
    pass


class MyThirdService(service.Service):
    pass


def main():
    conf = cfg.COnfigOpts()
    service = MyService(conf)
    launcher = service.launch(conf, service, workers=2,
                              restart_method='reload')
    launch.launch_service(MyOtherService(), workers=conf.other_workers)

    # Obviously not recommande, because two objects will handle the
    # lifetime of the masterp process but some application does this, so...
    launcher2 = service.launch(conf, MyThirdService(), workers=2,
                               restart_method='restart')

    launcher.wait()
    launcher2.wait()

    # Here, we have no way to change the number of worker dyamically.
