def orbits(text):
    left,right = [],[]
    for line in text.split():
        items = line.split(')')
        left.append(items[0])
        right.append(items[1])

    d = {}
    for i in range(len(left)):
        if left[i] not in d:
            d[left[i]] = [right[i]]
        else:
            d[left[i]].append(right[i])

    def indirects(key): # to recursively determine indirect orbits by summing indirect orbits of its children
        if key not in d:
            return 0        
        return sum(1+indirects(child) for child in d[key])

    def recursiveIn(target): # recursively finds the entire chain going from target node to the root node
        parents = []
        for item in d:
            if target in d[item]:
                parents.append(item)
                parents += recursiveIn(item)
                return parents
        return []

    toYou = recursiveIn('YOU')
    toSan = recursiveIn('SAN')

    # second part computes hops from YOU to SAN by adding both chains together and tossing the shared part
    return sum(indirects(key) for key in d), (len(toYou) + len(toSan) - 2*len(set(toYou).intersection(toSan)))

if __name__ == "__main__":
    with open('06.in') as f:
        text = f.read()
        
        print(orbits(text))


