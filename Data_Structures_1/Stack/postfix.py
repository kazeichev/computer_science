from stack import Stack


def postfix(string):
    stack_1 = Stack()
    stack_2 = Stack()
    operands = ['+', '*', '=']

    for i in reversed(string.split(" ")):
        stack_1.push(i)

    while stack_1.size() > 0:
        st1_element = stack_1.pop()

        if st1_element in operands:
            if st1_element == '=':
                return stack_2.pop()

            st2_first_element = stack_2.pop()
            st2_second_element = stack_2.pop()
            tmp_result = ''

            if st1_element == '+':
                tmp_result = int(st2_first_element) + int(st2_second_element)
            elif st1_element == '*':
                tmp_result = int(st2_first_element) * int(st2_second_element)

            stack_2.push(tmp_result)
        else:
            stack_2.push(st1_element)
