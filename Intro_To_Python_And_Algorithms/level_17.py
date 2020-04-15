string = ''
cmd_stack = list()
undo_stack = list()
undo_counts = 0


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
    global undo_counts
    global undo_stack

    if undo_counts > 0:
        undo_stack = list()
        cmd_stack = list()
        undo_counts = 0

    cmd_stack.append(string)
    string += chars


def Remove(n):
    global string
    global cmd_stack
    global undo_counts
    global undo_stack

    if undo_counts > 0:
        undo_stack = list()
        cmd_stack = list()
        undo_counts = 0

    cmd_stack.append(string)
    string = string[:-int(n)]


def Print(n):
    global string
    n = int(n)

    if n >= len(string):
        return ''

    return string[n]


def Undo():
    global string
    global cmd_stack
    global undo_stack
    global undo_counts

    if len(cmd_stack) > 0:
        undo_stack.append(string)
        string = cmd_stack[-1]
        del cmd_stack[-1]
        undo_counts += 1


def Redo():
    global string
    global cmd_stack
    global undo_stack

    if len(undo_stack) > 0:
        cmd_stack.append(undo_stack[-1])
        string = undo_stack[-1]
        del undo_stack[-1]
