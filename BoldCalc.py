import re
bad1 = re.compile(r"\w+\(")
bad2 = re.compile(r"\)\w+")
allowed = set(r"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzабвг()+-*/%_")

class Assignment_error(Exception): pass
class Syntax_error(Exception): pass

global_dict = dict()

s = input()
while s:
    try:
        s = "".join(s.split())
        if s[0] != '#':
            content = s.split("=")
            if len(content) > 2:
                raise Syntax_error
            elif len(content) == 2:
                if not str.isidentifier(content[0]):
                    raise Assignment_error
                if "**" in content[1]:
                    raise Syntax_error                  
                for elem in content[1]:
                    if elem not in allowed:
                        raise Syntax_error
                if re.match(bad1, content[1]) or re.match(bad2, content[1]):
                    raise Syntax_error
                res_str0 = []
                for elem in content[0]:
                    if "A" <= elem.upper() <= 'Z':
                        res_str0 += ['г', elem]
                    else:
                        res_str0 += [elem]
                res_str0 = ''.join(res_str0)
                
                res_str1 = []
                for elem in content[1]:
                    if "A" <= elem.upper() <= 'Z':
                        res_str1 += ['г', elem]
                    else:
                        res_str1 += [elem]
                res_str1 = ''.join(res_str1)  
                res_str1 = res_str1.replace("/", "//")
                res = eval(res_str1, global_dict) 
                global_dict[res_str0] = res
            else:
                if "**" in content[0]:
                    raise Syntax_error
                for elem in content[0]:
                    if elem not in allowed:
                        raise Syntax_error
                if re.match(bad1, content[0]) or re.match(bad2, content[0]):
                    raise Syntax_error
                res_str = []
                for elem in content[0]:
                    if "A" <= elem.upper() <= 'Z':
                        res_str += ['г', elem]
                    else:
                        res_str += [elem]
                res_str = ''.join(res_str)
                res_str = res_str.replace("/", "//")
                print(eval(res_str, global_dict))
            
    except Syntax_error:
        print("Syntax error")
    except SyntaxError:
        print("Syntax error")
    except Assignment_error:
        print("Assignment error")
    except NameError:
        print("Name error")
    except Exception:
        print("Runtime error") 
    s = input()
