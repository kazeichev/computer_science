def LineAnalysis(line):
    is_correct = False

    if len(line) == 1:
        if line == '*':
            is_correct = True

        return is_correct

    line_template = line.split("*")[1]

    for part in (line if line_template == '' else line.split(line_template)):
        if part != '*':
            is_correct = False
            return is_correct
        else:
            is_correct = True

    return is_correct
