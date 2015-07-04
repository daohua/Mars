# -*- coding: utf-8 -*-

import os
import sys

sys.path.append('/opt/projects/backend/server/django/mars')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mars.settings")

import datetime
from decimal import Decimal
from socialcalendar.models import Caldata

"""
Base class for reading data files
"""
class DataReader(object):

    def __init__(self, datafile):
        self.datafile = datafile # The DataFile object for loading

    # load do actual data loading work from files. 
    # subclass have to override this 
    def load(self):
        pass

    # load single data file
    def loadSingleFile(self, data):
        pass

   # parse the header of the data file
    def parseHeader(self, header):
        pass

    # parse the data rows of the file
    # @param row - list of cells for the row
    # @return the parsing resulted model object from the row
    def parseRow(self, row):
        pass

    # get object with the provided key from db or create a new model object with the provided key
    # @param key - Model object key 
    def getOrCreateModelObject(self, key):
        pass

    def isZipfile(self, filename):
        return filename.endswith('.zip')

    def isValidDatafile(self, filename):
        return True

    #factory method to create readers according to data file category
    @staticmethod
    def newDataReader(datafile):
        if datafile.category == DataFile.TYPE_JSON:
            pass
        elif datafile.category == DataFile.TYPE_EXCEL:
            pass
        elif datafile.category == DataFile.TYPE_CVS:
            pass
        elif datafile.category == DataFile.TYPE_TXT:
            pass
        else:
            return None

class SocialCalendarReader(DataReader):
    month = ("JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC")

    def __init__(self, file_path):
        self.path = file_path

    def parseHeader(self):
        pass

    def loadSingleFile(self):
        datas = []
        with open(self.path) as infile:
            for index, row in enumerate(infile):
                datas.extend(self.parseRow(row))
                if len(datas)==720000: 
                    Caldata.objects.bulk_create(datas)
                    datas = []
            if datas:
                Caldata.objects.bulk_create(datas)

    def parseRow(self, row):
        datas = []
        arr = row.replace('\n','').split('\t')
        bi = [arr[x] for x in xrange(17, 29)]
        bisnr = [arr[x] for x in xrange(29, 41)]
        gmb = [arr[x] for x in xrange(45, 57)]
        gmbsnr = [arr[x] for x in xrange(57, 69)]

        for x in xrange(0,12):
            data = Caldata()
            data.site=int(arr[0])
            data.month=self.month[x]
            data.power=None

            data.bi=None if bi[x] == '' or bi[x] =='NA' else Decimal(bi[x])
            data.bisnr=None if bisnr[x] == '' or bisnr[x] =='NA' else float(bisnr[x])
            data.gmb=None if gmb[x] == '' or gmb[x] =='NA' else Decimal(gmb[x])
            data.gmbsnr=None if gmbsnr[x] == '' or gmbsnr[x] =='NA' else float(gmbsnr[x])

            data.lv1id= None if arr[2] == '' or arr[2] =='NA' else int(arr[2])
            data.lv1name=None if arr[1] == '' or arr[1] =='NA' else arr[1]
            data.lv2id=None if arr[6] == '' or arr[6] =='NA' else int(arr[6])
            data.lv2name=None if arr[5] == '' or arr[5] =='NA' else arr[5]
            data.lv3id=None if arr[8] == '' or arr[8] =='NA' else int(arr[8])
            data.lv3name=None if arr[7] == '' or arr[7] =='NA' else arr[7]
            data.lv4id=None if arr[10] == '' or arr[10] =='NA' else int(arr[10])
            data.lv4name=None if arr[9] == '' or arr[9] =='NA' else arr[9]
            data.lvleafid=None if arr[12] == '' or arr[12] =='NA' else int(arr[12])
            data.lvleafname=None if arr[11] == '' or arr[11] =='NA' else arr[11]
            datas.append(data)

        return datas

    def isValidDatafile(self, filename):
        return filename.endswith('.txt') or filename.endswith('.TXT')


if __name__ == '__main__':
    SocialCalendarReader("./sample/dataSchema.txt").loadSingleFile()