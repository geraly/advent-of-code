import re

INGREDIENT = "ingredient"
ALLERGEN = "allergen"


def get_all_ingredients(list_):
    ret = set()

    for item_ in list_:
        ret |= set(item_[INGREDIENT])

    return ret


def search_non_allergen(list_):
    # アレルゲンごとに候補の成分を探す
    # アレルゲンが記載されているメニューには必ず共通の成分がある
    allergen_candidate = {}

    for item_ in list_:
        for allergen in item_[ALLERGEN]:
            if allergen not in allergen_candidate:
                allergen_candidate[allergen] = set(item_[INGREDIENT])
                continue
            allergen_candidate[allergen] &= set(item_[INGREDIENT])

    candidate = set()
    for ingredients in allergen_candidate.values():
        candidate |= ingredients

    all_ingredients = get_all_ingredients(list_)
    ret = all_ingredients
    for ingredient in candidate:
        ret.remove(ingredient)

    return ret


def count_ingredient(list_, ingredients):
    ret = 0
    for v in list_:
        for ingredient in v[INGREDIENT]:
            if ingredient in ingredients:
                ret += 1

    return ret


def solve(list_):
    ingredients = search_non_allergen(list_)
    ret = count_ingredient(list_, ingredients)

    return ret


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        list_ = []
        for line in f.read().splitlines():
            m = re.match(r"(.+) \(contains (.+)\)", line)
            if m is None:
                print("Format Error")
                quit()
            ingredient = m.group(1).split(' ')
            allergen = m.group(2).split(', ')
            list_.append({INGREDIENT: ingredient, ALLERGEN: allergen})

    print(solve(list_))
