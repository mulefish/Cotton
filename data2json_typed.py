"""Convert HD detail records from a fixed-width EWR file into JSON data."""

import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Callable, ClassVar, List, Optional, Tuple


@dataclass
class HDRecord:
    """Structured view of a single HD detail record."""

    # Identifier-style fields are kept as strings (even if they contain digits).
    # Measurement-oriented fields are stored as integers so math/analysis works naturally.
    warehouseCode: Optional[str] = None
    electronicReceiptNumber: Optional[str] = None
    cropYear: Optional[str] = None
    issueDate: Optional[str] = None 
    tareWeightLb: Optional[int] = None
    netWeightLb: Optional[int] = None
    baggingCode: Optional[str] = None
    tieCode: Optional[str] = None
    compressionCode: Optional[str] = None
    receivingPaidFlag: Optional[str] = None
    loadingPaidFlag: Optional[str] = None
    compressionPaidFlag: Optional[str] = None
    ginCode: Optional[str] = None
    ginTag: Optional[str] = None
    storagePaidThrough: Optional[str] = None
    classDate: Optional[str] = None
    colorGrade: Optional[str] = None
    stapleCode: Optional[str] = None
    micronaire: Optional[int] = None
    strength: Optional[int] = None
    leafGrade: Optional[str] = None
    extraneousMatter: Optional[str] = None
    remarks: Optional[str] = None
    hviColor: Optional[str] = None
    colorQuadrant: Optional[str] = None
    hviRd: Optional[int] = None
    hviPlusB: Optional[int] = None
    trashPercent: Optional[int] = None
    fiberLengthCode: Optional[int] = None
    uniformityIndex: Optional[int] = None

    @staticmethod
    def _to_int(value: str) -> Optional[int]:
        """Convert a substring to an int, or return None if the field is blank."""
        stripped = value.strip()
        if not stripped:
            return None
        return int(stripped)

    @staticmethod
    def _to_str(value: str) -> Optional[str]:
        """Normalize a substring to a trimmed string (or None if blank)."""
        stripped = value.strip()
        return stripped if stripped else None

    FIELDS: ClassVar[List[Tuple[str, int, int, Callable[[str], Optional[object]]]]] = [
        # (attribute name, start column, end column, converter)
        ("warehouseCode", 2, 7, _to_str.__func__),
        ("electronicReceiptNumber", 8, 14, _to_str.__func__),
        ("cropYear", 15, 18, _to_str.__func__),
        ("issueDate", 19, 26, _to_str.__func__),
        ("tareWeightLb", 27, 28, _to_int.__func__),
        ("netWeightLb", 29, 31, _to_int.__func__),
        ("baggingCode", 32, 32, _to_str.__func__),
        ("tieCode", 33, 33, _to_str.__func__),
        ("compressionCode", 35, 35, _to_str.__func__),
        ("receivingPaidFlag", 45, 45, _to_str.__func__),
        ("loadingPaidFlag", 46, 46, _to_str.__func__),
        ("compressionPaidFlag", 48, 48, _to_str.__func__),
        ("ginCode", 63, 67, _to_str.__func__),
        ("ginTag", 68, 74, _to_str.__func__),
        ("storagePaidThrough", 75, 82, _to_str.__func__),
        ("classDate", 273, 280, _to_str.__func__),
        ("colorGrade", 289, 290, _to_str.__func__),
        ("stapleCode", 291, 292, _to_str.__func__),
        ("micronaire", 293, 294, _to_int.__func__),
        ("strength", 295, 297, _to_int.__func__),
        ("leafGrade", 299, 299, _to_str.__func__),
        ("extraneousMatter", 300, 301, _to_str.__func__),
        ("remarks", 302, 303, _to_str.__func__),
        ("hviColor", 304, 305, _to_str.__func__),
        ("colorQuadrant", 306, 306, _to_str.__func__),
        ("hviRd", 307, 309, _to_int.__func__),
        ("hviPlusB", 310, 312, _to_int.__func__),
        ("trashPercent", 313, 314, _to_int.__func__),
        ("fiberLengthCode", 315, 317, _to_int.__func__),
        ("uniformityIndex", 318, 320, _to_int.__func__),
    ]

    @classmethod
    def from_line(cls, line: str) -> "HDRecord":
        """Parse one fixed-width line into an HDRecord instance."""

        values = {}
        for field_name, start, end, converter in cls.FIELDS:
            raw = line[start - 1 : end]
            values[field_name] = converter(raw)
        return cls(**values)

    def toJson(self) -> str:
        """Serialize the record into a JSON string."""
        return json.dumps(asdict(self), indent=2)


def main() -> None:
    """Read the first two HD records and print their JSON representation."""

    path = Path("data/testbales01.txt")
    lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()

    records = []
    for idx, line in enumerate(lines):
        # Only show the first two records, mirroring the behaviour of data2json.py
        if idx >= 2:
            break
        # Skip blank/whitespace lines just in case
        if not line.strip():
            continue
        record = HDRecord.from_line(line)
        records.append({"lineNumber": idx + 1, "record": asdict(record)})

    # Pretty-print the collected records as JSON
    print(json.dumps(records, indent=2))


if __name__ == "__main__":
    main()
