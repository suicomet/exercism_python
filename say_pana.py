ONES = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
TEENS = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen'] + [n.strip('t') + 'teen' for n in ONES[-4:]]
TENS = ['twenty', 'thirty', 'forty', 'fifty'] + [n.strip('t') + 'ty' for n in ONES[-4:]]
LT_TWENTY = ['zero'] + ONES + TEENS
MAGNITUDES = ['', 'thousand', 'million', 'billion', 'trillion']


def say_hundreds(i):
    """Step 1

    Handle the basic case of -999 through 999.
    """
    output = []
    base = 10
    ones = i % base
    tens = i % (base ** 2) // base
    hundreds = i % (base ** 3) // (base ** 2)

    if i > 19:
        hyphenated = []
        if hundreds:
            output.append(ONES[hundreds - 1] + ' hundred')
        if tens:
            hyphenated.append(TENS[tens - 2])
        if ones:
            hyphenated.append(ONES[ones - 1])
        if hyphenated:
            output.append('-'.join(hyphenated))
    else:
        output.append(LT_TWENTY[i])

    return output


def break_num(i):
    """Step 2

    Implement breaking a number up into chunks of thousands.
    So 1234567890 should yield a list like 1, 234, 567, and 890, while the far simpler 1000 should yield just 1 and 0.

    Step 3

    Now handle inserting the appropriate scale word between those chunks.
    So 1234567890 should yield '1 billion 234 million 567 thousand 890'
    The program must also report any values that are out of range. It's fine to stop at "trillion".
    """
    s = str(i)[::-1]
    separated = [int(s[i:i+3][::-1]) for i in range(0, len(s), 3)]

    return list(zip(separated, MAGNITUDES[:len(separated)]))[::-1]


def say(i):
    """Step 4

    Put it all together to get nothing but plain English.
    12345 should give twelve thousand three hundred forty-five.
    The program must also report any values that are out of range.
    """
    output = []

    if i < 0:
        output.append('negative')
        i = abs(i)

    if i > 999_999_999_999:
        raise ValueError("input out of range")

    for h, mag in break_num(i):
        output += say_hundreds(h)
        if mag:
            output.append(mag)

    return ' '.join(output)


def main():
    print(say(43674982))


if __name__ == '__main__':
    main()