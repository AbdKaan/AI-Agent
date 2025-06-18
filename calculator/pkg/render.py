# render.py


def render(expression, result):
    blue = "\033[94m"
    green = "\033[92m"
    reset = "\033[0m"

    if isinstance(result, float) and result.is_integer():
        result_str = str(int(result))
    else:
        result_str = str(result)

    box_width = max(len(expression), len(result_str)) + 4

    box = []
    box.append("+" + "-" * box_width + "+")
    box.append(
        "|"
        + " " * 2
        + blue
        + expression
        + reset
        + " " * (box_width - len(expression) - 2)
        + "|"
    )
    box.append("|" + " " * box_width + "|")
    box.append("|" + " " * 2 + "=" + " " * (box_width - 3) + "|")
    box.append("|" + " " * box_width + "|")
    box.append(
        "|"
        + " " * 2
        + green
        + result_str
        + reset
        + " " * (box_width - len(result_str) - 2)
        + "|"
    )
    box.append("+" + "-" * box_width + "+")
    return "\n".join(box)

