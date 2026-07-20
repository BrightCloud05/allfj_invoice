import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / "index.html").read_text(encoding="utf-8")


class MultilineDescriptionTests(unittest.TestCase):
    def test_line_item_detail_uses_multiline_textarea(self):
        self.assertRegex(
            HTML,
            re.compile(
                r'<textarea[^>]*data-f="subtitle"[^>]*>\$\{esc\(it\.subtitle\)\}</textarea>',
                re.DOTALL,
            ),
        )

    def test_invoice_preview_preserves_description_line_breaks(self):
        self.assertRegex(
            HTML,
            re.compile(r'\.item-row \.desc \.s\s*\{[^}]*white-space:\s*pre-line', re.DOTALL),
        )

    def test_multiline_detail_field_has_usable_default_height(self):
        self.assertRegex(
            HTML,
            re.compile(
                r'textarea\[data-f="subtitle"\]\s*\{[^}]*min-height:\s*\d+px',
                re.DOTALL,
            ),
        )

    def test_long_line_items_are_not_split_across_printed_pages(self):
        self.assertRegex(
            HTML,
            re.compile(
                r'@media print\s*\{.*?#sheet \.item-row\s*\{[^}]*break-inside:\s*avoid',
                re.DOTALL,
            ),
        )

    def test_from_section_keeps_brand_and_identifies_sole_trader(self):
        self.assertIn('<div class="co">ALLFJ AI</div>', HTML)
        self.assertIn('${esc(settings.supplierName)} · Sole Trader', HTML)
        self.assertIn('ABN ${esc(settings.abn)}', HTML)


if __name__ == "__main__":
    unittest.main()
