import re

data = []

with open('input.txt', 'r') as f:
    lines = f.readlines()

valid_count = 0

for line in lines:
    m = re.match(r"(\d+)-(\d+) (\w): (\w+)$", line)
    if m is None:
        raise Exception("format error")
    first = int(m.group(1)) - 1  # 0 index
    last = int(m.group(2)) - 1  # 0 index
    policy = m.group(3)
    password = m.group(4)

    if len(password) <= last or len(password) <= first:
        continue

    if (password[first] == policy and password[last] != policy) \
            or (password[first] != policy and password[last] == policy):
        valid_count += 1

print(valid_count)
