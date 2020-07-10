class EventSourcer():
    # Do not change the signature of any functions
    tracker = []
    delete = []

    def __init__(self):
        self.value = 0
        EventSourcer.tracker.append(self.value)

    def add(self, num: int):
        ans = EventSourcer.tracker[-1] + num
        EventSourcer.tracker.append(ans)
        self.value = ans
        print(ans)
        return ans

    def subtract(self, num: int):
        ans = EventSourcer.tracker[-1] - num
        EventSourcer.tracker.append(ans)
        self.value = ans
        return ans

    def undo(self):
        # self.value = EventSourcer.tracker.append(self.value[-1])
        EventSourcer.delete.append(EventSourcer.tracker[-1])
        del EventSourcer.tracker[-1]
        ans = EventSourcer.tracker[-1]
        self.value = ans
        return ans

    def redo(self):
        # self.value = EventSourcer.tracker.append(self.value[-2])
        EventSourcer.tracker.append(EventSourcer.delete[-1])
        del EventSourcer.delete[-1]
        ans = EventSourcer.tracker[-1]
        self.value = ans
        return ans

    def bulk_undo(self, steps: int):
        EventSourcer.delete.append(EventSourcer.tracker[-steps])
        del EventSourcer.tracker[-steps]
        ans = EventSourcer.tracker[-1]
        self.value = ans
        return ans

    def bulk_redo(self, steps: int):
        EventSourcer.tracker.append(EventSourcer.delete[-steps])
        del EventSourcer.delete[-steps]
        ans = EventSourcer.tracker[-1]
        self.value = ans
        return ans
