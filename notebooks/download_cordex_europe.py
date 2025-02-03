#!/usr/bin/env python

import pandas as pd
import papermill

params = pd.read_csv("parameters.csv", delim_whitespace=True)
params = params.where(params.domain == "europe").dropna()

for n in range(len(params)):
    pdict = dict(params.iloc[n])
    try:
        papermill.execute_notebook(
            "download_cordex.ipynb",
            "download_cordex.{domain}_{horizontal_resolution}_{gcm_model}_{rcm_model}.ipynb".format(**pdict),
            parameters=pdict,
        )
    except Exception as e:
        pass