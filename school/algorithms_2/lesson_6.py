from typing import Optional


class BSTNode:

    def __init__(self, key: int, parent: Optional["BSTNode"]):
        self.NodeKey: int = key  # ключ узла
        self.Parent: Optional[BSTNode] = parent  # родитель или None для корня
        self.LeftChild: Optional[BSTNode] = None  # левый потомок
        self.RightChild: Optional[BSTNode] = None  # правый потомок
        self.Level: int = 0  # уровень узла

    def __get_child_max_level(self, child: "BSTNode") -> int:

        left_level = child.Level
        right_level = child.Level
        if child.LeftChild:
            left_level = self.__get_child_max_level(child.LeftChild)
        if child.RightChild:
            right_level = self.__get_child_max_level(child.RightChild)
        return left_level if left_level > right_level else right_level

    def get_right_max_level(self) -> int:

        if self.RightChild is None:
            return self.Level
        return self.__get_child_max_level(self.RightChild)

    def get_left_max_level(self) -> int:

        if self.LeftChild is None:
            return self.Level
        return self.__get_child_max_level(self.LeftChild)


class BalancedBST:

    def __init__(self):
        self.Root: Optional[BSTNode] = None  # корень дерева

    def GenerateTree(self, a: list[int]) -> None:

        a.sort()
        self.Root = self._fill_tree(a, None, 0)

    def _fill_tree(self, source_list: list[int], parent: Optional[BSTNode], level: int) -> Optional[BSTNode]:

        if len(source_list) == 0:
            return None

        middle_index = self._get_middle_index(source_list)

        new_node = BSTNode(source_list[middle_index], parent)
        new_node.Level = level
        new_node.LeftChild = self._fill_tree(source_list[:middle_index], new_node, level + 1)
        new_node.RightChild = self._fill_tree(source_list[middle_index + 1:], new_node, level + 1)

        return new_node

    def _get_middle_index(self, source_list) -> int:

        middle_index = len(source_list) // 2

        while middle_index != 0 and source_list[middle_index - 1] == source_list[middle_index]:
            middle_index -= 1

        return middle_index

    def IsBalanced(self, root_node: BSTNode) -> bool:

        if root_node is None:
            return True

        if not self.IsBalanced(root_node.LeftChild) or not self.IsBalanced(root_node.RightChild):
            return False

        level_diff = root_node.get_left_max_level() - root_node.get_right_max_level()
        if level_diff > 1 or level_diff < -1:
            return False
        return True

    def get_all_nodes(self) -> list[BSTNode]:

        all_nodes: list[BSTNode] = []
        self._add_node(self.Root, all_nodes)
        return all_nodes

    def _add_node(self, root: Optional[BSTNode], all_nodes: list[BSTNode]) -> None:

        if root is None:
            return

        all_nodes.append(root)

        self._add_node(root.LeftChild, all_nodes)
        self._add_node(root.RightChild, all_nodes)
