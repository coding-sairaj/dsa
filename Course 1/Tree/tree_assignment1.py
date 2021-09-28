class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
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

    def print_tree(self, type):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + (self.name if type=="name" else (self.designation if type == "designation" else self.name + " (" + self.designation + ")")))
        if(self.children):
            for child in self.children:
                child.print_tree(type)

def build_management_hierarchy():
    CEO = TreeNode("Nilupul", "CEO")

    CTO = TreeNode("Chinmay","CTO")
    InfraHead = TreeNode("Vishwa","Infrastructure Head")
    CloudManager = TreeNode("Dhaval","Cloud Manager")
    AppManager = TreeNode("Abhijit","App Manager")
    AppHead = TreeNode("Aamir","Application Head")
    HRHead = TreeNode("Gels","HR Head")
    RecManager = TreeNode("Peter","Recruitment Manager")
    PolicyManager = TreeNode("Waqas","Policy Manager")

    CEO.add_child(CTO)
    CEO.add_child(HRHead)

    CTO.add_child(InfraHead)
    CTO.add_child(AppHead)

    HRHead.add_child(RecManager)
    HRHead.add_child(PolicyManager)

    InfraHead.add_child(CloudManager)
    InfraHead.add_child(AppManager)

    return CEO

if __name__ == '__main__':
    root = build_management_hierarchy()
    root.print_tree("both")

