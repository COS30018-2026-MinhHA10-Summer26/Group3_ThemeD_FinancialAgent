import unittest

from ai_integration.ingestion.chunking import chunk_documents


class ChunkingTests(unittest.TestCase):
    def test_body_sections_chunk_by_paragraph_and_repeat_heading(self):
        documents = [
            {
                "text": (
                    "Revenue grew 12% year over year and operating margin improved.\n\n"
                    "Management attributed the increase to stronger enterprise demand.\n\n"
                    "Guidance remains unchanged for the second half of the year."
                ),
                "source": "sample.pdf",
                "page": 2,
                "section_title": "Management Discussion",
                "section_type": "body",
            }
        ]

        chunks = chunk_documents(documents, chunk_size=120, overlap=30)

        self.assertEqual(len(chunks), 3)
        self.assertTrue(all(chunk["text"].startswith("Management Discussion\n\n") for chunk in chunks))
        self.assertIn(
            "Revenue grew 12% year over year and operating margin improved.",
            chunks[0]["text"],
        )
        self.assertIn(
            "Management attributed the increase to stronger enterprise demand.",
            chunks[1]["text"],
        )
        self.assertIn(
            "Guidance remains unchanged for the second half of the year.",
            chunks[2]["text"],
        )

    def test_tables_split_by_rows_not_raw_character_windows(self):
        documents = [
            {
                "text": (
                    "Year   Revenue   Net income\n"
                    "2023   100       20\n"
                    "2024   120       25\n"
                    "2025   140       30"
                ),
                "source": "financials.pdf",
                "page": 8,
                "section_title": "Income Statement",
                "section_type": "table",
            }
        ]

        chunks = chunk_documents(documents, chunk_size=75, overlap=0)

        self.assertEqual(len(chunks), 2)
        self.assertTrue(all(chunk["text"].startswith("Income Statement\n[table]\n\n") for chunk in chunks))
        self.assertIn("Year Revenue Net income", chunks[0]["text"])
        self.assertIn("2023 100 20", chunks[0]["text"])
        self.assertIn("2024 120 25", chunks[0]["text"])
        self.assertIn("2025 140 30", chunks[1]["text"])

    def test_long_paragraph_falls_back_to_sentence_chunks(self):
        documents = [
            {
                "text": (
                    "Tesla reported record deliveries in the quarter. "
                    "Gross margin declined due to price cuts and a higher mix of lower-priced vehicles. "
                    "Energy storage deployments reached another all-time high."
                ),
                "source": "earnings.txt",
                "page": 0,
                "section_title": "Quarterly Update",
                "section_type": "body",
            }
        ]

        chunks = chunk_documents(documents, chunk_size=110, overlap=20)

        self.assertGreaterEqual(len(chunks), 2)
        self.assertTrue(all(chunk["text"].startswith("Quarterly Update\n\n") for chunk in chunks))
        self.assertTrue(any("Tesla reported record deliveries in the quarter." in chunk["text"] for chunk in chunks))
        self.assertTrue(
            any(
                "Gross margin declined due to price cuts and a higher mix of lower-priced vehicles."
                in chunk["text"]
                for chunk in chunks
            )
        )


if __name__ == "__main__":
    unittest.main()
