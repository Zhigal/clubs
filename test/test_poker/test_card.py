import random

import pytest

from clubs import error, poker


def test_draw():

    deck = poker.Deck(2, 3)

    cards = deck.draw(1)
    assert len(cards) == 1

    cards = deck.draw(3)
    assert len(cards) == 3

    cards = deck.draw(4)
    assert len(cards) == 2

    cards = deck.draw(1)
    assert len(cards) == 0


def test_trick():
    random.seed(42)

    deck = poker.Deck(4, 13).trick(['Ah', '2s'])

    cards = deck.draw(2)
    assert cards[0] == poker.Card('Ah')
    assert cards[1] == poker.Card('2s')

    deck = deck.shuffle()
    cards = deck.draw(2)
    assert cards[0] == poker.Card('Ah')
    assert cards[1] == poker.Card('2s')

    deck = deck.untrick().shuffle()
    cards = deck.draw(2)
    assert cards[0] != poker.Card('Ah')
    assert cards[1] != poker.Card('2s')


def test_invalid_init():
    with pytest.raises(error.InvalidRankError):
        poker.Card('1s')
        poker.Card('1t')

    with pytest.raises(error.InvalidSuitError):
        poker.Card('At')