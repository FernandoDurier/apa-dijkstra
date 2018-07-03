import os

class graphPathFinder:
    def __init__(self):
        pass
    
    def exploreFolder(self, folderpath):
        files = []
        folders = []
        for (path, dirnames, filenames) in os.walk(folderpath):
            folders.extend(os.path.join(path, name) for name in dirnames)
            files.extend(os.path.join(path, name) for name in filenames)

        return {"files":files,"folders":folders}