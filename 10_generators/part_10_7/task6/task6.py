def nonempty_lines(file):
    with open(file, encoding="utf-8") as f:

        cleaned = (line.strip() for line in f)
        clipped = (line if len(line) <= 25 else "..." for line in cleaned)
        yield from (line for line in clipped if line)


if __name__ == "__main__":
    for i in range(1, 6):
        print(f"Test {i}")
        print(*nonempty_lines(f"D:\solutions_python_generation\module10\part_10_7\\task6\\tests\\file{i}.txt"), sep="\n")
        print("-"*70)