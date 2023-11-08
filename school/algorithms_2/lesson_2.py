from __future__ import annotations

from typing import Any, Optional


class BSTNode:

    def __init__(self, key: int, val: Any, parent: Optional[BSTNode]):
        self.NodeKey = key  # ключ узла
        self.NodeValue = val  # значение в узле
        self.Parent: Optional[BSTNode] = parent  # родитель или None для корня
        self.LeftChild: Optional[BSTNode] = None  # левый потомок
        self.RightChild: Optional[BSTNode] = None  # правый потомок

    def is_leaf(self) -> bool:

        return self.LeftChild is None and self.RightChild is None


class BSTFind:  # промежуточный результат поиска

    def __init__(self):
        self.Node: Optional[BSTNode] = None  # None если
        # в дереве вообще нету узлов

        self.NodeHasKey: bool = False  # True если узел найден
        self.ToLeft: bool = False  # True, если родительскому узлу надо
        # добавить новый узел левым потомком

    @classmethod
    def found(cls, found_node: BSTNode) -> BSTFind:

        find = BSTFind()
        find.Node = found_node
        find.NodeHasKey = True
        return find

    @classmethod
    def not_found_left(cls, parent: BSTNode) -> BSTFind:

        find = cls()
        find.Node = parent
        find.NodeHasKey = False
        find.ToLeft = True
        return find

    @classmethod
    def not_found_right(cls, parent: BSTNode) -> BSTFind:

        find = cls()
        find.Node = parent
        find.NodeHasKey = False
        find.ToLeft = False
        return find


class BST:

    def __init__(self, node: Optional[BSTNode]):
        self.Root = node  # корень дерева, или None

    def FindNodeByKey(self, key: int) -> Optional[BSTFind]:

        if self.Root is None:
            return None

        return self._find_node_by_key(self.Root, key)

    def _find_node_by_key(self, root: BSTNode, key: int) -> BSTFind:

        if key < root.NodeKey and root.LeftChild is None:
            return BSTFind.not_found_left(root)
        if key < root.NodeKey:
            return self._find_node_by_key(root.LeftChild, key)

        if key > root.NodeKey and root.RightChild is None:
            return BSTFind.not_found_right(root)
        if key > root.NodeKey:
            return self._find_node_by_key(root.RightChild, key)

        return BSTFind.found(root)

    def AddKeyValue(self, key: int, val: Any) -> bool:

        if self.Root is None:
            self.Root = BSTNode(key, val, None)
            return True

        find = self.FindNodeByKey(key)

        if find.NodeHasKey:
            return False

        if find.ToLeft:
            find.Node.LeftChild = BSTNode(key, val, find.Node)

        if not find.ToLeft:
            find.Node.RightChild = BSTNode(key, val, find.Node)

        return True

    def FinMinMax(self, FromNode: BSTNode, FindMax: bool) -> Optional[BSTNode]:

        if FromNode.LeftChild is None:
            return FromNode
        return self._find_min_max(FromNode, FindMax)

    def _find_min_max(self, root: BSTNode, is_max: bool) -> BSTNode:

        if is_max and root.RightChild is not None:
            return self._find_min_max(root.RightChild, is_max)
        # if is_max and root.LeftChild is not None:
        #     return self._find_min_max(root.LeftChild, is_max)

        if not is_max and root.LeftChild is not None:
            return self._find_min_max(root.LeftChild, is_max)
        # if not is_max and root.RightChild is not None:
        #     return self._find_min_max(root.RightChild, is_max)

        return root

    def DeleteNodeByKey(self, key: int) -> bool:

        find = self.FindNodeByKey(key)

        if not find.NodeHasKey:
            return False

        if find.Node.is_leaf() and find.Node is self.Root:
            self.Root = None
            return True

        if find.Node.is_leaf() and find.Node.Parent.LeftChild is find.Node:
            find.Node.Parent.LeftChild = None
            return True

        if find.Node.is_leaf() and find.Node.Parent.RightChild is find.Node:
            find.Node.Parent.RightChild = None
            return True

        # if find.Node.LeftChild and find.Node.Parent.LeftChild is find.Node:
        #     find.Node.Parent.LeftChild = find.Node.LeftChild
        #     find.Node.LeftChild.Parent = find.Node.Parent
        #     return True
        #
        # if find.Node.LeftChild and find.Node.Parent.RightChild is find.Node:
        #     find.Node.Parent.RightChild = find.Node.LeftChild
        #     find.Node.LeftChild.Parent = find.Node.Parent
        #     return True
        #
        # if find.Node.RightChild and find.Node.Parent.LeftChild is find.Node:
        #     find.Node.Parent.LeftChild = find.Node.RightChild
        #     find.Node.RightChild.Parent = find.Node.Parent
        #     return True
        #
        # if find.Node.RightChild and find.Node.Parent.RightChild is find.Node:
        #     find.Node.Parent.RightChild = find.Node.RightChild
        #     find.Node.RightChild.Parent = find.Node.Parent
        #     return True

        if find.Node.RightChild:
            most_left_node = self.FinMinMax(find.Node.RightChild, False)

            if most_left_node.is_leaf():
                most_left_node.Parent.LeftChild = None
            else:
                most_left_node.Parent.LeftChild = most_left_node.RightChild
                most_left_node.RightChild.Parent = most_left_node.Parent

            if find.Node is self.Root:
                self.Root = most_left_node
                most_left_node.Parent = None

            if find.Node.Parent and find.Node.Parent.LeftChild is find.Node:
                most_left_node.Parent = find.Node.Parent
                find.Node.Parent.LeftChild = most_left_node

            if find.Node.Parent and find.Node.Parent.RightChild is find.Node:
                most_left_node.Parent = find.Node.Parent
                find.Node.Parent.RightChild = most_left_node

        return True

    def Count(self) -> int:

        return len(self.get_all_nodes())

    def get_all_nodes(self) -> list[BSTNode]:

        if self.Root is None:
            return []

        all_nodes: list[BSTNode] = []
        self._get_all_nodes(self.Root, all_nodes)
        return all_nodes

    def _get_all_nodes(self, root: BSTNode, all_nodes: list[BSTNode]) -> None:

        all_nodes.append(root)

        if root.LeftChild:
            self._get_all_nodes(root.LeftChild, all_nodes)

        if root.RightChild:
            self._get_all_nodes(root.RightChild, all_nodes)

















