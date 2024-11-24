import unittest
from rokas_k_mod_atsiskaitymas.main import crawl_website


class TestCrawlWebsite(unittest.TestCase):
    def test_dict_format(self):
        result = crawl_website("https://15min.lt", output_format="dict")
        self.assertIn("titles", result)
        self.assertIn("links", result)

    def test_list_format(self):
        result = crawl_website("https://lrytas.lt", output_format="list")
        self.assertIsInstance(result, list)

    def test_csv_format(self):
        result = crawl_website("https://delfi.lt", output_format="csv")
        self.assertTrue(result.startswith("Data saved to output/"))

    def test_empty_url(self):
        result = crawl_website("", output_format="dict")
        self.assertIn("error", result)


if __name__ == "__main__":
    unittest.main()
