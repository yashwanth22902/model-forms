from django import forms
from app.models import *

class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'
class WebpageForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'
        ##labels={'topic_name':'TOPIC NAME'}
        ###exclude=['topic_name']
        ###widgets={'url':forms.PasswordInput}
        ###widgets={'name':forms.Textarea}

class AcessRecordForm(forms.ModelForm):
    class Meta:
        model=AcessRecord
        fields='__all__'