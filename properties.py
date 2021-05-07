class Properties:
    def __init__(self, name, buy_rate, rent_rate):
        self._name = name
        self._buy_rate = buy_rate
        self._rent_rate = rent_rate

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

    def get_buy_rate(self):
        return self._buy_rate

    def set_buy_rate(self, new_buy_rate):
        self._buy_rate = new_buy_rate

    def get_rent_rate(self):
        return self._buy_rate

    def set_rent_rate(self, new_rent_rate):
        self._rent_rate = new_rent_rate
