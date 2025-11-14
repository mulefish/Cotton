import json
from pathlib import Path

# ALL records in data/testbales01.txt are 'HD' - Holder Detail
# These are fixed-width fields
# key = field name, first number start and second number = end column
FIELDS = [
    ("warehouseCode", 2, 7),
    ("electronicReceiptNumber", 8, 14),
    ("cropYear", 15, 18),
    ("issueDate", 19, 26),
    ("tareWeightLb", 27, 28),
    ("netWeightLb", 29, 31),
    ("baggingCode", 32, 32),
    ("tieCode", 33, 33),
    ("compressionCode", 35, 35),
    ("receivingPaidFlag", 45, 45),
    ("loadingPaidFlag", 46, 46),
    ("compressionPaidFlag", 48, 48),
    ("ginCode", 63, 67),
    ("ginTag", 68, 74),
    ("storagePaidThrough", 75, 82),
    ("classDate", 273, 280),
    ("colorGrade", 289, 290),
    ("stapleCode", 291, 292),
    ("micronaire", 293, 294),
    ("strength", 295, 297),
    ("leafGrade", 299, 299),
    ("extraneousMatter", 300, 301),
    ("remarks", 302, 303),
    ("hviColor", 304, 305),
    ("colorQuadrant", 306, 306),
    ("hviRd", 307, 309),
    ("hviPlusB", 310, 312),
    ("trashPercent", 313, 314),
    ("fiberLengthCode", 315, 317),
    ("uniformityIndex", 318, 320),
]

def parse_record(line: str) -> dict:
    """Turn one fixed-width HD detail line into a dict."""
    record = {}
    for name, start, end in FIELDS:
        raw = line[start - 1 : end]
        value = raw.strip()
        if value:
            record[name] = value
    return record

def main():
    path = Path("data/testbales01.txt")
    lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()

    parsed = []
    for idx, line in enumerate(lines):
        if idx >= 2:  # stop after line 2 (0-based index)
            break
        if not line.strip():
            continue  # skip blank lines just in case
        parsed.append({"lineNumber": idx + 1, "record": parse_record(line)})

    print(json.dumps(parsed, indent=2))

if __name__ == "__main__":
    main()