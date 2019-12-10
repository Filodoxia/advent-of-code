class Image:
    def __init__(self, data:str, width:int, height:int):
        self.imgData = [int(i) for i in data]
        self.height = height
        self.width = width

    def layers(self):
        layerLength = self.width * self.height
        numberOfLayers = int(len(self.imgData) / layerLength)
        layers = []

        for layerNo in range(1, numberOfLayers + 1):
            layerStart = layerLength * (layerNo - 1)
            layerEnd = layerLength * layerNo
            layers.append(self.imgData[layerStart:layerEnd])

        return layers

    def layer(self, layerNo:int):
        layerLength = self.width * self.height
        layerStart = layerLength * (layerNo - 1)
        layerEnd = layerLength * layerNo
        return self.imgData[layerStart:layerEnd]