from rest_framework import serializers
from . models import PersonDetails,Team,Demo

class PersonSerializer(serializers.ModelSerializer):
# class PersonSerializer(serializers.HyperlinkedModelSerializer):
    # team_info = serializers.SerializerMethodField()
    class Meta:
        model = PersonDetails
        fields = '__all__'
        # fields = ['id','url','team','name','place','domain']
        depth = 1
        
    # def get_team_info(self,a):
    #     return "information feild"
    
class TeamSerilalizer(serializers.ModelSerializer):
#     member = PersonSerializer(many = True,read_only=True)
    class Meta:
        model = Team
#         field = ['teamName','id']
        fields = '__all__'
#     # def validate(self, data):
    #     spcl_chara = '!@#$%^&*()_+-=<>?,.'
        
    #     if any(x in spcl_chara for x in data['name']):
    #         raise serializers.ValidationError('name should not contain spcl characters')
        
        # if len(data['number'])!=10:
        #     raise serializers.ValidationError("Phone Number can't be less or more 10 number")
        
        
        
class DemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demo
        fields = '__all__'