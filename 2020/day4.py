import re

required_fields = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    "cid",
]


class Passport:
    def __init__(self, str):
        self.str = str
        tmp = [f.split(":") for f in str.split(" ")]
        self.fields = {f[0]: f[1] for f in tmp}

    def __str__(self):
        return self.str

    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    def validate_byr(self):
        byr = self.fields.get("byr")
        if byr:
            return bool(re.fullmatch(r"\d{4}", byr)) and (
                int(byr) >= 1920 and int(byr) <= 2002
            )
        return False

    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    def validate_iyr(self):
        iyr = self.fields.get("iyr")
        if not iyr:
            return False
        return bool(re.fullmatch(r"\d{4}", iyr)) and (
            int(iyr) >= 2010 and int(iyr) <= 2020
        )

    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    def validate_eyr(self):
        eyr = self.fields.get("eyr")
        if not eyr:
            return False
        return bool(re.fullmatch(r"\d{4}", eyr)) and (
            int(eyr) >= 2020 and int(eyr) <= 2030
        )

    # hgt (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
    def validate_hgt(self):
        hgt = self.fields.get("hgt")
        if hgt:
            match = re.fullmatch(r"(\d+)(cm|in)", hgt)
            if match:
                n = int(match.group(1))
                unit = match.group(2)
                return (unit == "cm" and (150 <= n <= 193)) or (
                    unit == "in" and (59 <= n <= 76)
                )
        return False

    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    def validate_hcl(self):
        hcl = self.fields.get("hcl")
        if hcl:
            return bool(re.fullmatch(r"#[0-9a-f]{6}", hcl))
        return False

    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    def validate_ecl(self):
        ecl = self.fields.get("ecl")
        if ecl:
            return bool(re.fullmatch(r"(amb|blu|brn|gry|grn|hzl|oth)", ecl))
        return False

    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    def validate_pid(self):
        pid = self.fields.get("pid")
        if not pid:
            return False
        return bool(re.fullmatch(r"\d{9}", pid))

    # cid (Country ID) - ignored, missing or not.
    def validate_cid(self):
        return True

    def is_valid(self):
        return (
            self.validate_byr()
            and self.validate_iyr()
            and self.validate_eyr()
            and self.validate_hgt()
            and self.validate_hcl()
            and self.validate_ecl()
            and self.validate_pid()
            and self.validate_cid()
        )

    def has_required(self):
        temp_required = required_fields[:]
        temp_required.remove("cid")
        tmp = [r in self.fields for r in temp_required]
        return all(tmp)


def get_inputs():
    inputs = []
    with open("./day4_input") as file:
        inputs = file.read().strip().split("\n\n")

    return [line.replace("\n", " ") for line in inputs]


if __name__ == "__main__":
    all_passports = get_inputs()

    has_required = [p for p in all_passports if Passport(p).has_required()]
    print("Number of passports with required fields: {}".format(len(has_required)))

    valid_passorts = [p for p in all_passports if Passport(p).is_valid()]

    for p in valid_passorts:
        print(p, Passport(p).is_valid())

    print("Number of valid passports: {}".format(len(valid_passorts)))
