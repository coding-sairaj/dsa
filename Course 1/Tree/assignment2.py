class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        
        return level

    def print_tree(self, level):
        currentLevel = self.get_level()
        spaces = ' ' * currentLevel * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if currentLevel == level:
            return
        if(self.children):
            for child in self.children:
                child.print_tree(level)

def build_location_tree():
    root = TreeNode("Global")

    india = TreeNode("India")
    gujarat = TreeNode("Gujarat")
    karnataka = TreeNode("Karnataka")
    ahmedabad = TreeNode("Ahmedabad")
    baroda = TreeNode("Baroda")
    bengaluru = TreeNode("Bengaluru")
    mysore = TreeNode("Mysore")

    USA = TreeNode("USA")
    NewJersey = TreeNode("New Jersey")
    California = TreeNode("California")
    Princeton = TreeNode("Princeton")
    Trenton = TreeNode("Trenton")
    SanFrancisco = TreeNode("San Francisco")
    MountainView = TreeNode("Mountain View")
    PaloAlto = TreeNode("Palo Alto")

    root.add_child(india)
    root.add_child(USA)

    india.add_child(gujarat)
    india.add_child(karnataka)

    gujarat.add_child(ahmedabad)
    gujarat.add_child(baroda)
    karnataka.add_child(bengaluru)
    karnataka.add_child(mysore)

    USA.add_child(NewJersey)
    USA.add_child(California)

    NewJersey.add_child(Princeton)
    NewJersey.add_child(Trenton)

    California.add_child(SanFrancisco)
    California.add_child(MountainView)
    California.add_child(PaloAlto)

    return root

if __name__ == '__main__':
    root = build_location_tree()
    root.print_tree(2)