from django import forms
from .models import HostInfo,UserInfo

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

class BaseInfo(forms.ModelForm):
    def get_error(self):
        news_errors = []
        errors = self.errors.get_json_data()
        for messages in errors.values():
        # [[{'message': '用户名最小长度不能少于4位！', 'code': 'min_length'}],[{'message': '密码最小长度不能少于6位！', 'code': 'min_length'}]]
            for message_dict in messages:
                for key, message in message_dict.items():
                    if key == 'message':
                        news_errors.append(message)
        return news_errors
class HostInfoForm(BaseInfo):
    #query = forms.CharField(max_length=8)
    class Meta:
        model = HostInfo
        fields = '__all__'

        error_messages = {
            'host_user':{
                'required': '请填写用户名',
            },
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
            },
            'dep':{
                'invalid_choice':'请选择部门'
            }


        }


class UserInfoForm(BaseInfo):
    class Meta:
        model = UserInfo
        fields = '__all__'

