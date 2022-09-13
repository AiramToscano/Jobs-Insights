from src.counter import count_ocurrences


def test_counter():
    path = 'src/jobs.csv'
    word = 'olá'
    assert count_ocurrences(path, word) == 0
    wor2 = "Lead"
    assert count_ocurrences(path, wor2) == 4085
