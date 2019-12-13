def password(text):
    currLayer = 0
    layers = []
    layer = []
    check = []
    for i,char in enumerate(text):
        layer.append(char)
        if (i+1)%(25*6) == 0:
            check.append(i+1)
            currLayer += 1
            layers.append(layer)
            layer = []

    minSeen = 25*6+1
    minPos = -1
    for i,layer in enumerate(layers):
        x = layer.count('0')
        if x < minSeen:
            minSeen = x
            minPos = i

    minLayer = layers[minPos]
    yield minLayer.count('1') * minLayer.count('2')

    result = layers[0]
    for i,layer in enumerate(layers):
        for j,pixel in enumerate(layer):
            if result[j] == '2':
                result[j] = pixel

    image = [result[i:i+25] for i in range(0, len(result), 25)]

    build = ""
    for row in image:
        build += ''.join(row) + "\n"
    yield build[:-1].replace('2', ' ').replace('0', ' ').replace('1', '▓')
    

if __name__ == "__main__":
    with open('08.in') as f:
        text = f.read()

        pw = password(text)
        print(next(pw), next(pw), sep='\n')
