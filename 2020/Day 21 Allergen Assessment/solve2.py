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


def determine_allergen(list_):
    allergen_candidate = {}

    for item_ in list_:
        for allergen in item_[ALLERGEN]:
            if allergen not in allergen_candidate:
                allergen_candidate[allergen] = set(item_[INGREDIENT])
                continue
            allergen_candidate[allergen] &= set(item_[INGREDIENT])

    output = {}

    while len(allergen_candidate) > 0:
        found_allergen = None
        found_ingredient = None
        for allergen, ingredients in allergen_candidate.items():
            if len(ingredients) == 1:
                found_ingredient = ingredients.pop()
                found_allergen = allergen
                output[found_allergen] = found_ingredient
                break
        assert found_allergen is not None and found_ingredient is not None
        allergen_candidate.pop(found_allergen)
        for allergen in allergen_candidate.keys():
            if found_ingredient in allergen_candidate[allergen]:
                allergen_candidate[allergen].remove(found_ingredient)

    return output


def show_ingredients(allergen_list):

    output = []
    allergens = list(allergen_list.keys())
    allergens.sort()
    for allergen in allergens:
        output.append(allergen_list[allergen])

    print(','.join(output))


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

    non_allergen = search_non_allergen(list_)
    for item_ in list_:
        for ingredient in non_allergen:
            if ingredient in item_[INGREDIENT]:
                item_[INGREDIENT].remove(ingredient)

    allergen_list = determine_allergen(list_)
    show_ingredients(allergen_list)
