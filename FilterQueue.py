import asyncio

class FilterQueue(asyncio.Queue):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.window = None

    def __contains__(self, ffilter):
        for elem in self._queue:
            if ffilter(elem):
                return True
        return False

    def _get(self):
        elem = self._queue.popleft()
        if self._queue:
            self.window = self._queue[0]
        else:
            self.window = None
        return elem

    def _put(self, elem):
        self._queue.append(elem)
        if self.window is None:
            self.window = elem

    def later(self):
        if not self._queue:
            self.window = None
            raise asyncio.QueueEmpty
        elem = self._get()
        self._put(elem)
    
    #From source code: Lib/asyncio/queues.py

    async def get(self, ffilter=None):
        if ffilter is not None and ffilter in self:
            while not ffilter(self.window):
                self.later()
        while self.empty():
            getter = self._get_loop().create_future()
            self._getters.append(getter)
            try:
                await getter
            except:
                getter.cancel()
                try:
                    self._getters.remove(getter)
                except ValueError:
                    pass
                if not self.empty() and not getter.cancelled():
                    self._wakeup_next(self._getters)
                raise
        return self.get_nowait()
