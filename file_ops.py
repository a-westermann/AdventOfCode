def read_input(puzzle: int) -> list[str]:
    lines = open(f'{puzzle}').readlines()
    return [line.strip('\n') for line in lines]
