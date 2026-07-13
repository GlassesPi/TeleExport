import csv
import json
import tempfile
import unittest
from pathlib import Path

from TeleExport import convert_contacts


class ConvertContactsTest(unittest.TestCase):
    def test_converts_telegram_export_without_third_party_dependencies(self):
        data = {
            "contacts": {
                "list": [
                    {
                        "first_name": "Ada",
                        "last_name": "Lovelace",
                        "phone_number": "+441234",
                    },
                    {
                        "first_name": "Ali",
                        "last_name": "Rezaei",
                        "phone_number": "009812345",
                    },
                ]
            }
        }

        with tempfile.TemporaryDirectory() as directory:
            directory = Path(directory)
            source = directory / "result.json"
            csv_output = directory / "contacts.csv"
            vcf_output = directory / "contacts.vcf"
            source.write_text(json.dumps(data), encoding="utf-8")

            count = convert_contacts(source, csv_output, vcf_output)

            self.assertEqual(count, 2)
            with csv_output.open(encoding="utf-8-sig", newline="") as csv_file:
                self.assertEqual(
                    list(csv.DictReader(csv_file)),
                    [
                        {
                            "first_name": "Ada",
                            "last_name": "Lovelace",
                            "phone_number": "+441234",
                        },
                        {
                            "first_name": "Ali",
                            "last_name": "Rezaei",
                            "phone_number": "012345",
                        },
                    ],
                )

            vcard = vcf_output.read_text(encoding="utf-8-sig")
            self.assertEqual(vcard.count("BEGIN:VCARD"), 2)
            self.assertIn("FN: Ada Lovelace", vcard)
            self.assertIn("TEL: 012345", vcard)


if __name__ == "__main__":
    unittest.main()
