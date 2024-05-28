'''def isbalanced(word):
    stack=[]
    for ele in word:
        if ele == '(':
            stack.append(ele)
        else:
            if len(stack)==0:
                return False
            else:
                stack.pop()
    if len(stack)==0:
        return True
    return False
word="()()()()"
result=isbalanced(word)
print(result)'''


def isValid(self, s):
        stack=[]
        openbrackets=['(','[','{']
        for ele in s:
            if ele in openbrackets:
               stack.append(ele)
            else:
                if len(stack)==0:
                   return False
                elif ele==')':
                    if stack[-1]=='(':
                       stack.pop()
                    else:
                       return False
                elif ele==']':
                    if stack[-1]=='[':
                       stack.pop()
                    else:
                       return False
                elif ele=='}':
                    if stack[-1]=='{':
                       stack.pop()
                    else:
                       return False
        if len(stack)==0:
            return True
        return False


