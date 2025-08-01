from inventory import TeaInventory
from journal import TeaJournal
from timer import TeaTimer


class ChasenApp:
    def __init__(self):
        print("ChasenApp starting...")
        self.inventory = TeaInventory()
        self.journal = TeaJournal()
        self.timer = TeaTimer()

        # self.inventory.add_tea(
        #     name="Crimson Pigeon",
        #     primary_type="Oolong",
        #     subtype="Oriental Beauty",
        #     source="Taiwan Sourcing",
        #     recommended_amount_tea=5,
        #     recommended_water_ml=100,
        #     recommended_water_temp=95,
        #     recommended_time_secs=60
        # )

        self.inventory.list_teas()

    def run(self):
        print("ChasenApp running...")
