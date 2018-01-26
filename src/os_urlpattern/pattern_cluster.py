class PatternCluster(object):
    def __init__(self, config, meta_info):
        self._config = config
        self._meta_info = meta_info

    def add_node(self, node):
        pass

    def cluster(self):
        pass


class PiecePatternCluster(PatternCluster):
    pass


class LengthPatternCluster(PatternCluster):
    pass


class BasePatternCluster(PatternCluster):
    pass


class MixedPatternCluster(PatternCluster):
    pass


class LastDotSplitFuzzyPatternCluster(PatternCluster):
    pass


class FuzzyPatternCluster(PatternCluster):
    pass


class MetaInfo(object):
    def __init__(self, url_meta, current_level):
        self._url_meta = url_meta
        self._current_level = current_level

    @property
    def current_level(self):
        return self._current_level

    @property
    def url_meta(self):
        return self._url_meta

    def is_last_level(self):
        return self.url_meta.depth == self._current_level

    def is_last_path_level(self):
        return self.url_meta.path_depth == self._current_level

    def next_level_meta_info(self):
        return MetaInfo(self.url_meta, self._current_level + 1)


class ClusterProcessor(object):
    def __init__(self, config, meta_info):
        self._config = config
        self._min_combine_num = self._config.getint('make', 'min_combine_num')
        self._meta_info = meta_info

    def add_node(self, node):
        pass

    def process(self):
        pass


def cluster(config, url_meta, piece_pattern_tree):
    meta_info = MetaInfo(url_meta, 0)
    processor = ClusterProcessor(config, meta_info)
    processor.add_node(piece_pattern_tree.root)
    processor.process()
