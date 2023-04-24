from collections import defaultdict

class_dict = defaultdict(list)
s = input()

while s:
    if s.find('class') == 0:
        pos1 = s.find(' ')
        pos2 = s.find('(')
        if pos2 == -1:
            class_name = s.split()[1][:-1]
        else:
            pos3 = s.find(')')
            inherited = s[pos2 + 1: pos3].split(', ')
            class_name = s[:pos2].split()[1]
            for c in inherited:
                class_dict[class_name].append(c)
    s = input()

def merge(sequences):
    result = []
    
    while True:
        sequences = [x for x in sequences if x]
        if not sequences:
            return result
        for seq in sequences:
            head = seq[0]
            if not any(head in s[1:] for s in sequences):
                break
        else:
            raise ValueError
        result.append(head)
        for seq in sequences:
            if seq[0] == head:
                del seq[0]



def build_graph(obj, bases_func):
    graph = {}
    _add_to_graph(obj, graph, bases_func)
    return graph

def _add_to_graph(obj, graph, bases_func):
    if obj not in graph:
        graph[obj] = bases_func
        for x in graph[obj]:
            _add_to_graph(x, graph, bases_func)


def class_graph(cls):
    return build_graph(cls, lambda cls: class_dict[cls])
    
    
def linearize(graph, heads=None, order=True):    
    results = {}
    graph = defaultdict(list, graph)
    for head in heads or sorted(graph, key=lambda k: len(graph[k])):
        _linearize(head, graph, order, results)
    return results


def _linearize(head, graph, order, results):
    if head in results:
        return results[head]
    res = merge(
        [[head]] +
        [_linearize(x, graph, order, results) for x in graph[head]] +
        ([graph[head]] if order else [])
    )
    results[head] = res
    return res


try:
    linearize(class_dict)
except ValueError:
    print('No')
else:
    print('Yes')
