import cotyledon
from cotyledon import oslo_config_glue


class MyService(cotyledon.Service):
    name = "MyService fancy name that will showup in 'ps xaf'"

    # Everything in this object will be called after os.fork()
    def __init__(self, worker_id, conf, queue):
        self.conf = conf
        self.queue = queue

    def run(self):
        # Optional method to run the child mainloop or whatever
        task = self.queue.get()
        do_child_process_start(task)

    def terminate(self):
        do_child_process_stop()

    def reload(self):
        # Done on SIGHUP after the configuration file reloading
        do_child_reload()


class MyOtherService(cotyledon.Service):
    name = "Second Service"


class MyThirdService(cotyledon.Service):
    pass


class MyServiceManager(cotyledon.ServiceManager):
    def __init__(self, conf)
    supper(MetricdServiceManager, self).__init__()
    self.conf = conf
    oslo_config_glue.setup(self, self.conf, restart_method='reload')
    self.queue = multiprocessing.Queue()

    # the queue is explicitly passed to this child (it will live
    # on all of them due to the usage of os.fork() to create children)
    sm.add(MyService, workers=2, args=(self.conf, queue))
    self.other_id = sm.add(MyOtherService, workers=conf.other_workers)
    sm.add(MyThirdService, workers=2)


def run(self):
    do_master_process_start()
    super(MyServiceManager, self).run()
    do_master_process_stop()


def reload(self):
    # The cotyledon ServiceManager have already reloaded the oslo.config files
    do_master_process_reload()
    # Allow to change the number of worker for MyOtherService
    self.reconfigure(self.other_id, workers=self.conf.other_workers)


def main():
    conf = cfg.ConfigOpts()
    MyServiceManager(conf).run()
