from operator import xor


class Password:
    def __init__(self, str):
        self.str = str
        number, letter, password = str.split(" ")
        self.n_first, self.n_last = [int(x) for x in number.split("-")]
        self.condition_letter = letter[0]
        self.password = password

    def __repr__(self):
        return self.str

    def is_valid(self):
        count = self.password.count(self.condition_letter)
        if count >= self.n_first and count <= self.n_last:
            return True
        return False


class PasswordNew(Password):
    def is_valid(self):
        return xor(
            self.password[self.n_first - 1] == self.condition_letter,
            self.password[self.n_last - 1] == self.condition_letter,
        )


def read_inputs():
    inputs = []
    with open("./day2_input", "r") as file:
        inputs = file.readlines()
    return inputs


def get_passwords():
    inputs = read_inputs()
    passwords = [Password(p) for p in inputs]
    passwords_new = [PasswordNew(p) for p in inputs]
    return passwords, passwords_new


def main():
    all_passwords, all_passwords_new = get_passwords()

    valid_passwords = [p for p in all_passwords if p.is_valid()]

    print(
        "According to 1st policy there are {} valid password.".format(
            len(valid_passwords)
        )
    )

    valid_passwords_new = [p for p in all_passwords_new if p.is_valid()]

    print(
        "According to 2st policy there are {} valid password.".format(
            len(valid_passwords_new)
        )
    )


if __name__ == "__main__":
    main()
