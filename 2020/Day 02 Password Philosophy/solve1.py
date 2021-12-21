import re

data = []

with open('input.txt', 'r') as f:
    lines = f.readlines()

valid_count = 0

for line in lines:
    m = re.match(r"(\d+)-(\d+) (\w): (\w+)$", line)
    if m is None:
        raise Exception("format error")
    (least, most, policy, password) = m.groups()
    policy_count = password.count(policy)
    if int(least) <= policy_count and policy_count <= int(most):
        valid_count += 1

print(valid_count)
