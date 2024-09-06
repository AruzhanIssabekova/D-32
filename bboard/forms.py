
from captcha.fields import CaptchaField
from django import forms


class FormWithCaptcha(forms.Form):
    name = forms.CharField(label='Name', max_length=50)
    email = forms.EmailField(label='Email')
    message = forms.CharField(widget=forms.Textarea, label='Text')
    captcha = CaptchaField()

# BbForm = modelform_factory(Bb,
#                            fields=('title', 'content', 'price', 'rubric'),
#                            labels={'title': 'Название товара'},
#                            help_texts={'rubric': 'Не забудь выбрать!'},
#                            field_classes={'price': IntegerField},
#                            widgets={'rubric': Select(attrs={'size': 8})})


# class BbForm(ModelForm):
#     class Meta:
#         model = Bb
#         fields = ('title', 'content', 'price', 'rubric')
#         labels={'title': 'Название товара'}
#         help_texts={'rubric': 'Не забудь выбрать!'}
#         field_classes={'price': IntegerField}
#         widgets={'rubric': Select(attrs={'size': 8})}



# class BbForm(forms.ModelForm):
#     title = forms.CharField(label='Название товара')
#     content = forms.CharField(label='Описание', widget=forms.widgets.Textarea())
#     price = forms.DecimalField(label='Цена', decimal_places=2)
#     rubric = forms.ModelChoiceField(queryset=Rubric.objects.all(),
#                                     label='Рубрики', help_text='Не забудь выбрать!',
#                                     widget=forms.widgets.Select(attrs={'size': 8}))
#     published = forms.DateField(widget=forms.widgets.SelectDateWidget(empty_label=('Выберите год', 'Выберите месяц', 'Выберите число')))
#
#     class Meta:
#         model = Bb
#         fields = ('title', 'content', 'price', 'rubric', 'published')
#         labels = {'title': 'Название товара'}
#
#     def clean_title(self):
#         val = self.cleaned_data.get('title')
#         if val == "Прошлогодний снег":
#             raise ValidationError('К продаже не допускается')
#         return val
#
#     def clean(self):
#         super().clean()
#         errors = {}
#         if not self.cleaned_data['content']:
#             errors['content'] = ValidationError('Укажите описание продаваемого товара')
#         if self.cleaned_data['price'] < 0:
#             errors['price'] = ValidationError('Укажите неотрицательное значение цены')
#         if errors:
#             raise ValidationError(errors)
#
#
#
# class RegisterUserForm(forms.ModelForm):
#     password1 = forms.CharField(label='Пароль')
#     password2 = forms.CharField(label='Пароль повторно')
#
#     captcha = CaptchaField(label = 'Введите текст с картинки', error_messages={'invalid': 'Неправельный текст'})
#
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')
#
#
#
#
# class SearchForm(forms.Form):
#     keyword = forms.CharField(max_length=20, label='Искомое слово')
#     rubric = forms.ModelChoiceField(queryset=Rubric.objects.all(), label='Рубрика')
#



