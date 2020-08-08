import pytest

from KataTheater.theater import Theater

theater = Theater()


@pytest.mark.parametrize("seats,n_request,expected",
                         [([[False]], 1, []),
                          ([[True]], 1, [[0, 0]]),
                          ([[True]], 2, []),
                          ([[False]], 2, [])])
def test_minimal_theater(seats, n_request, expected):
    # given
    theater.seats = seats
    # when
    result = theater.get_seats(n_request)
    # then
    assert sorted(result) == sorted(expected)


@pytest.mark.parametrize("seats,n_request,expected",
                         [([[False, False]], 1, []),
                          ([[True, True]], 1, [[0, 0]]),
                          ([[True, False]], 2, []),
                          ([[False, True]], 2, []),
                          ([[True, True, True]], 1, [[0, 1]]),
                          ([[True, True, True]], 2, [[0, 0], [0, 1]])
                          ])
def test_one_row_theater(seats, n_request, expected):
    # given
    theater.seats = seats
    # when
    result = theater.get_seats(n_request)
    # then
    assert sorted(result) == sorted(expected)
