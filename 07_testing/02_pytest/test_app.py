import pytest

from app import Figure

INVALID_TYPES = ["коло", "ромб", "", "Квадрат", "квадрат ", None]
INVALID_LENGTHS = [0, -1, -100, -0.5]


# --- Основи ---

@pytest.mark.unit
def test_triangle_type():
    assert Figure("трикутник", 4).type == "трикутник"


@pytest.mark.unit
def test_square_length(square):
    assert square.get_figure_length == 5


def test_invalid_figure():
    with pytest.raises(AssertionError):
        Figure("коло", 1)


# --- Параметризація ---

@pytest.mark.parametrize("figure_type", Figure.FIGURES)
def test_allowed_figure(figure_type):
    figure = Figure(figure_type, 1)
    assert figure.type == figure_type
    assert figure.get_figure_length == 1


@pytest.mark.parametrize("figure_type", INVALID_TYPES)
def test_invalid_type(figure_type):
    with pytest.raises(AssertionError, match="Невідомий тип фігури"):
        Figure(figure_type, 5)


@pytest.mark.parametrize("length", INVALID_LENGTHS)
def test_invalid_length(length):
    with pytest.raises(AssertionError, match="Довжина має бути більшою за 0!"):
        Figure("квадрат", length)


@pytest.mark.parametrize("length", [None, "5", [5]], ids=["None", "рядок", "список"])
def test_invalid_length_type(length):
    with pytest.raises(TypeError):
        Figure("квадрат", length)


# --- Fixture з довжиною 10 ---

def test_figure_10(figure_10, length):
    assert figure_10.type == "прямокутник"
    assert figure_10.length == length == 10
    assert figure_10.get_figure_length == 10


# --- Fixture зі scope="module" ---

def test_allowed_figures_count(allowed_figures, allowed_figures_created):
    assert len(allowed_figures) == 3
    assert allowed_figures_created == 1


def test_allowed_figures_content(allowed_figures, allowed_figures_created):
    assert "трикутник" in allowed_figures
    assert allowed_figures_created == 1  # fixture не створювалась удруге
