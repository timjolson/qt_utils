from qt_utils.colors import colorList, rgb_to_hex, hex_to_rgb, findColor


def test_rgb_vs_hex():
    # check all colors in colorList
    for c in colorList:
        # make sure conversions work
        assert '#'+rgb_to_hex(c.rgb) == c.hex
        assert hex_to_rgb(c.hex) == c.rgb


def test_findColor():
    # check all colors in colorList
    for C in colorList:
        # possible identifiers are all names in C[0], hex string in C[1], and rgb tuple in C[2]
        clist = C.names + list((C.hex, C.rgb))

        # each identifier returns correct color
        for c in clist:
            assert findColor(c) == C

    # check all colors in colorList
    for c in colorList:
        # adjust rgb values slightly to test the search algorithm (which gets closest by rgb tuple_distance)
        assert c == findColor((c.rgb.r+2, c.rgb.g-2, c.rgb.b))
        assert c == findColor((c.rgb.r, c.rgb.g+2, c.rgb.b-2))
        assert c == findColor((c.rgb.r-2, c.rgb.g, c.rgb.b+2))
