from django import forms
from .models import HostInfo

# class BaseForm(forms.ModelForm):
#     def get_errors(self):
#         errors = self.errors.get_json_data()
#         new_errors = {}
#         for key, message_dicts in errors.items():
#             messages = []
#             for message_dict in message_dicts:
#                 message = message_dict['message']
#                 messages.append(message)
#             new_errors[key] = messages
#         return new_errors
class HostInfoForm(forms.ModelForm):
    class Meta:
        model = HostInfo
        fields = '__all__'

        error_messages = {
            'host':{
                'required':'请填写主机编号',
                'invalid':'主机编号格式不正确，请重新填写'
            },
            'displayer': {
                'required': '请填写显示器编号',
                'invalid': '显示器编号格式不正确，请重新填写'
            },
            'ip_addr': {
                'required': '请填写IP地址',
                'invalid': 'IP地址格式不正确，请重新填写'
            },
            'username':{
                'required':'请填写用户名'
            }

        }
