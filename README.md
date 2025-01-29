# Climate Attribution Block Course Preparation

## Downloading all data

There's a [notebooks/download_cordex.ipynb](notebooks/download_cordex.ipynb) which can either be adapted (not recommended) or run with Papermill as follows:
```shell
$ papermill download_cordex.ipynb download_cordex.europe_mpi_mpi.ipynb -p gcm_model "mpi_m_mpi_esm_lr" -p rcm_model "mpi_csc_remo2009" -p domain "europe" -p horizontal_resolution "0_11_degree_x_0_11_degree"
$ papermill download_cordex.ipynb download_cordex.africa_mpi_clmcom.ipynb -p gcm_model "mpi_m_mpi_esm_lr" -p rcm_model "clmcom_kit_cclm5_0_15" -p domain "africa" -p horizontal_resolution "0_22_degree_x_0_22_degree"
```
As a result, we'll have a number of randomly named ZIP files in `data/orig/`

## un-chunking netCDF files

The netCDF files available from CDS are compressed (deflated in their own terms) netCDF-4 files with chunks of size `{"time": 1, "lon": "full", "lat": "fulll"}`.
Hence, _any_ read from the file will always have to read full spatial domains. 
For example, if a user requests one single time step for one single location, the netCDF libary will load the whole spatial field for the respective time step, uncompress it, select the requested time step, and forget the rest.
For the Europe domain, this is a `400^2` overhead when users are only interested in time series of single locations.

We'll transform all files to uncompressed files that don't use any chunking.
As the netCDF compression does not do particularly well with real data, the resulting files will be only about 20% larger.
