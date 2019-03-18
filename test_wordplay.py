import pytest
from wordplay import score_word


@pytest.mark.parametrize("word, score", [
    ('', 0),
    ('a', 1),
    ('bird', 7),
    ('cat', 5),
    ('fish', 10),
    ('bliffy', 17),
    ('xylophone', 24),
    ('leet-speak', 15),
    ('l33t-sp34k', 11),
])
def test_score_word(word, score):
    assert score_word(word) == score
