"""
Color utilities.
Convert hex <-> rgb.
Find a color name, hex, or rgb from any of these.

Functions:
    tuple_distance(x, y) - x: (int, int, int) -- y: (int, int, int)
    hex_to_rgb(hex) - hex: string, e.g. '#F0F0F0' or '0xf0f0f0'
    rgb_to_hex(rg) - rgb: (int, int, int)
    findColor(color) - color: hex string, color name string, or rgb (int, int, int)

Lists:
    colorList[
        (
            ['color name1', 'color name2', ...],
            'hex color string',
            (red, blue, green)
        ),
        ...
        ]

        eg.
        (['darkgray', 'darkgrey'], '#A9A9A9', (169, 169, 169))

"""


def tuple_distance(x, y):
    """Calculate tuple_distance between tuple values.

    :param x: (int, int, int), rgb tuple
    :param y: (int, int, int), rgb tuple
    :return: float, sum of distances between each pair of elements
    """
    from math import sqrt

    assert len(x)==len(y)
    sum = 0
    for i in range(len(x)):
        sum += (x[i]-y[i])**2
    sum = sqrt(sum)
    return sum

from collections import namedtuple
rgb = namedtuple('RGB', 'r g b')
C = namedtuple('ColorItem', 'names hex rgb')

colorList = \
[C(['aliceblue'], '#F0F8FF', rgb(240, 248, 255)),
 C(['antiquewhite'], '#FAEBD7', rgb(250, 235, 215)),
 C(['aqua', 'cyan'], '#00FFFF', rgb(0, 255, 255)),
 C(['aquamarine'], '#7FFFD4', rgb(127, 255, 212)),
 C(['azure'], '#F0FFFF', rgb(240, 255, 255)),
 C(['beige'], '#F5F5DC', rgb(245, 245, 220)),
 C(['bisque'], '#FFE4C4', rgb(255, 228, 196)),
 C(['black'], '#000000', rgb(0, 0, 0)),
 C(['blanchedalmond'], '#FFEBCD', rgb(255, 235, 205)),
 C(['blue'], '#0000FF', rgb(0, 0, 255)),
 C(['blueviolet'], '#8A2BE2', rgb(138, 43, 226)),
 C(['brown'], '#A52A2A', rgb(165, 42, 42)),
 C(['burlywood'], '#DEB887', rgb(222, 184, 135)),
 C(['cadetblue'], '#5F9EA0', rgb(95, 158, 160)),
 C(['chartreuse'], '#7FFF00', rgb(127, 255, 0)),
 C(['chocolate'], '#D2691E', rgb(210, 105, 30)),
 C(['coral'], '#FF7F50', rgb(255, 127, 80)),
 C(['cornflowerblue'], '#6495ED', rgb(100, 149, 237)),
 C(['cornsilk'], '#FFF8DC', rgb(255, 248, 220)),
 C(['crimson'], '#DC143C', rgb(220, 20, 60)),
 C(['darkblue'], '#00008B', rgb(0, 0, 139)),
 C(['darkcyan'], '#008B8B', rgb(0, 139, 139)),
 C(['darkgoldenrod'], '#B8860B', rgb(184, 134, 11)),
 C(['darkgray', 'darkgrey'], '#A9A9A9', rgb(169, 169, 169)),
 C(['darkgreen'], '#006400', rgb(0, 100, 0)),
 C(['darkkhaki'], '#BDB76B', rgb(189, 183, 107)),
 C(['darkmagenta'], '#8B008B', rgb(139, 0, 139)),
 C(['darkolivegreen'], '#556B2F', rgb(85, 107, 47)),
 C(['darkorange'], '#FF8C00', rgb(255, 140, 0)),
 C(['darkorchid'], '#9932CC', rgb(153, 50, 204)),
 C(['darkred'], '#8B0000', rgb(139, 0, 0)),
 C(['darksalmon'], '#E9967A', rgb(233, 150, 122)),
 C(['darkseagreen'], '#8FBC8F', rgb(143, 188, 143)),
 C(['darkslateblue'], '#483D8B', rgb(72, 61, 139)),
 C(['darkslategray', 'darkslategrey'], '#2F4F4F', rgb(47, 79, 79)),
 C(['darkturquoise'], '#00CED1', rgb(0, 206, 209)),
 C(['darkviolet'], '#9400D3', rgb(148, 0, 211)),
 C(['deeppink'], '#FF1493', rgb(255, 20, 147)),
 C(['deepskyblue'], '#00BFFF', rgb(0, 191, 255)),
 C(['dimgray', 'dimgrey'], '#696969', rgb(105, 105, 105)),
 C(['dodgerblue'], '#1E90FF', rgb(30, 144, 255)),
 C(['firebrick'], '#B22222', rgb(178, 34, 34)),
 C(['floralwhite'], '#FFFAF0', rgb(255, 250, 240)),
 C(['forestgreen'], '#228B22', rgb(34, 139, 34)),
 C(['gainsboro'], '#DCDCDC', rgb(220, 220, 220)),
 C(['ghostwhite'], '#F8F8FF', rgb(248, 248, 255)),
 C(['gold'], '#FFD700', rgb(255, 215, 0)),
 C(['goldenrod'], '#DAA520', rgb(218, 165, 32)),
 C(['gray', 'grey'], '#808080', rgb(128, 128, 128)),
 C(['green'], '#008000', rgb(0, 128, 0)),
 C(['greenyellow'], '#ADFF2F', rgb(173, 255, 47)),
 C(['honeydew'], '#F0FFF0', rgb(240, 255, 240)),
 C(['hotpink'], '#FF69B4', rgb(255, 105, 180)),
 C(['indianred'], '#CD5C5C', rgb(205, 92, 92)),
 C(['indigo'], '#4B0082', rgb(75, 0, 130)),
 C(['ivory'], '#FFFFF0', rgb(255, 255, 240)),
 C(['khaki'], '#F0E68C', rgb(240, 230, 140)),
 C(['lavender'], '#E6E6FA', rgb(230, 230, 250)),
 C(['lavenderblush'], '#FFF0F5', rgb(255, 240, 245)),
 C(['lawngreen'], '#7CFC00', rgb(124, 252, 0)),
 C(['lemonchiffon'], '#FFFACD', rgb(255, 250, 205)),
 C(['lightblue'], '#ADD8E6', rgb(173, 216, 230)),
 C(['lightcoral'], '#F08080', rgb(240, 128, 128)),
 C(['lightcyan'], '#E0FFFF', rgb(224, 255, 255)),
 C(['lightgoldenrodyellow'], '#FAFAD2', rgb(250, 250, 210)),
 C(['lightgray', 'lightgrey'], '#D3D3D3', rgb(211, 211, 211)),
 C(['lightgreen'], '#90EE90', rgb(144, 238, 144)),
 C(['lightpink'], '#FFB6C1', rgb(255, 182, 193)),
 C(['lightsalmon'], '#FFA07A', rgb(255, 160, 122)),
 C(['lightseagreen'], '#20B2AA', rgb(32, 178, 170)),
 C(['lightskyblue'], '#87CEFA', rgb(135, 206, 250)),
 C(['lightslategray', 'lightslategrey'], '#778899', rgb(119, 136, 153)),
 C(['lightsteelblue'], '#B0C4DE', rgb(176, 196, 222)),
 C(['lightyellow'], '#FFFFE0', rgb(255, 255, 224)),
 C(['lime'], '#00FF00', rgb(0, 255, 0)),
 C(['limegreen'], '#32CD32', rgb(50, 205, 50)),
 C(['linen'], '#FAF0E6', rgb(250, 240, 230)),
 C(['magenta', 'fuchsia'], '#FF00FF', rgb(255, 0, 255)),
 C(['maroon'], '#800000', rgb(128, 0, 0)),
 C(['mediumaquamarine'], '#66CDAA', rgb(102, 205, 170)),
 C(['mediumblue'], '#0000CD', rgb(0, 0, 205)),
 C(['mediumorchid'], '#BA55D3', rgb(186, 85, 211)),
 C(['mediumpurple'], '#9370DB', rgb(147, 112, 219)),
 C(['mediumseagreen'], '#3CB371', rgb(60, 179, 113)),
 C(['mediumslateblue'], '#7B68EE', rgb(123, 104, 238)),
 C(['mediumspringgreen'], '#00FA9A', rgb(0, 250, 154)),
 C(['mediumturquoise'], '#48D1CC', rgb(72, 209, 204)),
 C(['mediumvioletred'], '#C71585', rgb(199, 21, 133)),
 C(['midnightblue'], '#191970', rgb(25, 25, 112)),
 C(['mintcream'], '#F5FFFA', rgb(245, 255, 250)),
 C(['mistyrose'], '#FFE4E1', rgb(255, 228, 225)),
 C(['moccasin'], '#FFE4B5', rgb(255, 228, 181)),
 C(['navajowhite'], '#FFDEAD', rgb(255, 222, 173)),
 C(['navy'], '#000080', rgb(0, 0, 128)),
 C(['oldlace'], '#FDF5E6', rgb(253, 245, 230)),
 C(['olive'], '#808000', rgb(128, 128, 0)),
 C(['olivedrab'], '#6B8E23', rgb(107, 142, 35)),
 C(['orange'], '#FFA500', rgb(255, 165, 0)),
 C(['orangered'], '#FF4500', rgb(255, 69, 0)),
 C(['orchid'], '#DA70D6', rgb(218, 112, 214)),
 C(['palegoldenrod'], '#EEE8AA', rgb(238, 232, 170)),
 C(['palegreen'], '#98FB98', rgb(152, 251, 152)),
 C(['paleturquoise'], '#AFEEEE', rgb(175, 238, 238)),
 C(['palevioletred'], '#DB7093', rgb(219, 112, 147)),
 C(['papayawhip'], '#FFEFD5', rgb(255, 239, 213)),
 C(['peachpuff'], '#FFDAB9', rgb(255, 218, 185)),
 C(['peru'], '#CD853F', rgb(205, 133, 63)),
 C(['pink'], '#FFC0CB', rgb(255, 192, 203)),
 C(['plum'], '#DDA0DD', rgb(221, 160, 221)),
 C(['powderblue'], '#B0E0E6', rgb(176, 224, 230)),
 C(['purple'], '#800080', rgb(128, 0, 128)),
 C(['red'], '#FF0000', rgb(255, 0, 0)),
 C(['rosybrown'], '#BC8F8F', rgb(188, 143, 143)),
 C(['royalblue'], '#4169E1', rgb(65, 105, 225)),
 C(['saddlebrown'], '#8B4513', rgb(139, 69, 19)),
 C(['salmon'], '#FA8072', rgb(250, 128, 114)),
 C(['sandybrown'], '#F4A460', rgb(244, 164, 96)),
 C(['seagreen'], '#2E8B57', rgb(46, 139, 87)),
 C(['seashell'], '#FFF5EE', rgb(255, 245, 238)),
 C(['sienna'], '#A0522D', rgb(160, 82, 45)),
 C(['silver'], '#C0C0C0', rgb(192, 192, 192)),
 C(['skyblue'], '#87CEEB', rgb(135, 206, 235)),
 C(['slateblue'], '#6A5ACD', rgb(106, 90, 205)),
 C(['slategray', 'slategrey'], '#708090', rgb(112, 128, 144)),
 C(['snow'], '#FFFAFA', rgb(255, 250, 250)),
 C(['springgreen'], '#00FF7F', rgb(0, 255, 127)),
 C(['steelblue'], '#4682B4', rgb(70, 130, 180)),
 C(['tan'], '#D2B48C', rgb(210, 180, 140)),
 C(['teal'], '#008080', rgb(0, 128, 128)),
 C(['thistle'], '#D8BFD8', rgb(216, 191, 216)),
 C(['tomato'], '#FF6347', rgb(255, 99, 71)),
 C(['turquoise'], '#40E0D0', rgb(64, 224, 208)),
 C(['violet'], '#EE82EE', rgb(238, 130, 238)),
 C(['wheat'], '#F5DEB3', rgb(245, 222, 179)),
 C(['white'], '#FFFFFF', rgb(255, 255, 255)),
 C(['whitesmoke'], '#F5F5F5', rgb(245, 245, 245)),
 C(['yellow'], '#FFFF00', rgb(255, 255, 0)),
 C(['yellowgreen'], '#9ACD32', rgb(154, 205, 50)),
 C(['disabled-gray', 'disabled-grey'], '#F0F0F0', rgb(240, 240, 240))
 ]


