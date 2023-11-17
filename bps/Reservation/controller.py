from .model import Reservation


class ReservationController:
    def __init__(self):
        self.model = Reservation()

    def get(self):
        data = self.model.get()
        if not data:
            return {'message': 'no data found!'}, 404
        return {'data': data}
