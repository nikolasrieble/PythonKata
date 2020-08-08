class Theater:
    def __init__(self):
        self.seats = None

    def get_seats(self, number_of_seats: int) -> [[]]:
        seats = self.compute_seat_scores()
        if len(seats) >= number_of_seats:
            return seats[:number_of_seats]
        return []

    def get_row_length(self, row_id: int) -> int:
        return len(self.seats[row_id])

    def seat_score(self, row_id: int, seat_id: int) -> float:
        row_length = self.get_row_length(row_id)
        return abs((row_length-1) / 2 - seat_id)

    def compute_seat_scores(self):
        seats = []
        scores = []
        for row_id, row in enumerate(self.seats):
            for seat_id, seat in enumerate(row):
                if seat:
                    seats.append([row_id, seat_id])
                    scores.append(self.seat_score(row_id, seat_id))
        sorted_seats = sorted(seats, key=lambda x: scores[seats.index(x)])
        return sorted_seats
