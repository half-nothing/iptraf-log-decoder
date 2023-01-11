from time import perf_counter


class ProcessingBar:
    _total: int
    _start_time: float
    _now: int = 0
    _active: bool = False
    _title: str

    def __init__(self, total: int, title: str = "") -> None:
        self._total = total
        self._title = None if title == "" else title

    def start(self) -> None:
        self._start_time = perf_counter()
        if self._title is not None:
            print(self._title if self._title.endswith(":") else self._title + ":")
        self._active = True
        self.next()

    def next(self) -> None:
        if self._now <= self._total and self._active:
            processed = "*" * int(self._now / self._total * 100)
            unprocessed = "." * int((self._total - self._now) / self._total * 100)
            percentage = (self._now / self._total) * 100
            consuming = perf_counter() - self._start_time
            print("\r{:^3.0f}%[{}{}]{:.2f}s".format(percentage, processed, unprocessed, consuming), end="")
            self._now += 1
        else:
            self.stop()

    def stop(self) -> None:
        if self._active:
            print(f"\nFinish!")
            self._active = False

    def error(self, msg) -> None:
        if self._active:
            print(f"\nError: {msg}")

    def warn(self, msg) -> None:
        if self._active:
            print(f"\nWarning: {msg}")
