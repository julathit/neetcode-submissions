class Solution:
    def isValid(self, s: str) -> bool:
        sre = []

        for cha in s:
            if cha in ['[', '(', '{']:
                sre.append(cha)

            else:
                if not sre:
                    return False

                top = sre.pop()

                if cha == ')' and top != '(':
                    return False
                elif cha == ']' and top != '[':
                    return False
                elif cha == '}' and top != '{':
                    return False

        return len(sre) == 0