from inventory import TeaInventory
from journal import TeaJournal
from timer import TeaTimer

class ChasenApp:
    def __init__(self):
        print("ChasenApp starting...")
        self.inventory = TeaInventory()
        self.journal = TeaJournal()
        self.timer = TeaTimer()

    def run(self):
        print("ChasenApp running...")