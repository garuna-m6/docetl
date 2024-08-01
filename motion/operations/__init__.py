from motion.operations.map import MapOperation, ParallelMapOperation
from motion.operations.filter import FilterOperation
from motion.operations.explode import ExplodeOperation
from motion.operations.equijoin import EquijoinOperation
from motion.operations.split import SplitOperation
from motion.operations.reduce import ReduceOperation
from motion.operations.resolve import ResolveOperation


def get_operation(operation_type: str):
    operations = {
        "map": MapOperation,
        "parallel_map": ParallelMapOperation,
        "filter": FilterOperation,
        "explode": ExplodeOperation,
        "equijoin": EquijoinOperation,
        "split": SplitOperation,
        "reduce": ReduceOperation,
        "resolve": ResolveOperation,
    }
    return operations.get(operation_type)