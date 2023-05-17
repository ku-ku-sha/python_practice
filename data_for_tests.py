class InputData:
    delete_a = ['', 'iouhlkjhjkg;ljlkji', 'AAAaaaаааААА', 'jkhlkhl;aaaljlA', '1231465465', 12345]


class ExpectedResult:
    delete_a = [('', 0), ('iouhlkjhjkg;ljlkji', 0), ('', 12), ('jkhlkhl;ljl', 4), ('1231465465', 0), -1]
