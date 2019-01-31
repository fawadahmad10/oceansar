
import time
from netCDF4 import Dataset
from oceansar.ocs_io import NETCDFHandler


class ProcFile(NETCDFHandler):
    """ Processed raw data file generated by the OASIS Simulator

        :param file_name: File name
        :param mode: Access mode (w = write, r = read, r+ = read + append)
        :param proc_dim: Processed raw data dimensions
        :param format: netCDF format

        .. note::
            Refer to netCDF4 Python library for details on access mode and
            available formats
    """
    def __init__(self, file_name, mode, proc_dim=None, format='NETCDF4'):

        self.__file__ = Dataset(file_name, mode, format)

        # If writing, define file
        if mode == 'w':
            # Set file attributes
            self.__file__.description = 'OASIS Processed Raw Data File'
            self.__file__.history = 'Created ' + time.ctime(time.time())
            self.__file__.source = 'OASIS Simulator'

            # Dimensions
            if not proc_dim:
                raise ValueError('Processed raw data dimensions are needed when creating a new file!')

            self.__file__.createDimension('ch_dim', proc_dim[0])
            self.__file__.createDimension('pol_dim', proc_dim[1])
            self.__file__.createDimension('az_dim', proc_dim[2])
            self.__file__.createDimension('rg_dim', proc_dim[3])

            # Variables
            slc_r = self.__file__.createVariable('slc_r',
                                                 'f8',
                                                 ('ch_dim',
                                                  'pol_dim',
                                                  'az_dim',
                                                  'rg_dim'))
            slc_i = self.__file__.createVariable('slc_i',
                                                 'f8',
                                                 ('ch_dim',
                                                  'pol_dim',
                                                  'az_dim',
                                                  'rg_dim'))
            slc_r.units = '[]'
            slc_i.units = '[]'

