from abc import ABC, abstractmethod


class FileSystemItem(ABC):
    @abstractmethod
    def display(self, indent=0):
        pass


class File(FileSystemItem):
    def __init__(self, name):
        self.name = name

    def display(self, indent=0):
        print("  " * indent + f"- File: {self.name}")


class Folder(FileSystemItem):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, item: FileSystemItem):
        self.children.append(item)

    def remove(self, item: FileSystemItem):
        self.children.remove(item)

    def display(self, indent=0):
        print("  " * indent + f"+ Folder: {self.name}")
        for child in self.children:
            child.display(indent + 1)


if __name__ == "__main__":
    # Create files
    file1 = File("document.txt")
    file2 = File("photo.jpg")
    file3 = File("data.csv")

    folder1 = Folder("Documents")
    folder2 = Folder("Pictures")
    root = Folder("Root")

    folder1.add(file1)
    folder2.add(file2)

    subfolder = Folder("Backup")
    subfolder.add(file3)

    root.add(folder1)
    root.add(folder2)
    root.add(subfolder)

    root.display()
