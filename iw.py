import iterated_width
import MySearchModel
import searchspace
from iterated_width import NoveltyEvaluator, SearchStats
from collections import deque
import logging
def iterated_width_search(task, options, **kwargs):
    """
    :param task: The actual planning task
    :param options: Some width-related options, such as max_width, etc.
    :param kwargs: Might optionally contain e.g. the search model
    :return:
    """
    max_width = int(options.get('max_width', 2))
    model = kwargs.get('model', None)
    if model is None:
        model = SearchModel(task)

    searcher = IteratedWidthSearchAlgorithm(model, NoveltyEvaluator(max_width))
    return searcher.search()


class IteratedWidthSearchAlgorithm(object):
    def __init__(self, model, evaluator):
        self.model = model
        self.max_width = evaluator.max_width
        self.evaluator = evaluator
        self.best_node = None

        # Open and closed lists
        self.open = deque()
        self.closed = set()

        self.stats = SearchStats(self.max_width)

    def search(self):
        self.generate_node(self.model.root)

        while self.open:
            node = self.expand_node()
            if self.best_node is None or self.best_node.state.reward < node.state.reward:
                self.best_node = node

            for child_node in self.model.successor_nodes(node):
                self.generate_node(child_node)

        #logging.info("The task is not solvable with the current max-width ({}).".format(self.max_width))
        self.stats.report()
        return self.best_node.extract_solution()

    def check_goal(self, node):
        if self.model.is_goal(node):
            logging.info("Goal reached. Start extraction of solution.")
            self.stats.report()
            return True
        return False

    def generate_node(self, node):
        features = self.model.get_features(node)
        if features in self.closed:  # duplicate detection
            return

        self.closed.add(features)
        self.stats.generated += 1

        # Novelty evaluation
        novelty = self.evaluator.evaluate(features)
        self.stats.count_novelty(novelty)
        print novelty
        if novelty <= self.max_width:
            self.open.append(node)
        else:
            self.stats.pruned += 1

    def expand_node(self):
        node = self.open.popleft()
        self.stats.expanded += 1
        logging.debug("Expanded: {}".format(node))
        return node

if __name__ == "__main__":
    model = MySearchModel.MySearchModel(searchspace)
    options = {
        'max_width' : 1
    }
    sol = iterated_width_search(None, options, model=model)
    print sol 
    if sol:
        print("Solution found:")
        model.simulate_actions(sol)
    else:
        print("No solution found")
    
    
