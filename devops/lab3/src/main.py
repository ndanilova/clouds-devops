from typing import Tuple

def get_excessive_letter(shorter: str, longer: str) -> str:
    longer_sort = sorted(longer)
    shorter_sort = sorted(shorter)
    for i in range(len(shorter_sort)):
        if shorter_sort[i] != longer_sort[i]:
            return longer_sort[i]
    return longer_sort[len(longer_sort) - 1]
    pass

def read_input() -> Tuple[str, str]:
    shorter = input().strip()
    longer = input().strip()
    return shorter, longer

if __name__ == '__main__':
    shorter, longer = read_input()
    print(get_excessive_letter(shorter, longer))
