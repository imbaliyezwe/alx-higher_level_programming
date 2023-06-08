#!/usr/bin/python3


def magic_calculation(g, h):
    """Match bytecode provided by Holberton School."""
    from magic_calculation_102 import add, sub

    if g < h:
        j = add(g, h)
        for i in range(4, 6):
            j = add(j, i)
        return (j)

    else:
        return(sub(g, h))

