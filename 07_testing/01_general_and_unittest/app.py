class Figure:
    FIGURES = ["квадрат", "прямокутник", "трикутник"]
    def __init__(self, type, length) -> None:
        assert length > 0, "Довжина має бути більшою за 0!"
        assert type in self.FIGURES, "Дозволені фігури: квадрат, прямокутник, трикутник"
        self.type = type
        self.length = length

    @property
    def get_figure_type(self):
        return self.type

    @property
    def get_figure_length(self):
        return self.length # виправлено: раніше повертався self.type

    @property
    def get_angles(self):
        """Кількість кутів фігури."""
        if self.type in ["квадрат", "прямокутник"]:
            return 4
        if self.type == "трикутник":
            return 3
        return 0

def test_app_triangle():
    """Test if we create triangle figure.
    """
    fig = "трикутник"
    triangle = Figure(fig, 4)
    assert triangle.type == fig, f"Фігура має бути {fig}"


def simple_function():
    return True


if __name__ == "__main__":
    # Ручна перевірка властивостей (завдання «Перший приклад», п. 1–2)
    for fig_type, length in [("квадрат", 5), ("прямокутник", 10), ("трикутник", 3)]:
        fig = Figure(fig_type, length)
        print(f"{fig.get_figure_type}: довжина = {fig.get_figure_length}, кутів = {fig.get_angles}")
