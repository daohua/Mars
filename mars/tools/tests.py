import os
import sys
sys.path.append('/opt/projects/backend/server/django/mars')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mars.settings")

from django.test import TestCase
from socialcalendar.models import Caldata

# Create your tests here.
class Data(object):

    def __init__(self, *args):
        self._data = list(args)

    def __iter__(self):
        for x in self._data:
            yield x

class CalendarReader(object):

    month = ("JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC")

    def __init__(self, file_path):
        self.path = file_path

    def parseHeader(self):
        pass

    def loadSingleFile(self):
        # datas = []
        with open(self.path) as infile:
            for index, row in enumerate(infile):
                if index == 0:
                    pass
                else:
                    datas = self.parseRow(row)
                    Caldata.objects.bulk_create(datas)
                    # datas.extend(self.parseRow(row))d
                    # if len(datas)==24: 
                    #     Caldata.objects.bulk_create(datas)
                    #     datas = []
                if index==10000:
                    break

    def parseRow(self, row):
        datas = []
        arr = row.replace('\n','').split('\t')
        bi = [arr[x] for x in xrange(17, 29)]
        bisnr = [arr[x] for x in xrange(29, 41)]
        gmb = [arr[x] for x in xrange(45, 57)]
        gmbsnr = [arr[x] for x in xrange(57, 69)]

        for x in xrange(0,12):
            data = Caldata()
            data.site=arr[0]
            data.month=self.month[x]
            data.power=None

            data.bi=bi[x]
            data.bisnr=bisnr[x]
            data.gmb=gmb[x]
            data.gmbsnr=gmbsnr[x]

            data.lv1id= None if arr[2] == '' or arr[2] =='NA' else arr[2]
            data.lv1name=None if arr[1] == '' or arr[1] =='NA' else arr[1]
            data.lv2id=None if arr[6] == '' or arr[6] =='NA' else arr[6]
            data.lv2name=None if arr[5] == '' or arr[5] =='NA' else arr[5]
            data.lv3id=None if arr[8] == '' or arr[8] =='NA' else arr[8]
            data.lv3name=None if arr[7] == '' or arr[7] =='NA' else arr[7]
            data.lv4id=None if arr[10] == '' or arr[10] =='NA' else arr[10]
            data.lv4name=None if arr[9] == '' or arr[9] =='NA' else arr[9]
            data.lvleafid=None if arr[12] == '' or arr[12] =='NA' else arr[12]
            data.lvleafname=None if arr[11] == '' or arr[11] =='NA' else arr[11]
            datas.append(data)

        return datas

    def __str__(self):
        for data in datas:
            print "{0}.{1}.{2}.{3}.{4}".format(
                data.lv1id,
                data.lv1name,
                data.lv2id,
                data.lv2name,
                data.lv3id,
                data.lv3name,
                data.lv4id,
                data.lv4name,
                data.lvleafid,
                data.lvleafname)
        print '\n'


if __name__ == '__main__':
    CalendarReader("./sample/dataSchema.txt").loadSingleFile()
    # with open("./sample/dataSchema.txt.ori") as infile:
    #     fields = []
    #     for index, line in enumerate(infile):
    #         arr = line.split('\t')
    #         if index==0:
    #             fields=arr
    #         else:
    #             if fields is not None:      
    #                 data_map = dict(zip(fields, arr))
    #                 print data_map
            
    #         if index==2:
    #             break
  

