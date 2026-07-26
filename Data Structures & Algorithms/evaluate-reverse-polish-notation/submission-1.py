class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num=[]
        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                num.append(int(token))
            else:
                right_operand=num.pop()
                left_operand=num.pop()
            # Now you can check which operator it is and perform the math
            if token == "+":
                num.append(left_operand + right_operand)
            elif token == "-":
                num.append(left_operand - right_operand)
            elif token == "*":
                num.append(left_operand * right_operand)
            elif token == "/":
                # Division truncates toward zero in Python using int()
                num.append(int(left_operand / right_operand))
        return num[0]
                