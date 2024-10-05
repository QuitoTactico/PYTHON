from collections import deque


def balance(s: str) -> str:
    d = deque()
    for i in s:
        if i in ["(", "[", "{"]:
            d.append(i)

        if i is ")":
            if len(d) == 0:
                return "No"
            if d.pop() == "(":
                continue
            return "No"

        if i is "]":
            if len(d) == 0:
                return "No"
            if d.pop() == "[":
                continue
            return "No"

        if i == "}":
            if len(d) == 0:
                return "No"
            if d.pop() == "{":
                continue
            return "No"
    return "Yes" if len(d) == 0 else "No"


print(balance(input()))
