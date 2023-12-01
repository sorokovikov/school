from __future__ import annotations

from typing import Any, Optional


class SimpleTreeNode:

    level: Optional[int]

    def __init__(self, val: Any, parent: Optional[SimpleTreeNode]):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children: list[SimpleTreeNode] = []  # список дочерних узлов
        self.level = parent.level + 1 if (parent and parent.level) else 0

    def add_child(self, child: SimpleTreeNode) -> None:

        self.Children.append(child)
        child.Parent = self
        child.level = self.level + 1


class SimpleTree:

    def __init__(self, root: Optional[SimpleTreeNode]):
        self.Root = root  # корень, может быть None

    def AddChild(self, ParentNode: SimpleTreeNode, NewChild: SimpleTreeNode) -> None:

        ParentNode.add_child(NewChild)

    def DeleteNode(self, NodeToDelete: SimpleTreeNode) -> None:

        NodeToDelete.Parent.Children.remove(NodeToDelete)

    def GetAllNodes(self) -> list[SimpleTreeNode]:

        if self.Root is None:
            return []

        all_nodes = []
        self._get_all_nodes(self.Root, all_nodes)
        return all_nodes

    def _get_all_nodes(self, root: SimpleTreeNode, all_nodes: list[SimpleTreeNode]):

        all_nodes.append(root)

        for child in root.Children:
            self._get_all_nodes(child, all_nodes)

    def FindNodesByValue(self, val: Any) -> list[SimpleTreeNode]:

        if self.Root is None:
            return []

        found_nodes = []
        self._find_nodes_by_value(self.Root, val, found_nodes)
        return found_nodes

    def _find_nodes_by_value(self, root: SimpleTreeNode, val: Any, found_nodes: list[SimpleTreeNode]) -> None:

        if root.NodeValue == val:
            found_nodes.append(root)

        for child in root.Children:
            self._find_nodes_by_value(child, val, found_nodes)

    def MoveNode(self, OriginalNode: SimpleTreeNode, NewParent: SimpleTreeNode) -> None:

        OriginalNode.Parent.Children.remove(OriginalNode)
        self.AddChild(NewParent, OriginalNode)

    def Count(self) -> int:

        return len(self.GetAllNodes())

    def _count(self, root: SimpleTreeNode, count: int) -> None:

        count += 1

        for child in root.Children:
            self._count(child, count)

    def LeafCount(self) -> int:

        if self.Root is None:
            return 0

        leaf_nodes = []
        self._leaf_count(self.Root, leaf_nodes)
        return len(leaf_nodes)

    def _leaf_count(self, root: SimpleTreeNode, leaf_nodes: list[SimpleTreeNode]) -> None:

        if len(root.Children) == 0:
            leaf_nodes.append(root)
            return

        for child in root.Children:
            self._leaf_count(child, leaf_nodes)

    def set_levels(self):

        if self.Root is None:
            return

        self._set_level(self.Root, 0)

    def _set_level(self, root: SimpleTreeNode, level: int) -> None:

        root.level = level

        for child in root.Children:
            self._set_level(child, level + 1)

    def EvenTrees(self) -> list[SimpleTreeNode]:

        if self.Root is None:
            return []

        node_pairs: list[SimpleTreeNode] = []
        self._even_trees(self.Root, node_pairs)
        return node_pairs

    def _even_trees(self, root: SimpleTreeNode, node_pairs: list[SimpleTreeNode]) -> None:

        for child in root.Children:
            if SimpleTree(child).Count() % 2 == 0:
                node_pairs.append(root)
                node_pairs.append(child)
            self._even_trees(child, node_pairs)


