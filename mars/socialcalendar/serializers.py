from rest_framework import serializers
from .models import Caldata

class CaldataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caldata
        fields = ('id','site','month','vtlid','vtlname','lv1id','lv1name','lv2id','lv2name','lv3id','lv3name',
    'lv4id','lv4name','lvleafid','lvleafname','power','bi','gmb','bisnr','gmbsnr')