def hex_to_rgb(hex):
    """Convert a hex string to rgb tuple.

    :param hex: string, e.g. '#F0F0F0' or '0xf0f0f0'
    :return: (r, g, b)
    """
    hex = hex.split('#')[-1].split('0x')[-1]
    r = int(hex[:2], 16)
    g = int(hex[2:4], 16)
    b = int(hex[4:6], 16)
    return r, g, b


def rgb_to_hex(rgb):
    """Convert an rgb tuple to a hex string.

    :param rgb: (int, int, int), rgb tuple
    :return: string, hex color string, e.g. 'F0F0F0'
    """
    r, g, b = rgb[0], rgb[1], rgb[2]
    r, g, b = hex(r), hex(g), hex(b)
    r, g, b = r.split('0x')[-1].upper(), g.split('0x')[-1].upper(), b.split('0x')[-1].upper()
    if len(r) == 1:
        r = '0' + r
    if len(g) == 1:
        g = '0' + g
    if len(b) == 1:
        b = '0' + b
    return r+g+b


def findColor(color):
    """Finds a color in colorList by name, rgb, or hex string.
    If a name string is passed, it must match exactly.
    If rgb (int, int, int) tuple is passed, if no exact match, returns closest color
        by tuple_distance between values.
    If hex string passed, if no exact match, converts to rgb and runs with that tuple.

    :param color: hex string, color name string, or rgb (int, int, int)
    :return: ( [possible color name strings], hex string, (r,g,b) )
    """
    if isinstance(color, str) and (color.startswith('#') or color.startswith('0x')):
        for c in colorList:
            if c.hex == color:
                return c
        return findColor(hex_to_rgb(color))
    if isinstance(color, str):
        for c in colorList:
            for n in c.names:
                if n.upper() == color.upper():
                    return c
        return None
    if isinstance(color, tuple) and len(color) == 3 and all([isinstance(c, int) for c in color]):
        _min = 1.1e16
        _min_c = ''
        for c in colorList:
            if c.rgb == color:
                return c
        for c in colorList:
            d = tuple_distance(color, c.rgb)
            if d < _min:
                _min = d
                _min_c = c
        return _min_c if _min_c else None
    raise TypeError("color: {} is not the correct format for query".format(color))


__all__ = ['colorList', 'hex_to_rgb', 'rgb_to_hex', 'findColor', 'tuple_distance']
