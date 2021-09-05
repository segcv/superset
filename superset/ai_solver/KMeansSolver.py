import pandas as pd
from sklearn.cluster import KMeans
from sklearn import preprocessing
import pickle
from scipy.spatial.distance import cdist
import numpy as np

from superset.utils.MapUtil import get_map_val


class KMeansSolver():
    def train_zhou(self, x, y=None, config={}):
        max_num_clusters = get_map_val(config, 'max_num_clusters', 9)

        idx = np.arange(1, max_num_clusters + 1)
        euclidean = []

        for i in idx:
            classfier = KMeans(n_clusters=i)
            classfier.fit(x)
            loss = np.min(cdist(x, classfier.cluster_centers_, metric='euclidean'), axis=1)
            loss = np.sum(loss) / x.shape[0]
            euclidean.append(loss)

        return idx, euclidean

    def train(self, x, y=None, config={}):
        num_clusters = get_map_val(config, 'num_clusters', 3)

        classfier = KMeans(n_clusters=num_clusters)
        classfier.fit(x)

        loss = np.min(cdist(x, classfier.cluster_centers_, metric='euclidean'), axis=1)
        loss = np.sum(loss) / x.shape[0]

        return loss, classfier

    def test(self, x, y=None, checkpoint=None, config={}):
        num_clusters = get_map_val(config, 'num_clusters', 3)

        if checkpoint is None:
            return None

        # real work
        cls:KMeans = pickle.loads(checkpoint)
        cls.predict(x)
        
        y_pred = cls.labels_
        index = np.arange(0, num_clusters)
        clusters = []
        for i in index:
            idx = np.where(y_pred == (i))
            cluster = x[idx]
            info = np.array([cluster[:, 0], cluster[:, 1]]).transpose()
            clusters.append(info)

        return index, clusters
