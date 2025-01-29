# Climate Attribution Block Course Preparation

## Downloading all data

There's a [notebooks/download_cordex.ipynb](notebooks/download_cordex.ipynb) which can either be adapted (not recommended) or run with Papermill as follows:
```shell
$ papermill download_cordex.ipynb download_cordex.europe_mpi_mpi.ipynb -p gcm_model "mpi_m_mpi_esm_lr" -p rcm_model "mpi_csc_remo2009" -p domain "europe" -p horizontal_resolution "0_11_degree_x_0_11_degree"
$ papermill download_cordex.ipynb download_cordex.africa_mpi_clmcom.ipynb -p gcm_model "mpi_m_mpi_esm_lr" -p rcm_model "clmcom_kit_cclm5_0_15" -p domain "africa" -p horizontal_resolution "0_22_degree_x_0_22_degree"
```
As a result, we'll have a number of randomly named ZIP files in `data/orig/`

## Rechunking 

TBD