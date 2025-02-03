# Climate Attribution Block Course Preparation

## Downloading all data

There's a [notebooks/download_cordex.ipynb](notebooks/download_cordex.ipynb) which can either be adapted (not recommended) or run with Papermill as follows:
```shell
$ papermill download_cordex.ipynb download_cordex.europe_mpi_mpi.ipynb -p gcm_model "mpi_m_mpi_esm_lr" -p rcm_model "mpi_csc_remo2009" -p domain "europe" -p horizontal_resolution "0_11_degree_x_0_11_degree"
$ papermill download_cordex.ipynb download_cordex.africa_mpi_clmcom.ipynb -p gcm_model "mpi_m_mpi_esm_lr" -p rcm_model "clmcom_kit_cclm5_0_15" -p domain "africa" -p horizontal_resolution "0_22_degree_x_0_22_degree"
```
As a result, we'll have a number of randomly named ZIP files in `data/orig/`

## Performance-optimised netCDF files

The netCDF files available from CDS are compressed (deflated in their own terms) netCDF-4 files with chunks of size `{"time": 1, "lon": "full", "lat": "fulll"}`.
Hence, _any_ read from the file will always have to read full spatial domains. 
For example, if a user requests one single time step for one single location, the netCDF libary will load the whole spatial field for the respective time step, uncompress it, select the requested time step, and forget the rest.
For the Europe domain, this is a `400^2` overhead when users are only interested in time series of single locations.

We'll transform all files to uncompressed files that don't use any chunking.
For the CORDEX data, uncompressed netCDF files are approximately 90% larger than the compressed files.

In addition to chunks limiting througput, it's also advisable to stay away from netCDF4, because netCDF4 with HDF5 underneath does not allow for multi-threaded reads on the same file. This limitation is not present for netCDF3 files. So we go for netCDF3 files (with 64bit offset to allow for bigger than 2GB files).

And finally, once the model simulation is finished, there is no use for record (or unlimited) time dimensions (as we don't _record_ any data any more). So we transform the time dimension to a regular fixed dimension. This further helps with fast opening of files and with random access.

So in summary, we do:
```shell
$ cd data/orig/
$ ls -1tr *.zip | xargs -P4 -I {} unzip -o {}
$ ls -1tr *.nc | xargs -P4 -I {} nccopy -6 -u {} ../performance/{}
$ cd -
```
The `ls -1tr` will work in chronological order on the `zip` and `nc` files.
Hence, it accommodates the impatient who may want to have a look at the data while the download is still running.

If everything looks good, we can delete the `.zip` and `.nc` files from `data/orig/`.