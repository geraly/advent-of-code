import re


def read_passport(passport):
    fields = []
    for line in passport.splitlines():
        fields.extend(line.split(' '))

    passport_dic = {}
    for field in fields:
        (key, value) = field.split(':')
        passport_dic[key] = value

    return passport_dic


def check_passport(passport_dic):
    # check required fields
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for cf in required_fields:
        if cf not in passport_dic:
            return False

    # check each fields
    if int(passport_dic['byr']) < 1920 or 2002 < int(passport_dic['byr']):
        return False

    if int(passport_dic['iyr']) < 2010 or 2020 < int(passport_dic['iyr']):
        return False

    if int(passport_dic['eyr']) < 2020 or 2030 < int(passport_dic['eyr']):
        return False

    m = re.match(r'(\d+)(cm|in)', passport_dic['hgt'])
    if m is None:
        return False
    if m.group(2) == 'cm':
        if int(m.group(1)) < 150 or 193 < int(m.group(1)):
            return False
    elif m.group(2) == 'in':
        if int(m.group(1)) < 59 or 76 < int(m.group(1)):
            return False
    else:
        raise Exception('format error')

    m = re.match(r'#[0-9a-f]{6}$', passport_dic['hcl'])
    if m is None:
        return False

    m = re.match(r'(amb|blu|brn|gry|grn|hzl|oth)$', passport_dic['ecl'])
    if m is None:
        return False

    m = re.match(r'\d{9}$', passport_dic['pid'])
    if m is None:
        return False

    return True


if __name__ == '__main__':

    with open('input.txt', 'r') as f:
        data = f.read()
    passports = data.split("\n\n")

    valid_passport = 0
    for passport in passports:
        if check_passport(read_passport(passport)):
            valid_passport += 1

    print(valid_passport)
