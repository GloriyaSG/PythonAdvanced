import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


pattern = r"[A-Za-z]{5,}@[a-z]+.(com|bg|org|net)"
pattern_domain = r"(com|bg|org|net)"


while True:

    command = input()
    if command == "End":
        break
    else:

        if re.findall(pattern,command):
            print("Email is valid")
        else:
            if "@" not in command:
                raise MustContainAtSymbolError("Email must contain @")

            if not re.findall(pattern_domain, command.split(".")[-1]):
                raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
            if len(command.split("@")[0]) <= 4:
                raise NameTooShortError("Name must be more than 4 characters")

