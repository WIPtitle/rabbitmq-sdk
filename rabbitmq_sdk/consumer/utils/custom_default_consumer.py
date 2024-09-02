class CustomDefaultConsumer:
    def __init__(self, channel=None):
        self._channel = channel
        self._consumer_tag = None

    def handle_consume_ok(self, consumer_tag):
        self._consumer_tag = consumer_tag

    def handle_cancel_ok(self, consumer_tag):
        pass

    def handle_cancel(self, consumer_tag):
        pass

    def handle_shutdown_signal(self, consumer_tag, sig):
        pass

    def handle_recover_ok(self, consumer_tag):
        pass

    def handle_delivery(self, consumer_tag, method, properties, body):
        pass

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, channel):
        self._channel = channel

    @property
    def consumer_tag(self):
        return self._consumer_tag
