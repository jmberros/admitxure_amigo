import re
import os

import pandas as pd


def read_Q_file(path):
    """
    Read a Q file generated by Admixture into a pandas DF.
    Expects a +path+ that has the K value in it, like `foo.5.Q`.
    """
    q_values = pd.read_table(path, sep='\s+', header=None)
    k = re.search(r'.+\.(\d+)\.Q$', os.path.basename(path)).group(1)
    q_values.columns = ('k{}_cluster_'.format(k) +
                        (q_values.columns + 1).astype(str))
    return q_values
