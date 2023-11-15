class Tree:
    def __init__(self, name=''):
        self.name = name
        self.children = {}

    def insert(self, path):
        node = self
        for part in path:
            if part not in node.children:
                node.children[part] = Tree(part)
            node = node.children[part]

    def to_dict(self):
        return {self.name: {child: self.children[child].to_dict() for child in self.children}} if self.children else self.name