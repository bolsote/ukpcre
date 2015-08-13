from collections import Iterable
from functools import partial


def _transform_factory(meth, item):
    if isinstance(item, Iterable) and not isinstance(item, str):
        return tuple(map(meth, item))
    return meth(item)


class DataGenerator:
    transforms = {
        "lowercase": partial(
            _transform_factory,
            lambda k: k.lower() if k else k
        ),
        "nospace": partial(
            _transform_factory,
            lambda k: k.replace(' ', '') if k else k
        ),
    }

    def __init__(self, dataset):
        self.dataset = dataset

    def _get_transform_combinations(self):
        elems = list(self.transforms)
        N = len(elems)
        fmtstr = "{{:0{}b}}".format(N)

        for k in range(2 ** N):
            bitstr = fmtstr.format(k)
            combination = []
            for bit in range(len(bitstr)):
                if int(bitstr[bit]):
                    combination.append(elems[bit])
            yield combination

    def _transform_data(self, item, *args):
        if args:
            for transform in args:
                item = map(self.transforms[transform], item)

        return tuple(item)

    def generate_data(self):
        for item in self.dataset:
            for transform in self._get_transform_combinations():
                yield self._transform_data(item, *transform)

    def generate_ids(self):
        for item in self.dataset:
            for transform in self._get_transform_combinations():
                yield "{}-{}".format(
                    item[0].replace(" ", "_"),
                    "_".join(transform) or "original"
                )


def pytest_generate_tests(metafunc):
    gen = DataGenerator(metafunc.cls.postcodes)

    metafunc.parametrize(
        'data,postcode,first,second',
        list(gen.generate_data()),
        ids=list(gen.generate_ids()),
        scope='class'
    )
