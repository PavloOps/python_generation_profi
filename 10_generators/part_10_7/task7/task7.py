def txt_to_dict():
    with open(
            r"D:\solutions_python_generation\module10\part_10_7\task7\planets.txt",
            encoding="utf-8") as file:

        planet = dict()
        for line in (x.strip() for x in file):
            if not line:
                yield planet
                planet = dict()
            else:
                key, value = line.split(" = ")
                planet[key] = value
        if planet:
            yield planet

if __name__ == "__main__":
    gen = txt_to_dict()
    for _ in range(9):
        print(next(gen))
    lst = [1, 2, 3]
    print(type(lst))
    print(type(reversed(lst)))