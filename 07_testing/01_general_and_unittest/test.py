import unittest
from random import choice, randint

from app import Figure

class TestFigure(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Виконається лише раз на початку тестів
        """
        pass

    def setUp(self) -> None:
        """Виконується кожного разу коли запускається тест
        """
        self.figure = choice(Figure.FIGURES)
        self.length = randint(1, 10)
        self.obj = Figure(self.figure, self.length)
        return super().setUp()

    def tearDown(self) -> None:
        del self.obj
        return super().tearDown()

    def test_figure_type(self):
        print(f"Тестуємо вивід, має бути: {self.figure} == {self.obj.get_figure_type}")
        self.assertEqual(self.figure, self.obj.get_figure_type, "Властивість get_figure_type повертає непривильну фігуру!")

    def test_figure_lengh(self):
        self.assertEqual(self.length, self.obj.get_figure_length, "Властивість get_figure_length повертає непривильну довжину!")

    def test_obj(self):
        with self.assertRaises(AssertionError):
            Figure("коло", 1) # Спробуємо створити обєкт з недозволеними параметрими, в нас має бути помилка AssertionError


class TestFigureAngles(unittest.TestCase):
    """Тести властивості get_angles."""

    def test_square_angles(self):
        self.assertEqual(4, Figure("квадрат", 5).get_angles)

    def test_rectangle_angles(self):
        self.assertEqual(4, Figure("прямокутник", 7).get_angles)

    def test_triangle_angles(self):
        self.assertEqual(3, Figure("трикутник", 3).get_angles)


class TestFigureInvalidData(unittest.TestCase):
    """Граничні та помилкові дані."""

    def test_zero_length(self):
        with self.assertRaises(AssertionError):
            Figure("квадрат", 0)

    def test_negative_length(self):
        with self.assertRaises(AssertionError):
            Figure("трикутник", -5)

    def test_unknown_figure_type(self):
        with self.assertRaises(AssertionError) as context:
            Figure("ромб", 3)
        self.assertIn("Дозволені фігури", str(context.exception))

    def test_min_valid_length(self):
        # 1 — найменша допустима довжина, об'єкт має створитися
        self.assertEqual(1, Figure("квадрат", 1).get_figure_length)


class TestFigureSubTest(unittest.TestCase):
    """subTest: один тест перевіряє всі типи фігур."""

    def test_all_figures(self):
        expected_angles = {"квадрат": 4, "прямокутник": 4, "трикутник": 3}
        for figure_type in Figure.FIGURES:
            for length in [1, 5, 10]:
                with self.subTest(figure=figure_type, length=length):
                    fig = Figure(figure_type, length)
                    self.assertEqual(figure_type, fig.get_figure_type)
                    self.assertEqual(length, fig.get_figure_length)
                    self.assertEqual(expected_angles[figure_type], fig.get_angles)


if __name__ == '__main__':
    unittest.main(verbosity=2)
