def check_passport(passport):
    check_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    fields = []
    for line in passport.splitlines():
        fields.extend(line.split(' '))

    passport_dic = {}
    for field in fields:
        (key, value) = field.split(':')
        passport_dic[key] = value

    for cf in check_fields:
        if cf not in passport_dic:
            return False
    return True


if __name__ == '__main__':

    with open('input.txt', 'r') as f:
        data = f.read()
    passports = data.split("\n\n")

    valid_passport = 0
    for passport in passports:
        if check_passport(passport):
            valid_passport += 1

    print(valid_passport)
