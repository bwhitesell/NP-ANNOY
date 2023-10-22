from typing import List


class AnnoyIndex:

    def __init__(self, n_trees: int, n_neighbors: int) -> None:
        self.n_trees = n_trees
        self.n_neighbors = n_neighbors

    def add_point(self, point: List[float]) -> None:
        ...

    def _build_tree(self) -> None:
        ...


