import unittest
from main import find_promo_codes

class TestPromoFinder(unittest.TestCase):
    """Тестирование функции поиска промокодов."""

    def test_simple_promo(self):
        """Простой промокод с пробелом."""
        text = "Ваш промокод SALE2027 дает скидку."
        self.assertEqual(find_promo_codes(text), ["SALE2027"])

    def test_with_colon(self):
        """Промокод с двоеточием."""
        text = "Промокод: BLACKFRIDAY"
        self.assertEqual(find_promo_codes(text), ["BLACKFRIDAY"])

    def test_with_dash(self):
        """Промокод с тире."""
        text = "Скидка - PROMO67"
        self.assertEqual(find_promo_codes(text), ["PROMO67"])

    def test_multiple_promos(self):
        """Несколько промокодов в тексте."""
        text = "Промокод SALE2027 и скидка PROMO67. А также промо UDURG."
        expected = ["SALE2027", "PROMO67", "UDURG"]
        self.assertEqual(find_promo_codes(text), expected)

    def test_duplicate_promos(self):
        """Дубликаты промокодов должны удаляться."""
        text = "Промокод AAAA6767... И снова промокод AAAA6767!"
        self.assertEqual(find_promo_codes(text), ["AAAA6767"])

    def test_ignore_too_short(self):
        """Промокод меньше 3 символов игнорируется."""
        text = "Промокод X3"
        self.assertEqual(find_promo_codes(text), [])

    def test_ignore_too_long(self):
        """Промокод больше 15 символов игнорируется."""
        text = "Промокод VKAMINEV6UTRAFOTOGRAFIYATVOYA"
        self.assertEqual(find_promo_codes(text), [])

    def test_ignore_lowercase(self):
        """Код должен быть только из заглавных букв."""
        text = "Промокод leva200"
        self.assertEqual(find_promo_codes(text), [])

    def test_no_promos(self):
        """Текст без промокодов."""
        text = "Здесь просто текст без скидок."
        self.assertEqual(find_promo_codes(text), [])

    def test_case_insensitive_keyword(self):
        """Ключевое слово 'ПРОМОКОД' в верхнем регистре."""
        text = "ПРОМОКОД VERITY14"
        self.assertEqual(find_promo_codes(text), ["VERITY14"])

if __name__ == '__main__':
    unittest.main()
