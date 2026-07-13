#!/usr/bin/env python3
"""Convert Telegram's exported contact list to CSV and vCard files."""

import argparse
import csv
import json
from pathlib import Path


CSV_COLUMNS = ("first_name", "last_name", "phone_number")


def convert_contacts(source: Path, csv_output: Path, vcf_output: Path) -> int:
    """Convert contacts from a Telegram JSON export and return their count."""
    with source.open(encoding="utf-8") as contacts_file:
        data = json.load(contacts_file)

    contacts = data["contacts"]["list"]

    with (
        csv_output.open("w", encoding="utf-8-sig", newline="") as csv_file,
        vcf_output.open("w", encoding="utf-8-sig", newline="") as vcf_file,
    ):
        writer = csv.DictWriter(csv_file, fieldnames=CSV_COLUMNS)
        writer.writeheader()

        for contact in contacts:
            first_name = str(contact["first_name"])
            last_name = str(contact["last_name"])
            phone_number = str(contact["phone_number"])

            if phone_number.startswith("0098"):
                phone_number = "0" + phone_number[4:]

            writer.writerow(
                {
                    "first_name": first_name,
                    "last_name": last_name,
                    "phone_number": phone_number,
                }
            )
            vcf_file.write("BEGIN:VCARD\nVERSION:3.0\n")
            vcf_file.write(f"N:{last_name}; {first_name};;;\n")
            vcf_file.write(f"FN: {first_name} {last_name}\n")
            vcf_file.write(f"TEL: {phone_number}\n")
            vcf_file.write("END:VCARD\n")

    return len(contacts)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "source",
        nargs="?",
        type=Path,
        default=Path("result.json"),
        help="Telegram JSON export (default: result.json)",
    )
    parser.add_argument(
        "--csv",
        type=Path,
        default=Path("contacts.csv"),
        help="CSV output path (default: contacts.csv)",
    )
    parser.add_argument(
        "--vcf",
        type=Path,
        default=Path("contacts.vcf"),
        help="vCard output path (default: contacts.vcf)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    count = convert_contacts(args.source, args.csv, args.vcf)
    print(f"Exported {count} contacts to {args.csv} and {args.vcf}")


if __name__ == "__main__":
    main()
