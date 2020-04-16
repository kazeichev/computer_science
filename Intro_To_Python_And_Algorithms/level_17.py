string = ''
cmd_stack = list()
index = -1
undo_count = 0


def BastShoe(command):
    global string

    if command[0] == '1':
        Add(command[2:])

    if command[0] == '2':
        Remove(command[2:])

    if command[0] == '3':
        return Print(command[2:])

    if command[0] == '4':
        Undo()

    if command[0] == '5':
        Redo()

    return string


def Add(chars):
    global string
    global cmd_stack
    global undo_count
    global index

    if undo_count > 0:
        cmd_stack = [string]
        undo_count = 0
        index = 0

    string += chars
    cmd_stack.append(string)
    index += 1


def Remove(n):
    global string
    global cmd_stack
    global undo_count
    global index

    if undo_count > 0:
        cmd_stack = [string]
        undo_count = 0
        index = 0

    string = string[:-int(n)]
    cmd_stack.append(string)
    index += 1


def Print(n):
    global string
    n = int(n)

    if n >= len(string):
        return ''

    return string[n]


def Undo():
    global string
    global cmd_stack
    global undo_count
    global index

    index -= 1

    if index < 0:
        index = 0

    string = cmd_stack[index]
    undo_count += 1


def Redo():
    global string
    global cmd_stack
    global undo_count
    global index

    index += 1

    if index >= len(cmd_stack):
        index = len(cmd_stack) - 1

    string = cmd_stack[index]

