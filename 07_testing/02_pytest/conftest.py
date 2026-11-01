import pytest

from app import Figure

# Скільки разів pytest створив fixture allowed_figures (для перевірки scope="module")
created = {"allowed_figures": 0}


@pytest.fixture
def square():
    return Figure("квадрат", 5)


@pytest.fixture
def length():
    return 10


@pytest.fixture
def figure_10(length):
    """Фігура з довжиною 10; залежить від fixture length."""
    return Figure("прямокутник", length)


@pytest.fixture(scope="module")
def allowed_figures():
    created["allowed_figures"] += 1
    return tuple(Figure.FIGURES)


@pytest.fixture
def allowed_figures_created():
    return created["allowed_figures"]
