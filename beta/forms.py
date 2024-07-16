from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

sex_status = [
    ('1', 'دائم‌السیخ'),
    ('2', 'دائم‌الخیس'),
    ('3', 'من کافورم!')
]

pet_status = [
    ('c', 'گربه'),
    ('d', 'سگ'),
    ('no', 'ندارم')
]

class User_form(forms.Form):
    
    name = forms.CharField(label='اسم‌تون', max_length=70, error_messages={
        'required': 'لطفا اسمتو بنویس',
        #'max_length': 'این اسمو یه کامیون نمی‌تونه بکشه!' # max_length error message is not displayed 
    })
    
    net = forms.IntegerField(widget=forms.NumberInput, label='دارایی خالص‌تون (تومان)', validators=[MaxValueValidator(999999999)], error_messages={
        'required': 'بدون پول که نمیشه',
        'max_value': 'ایلان ماسک کی بودی؟' # MaxValueValidator is not the correct name for this error. find the correct name
    })
    ex = forms.IntegerField(label='تعداد اکس‌تون', required=False, validators=[MaxValueValidator(99)], error_messages={
        'max_value': 'نه دیگه، یه چیزی بگو که جور دربیاد'
    })
    # >>> Pay attention to the following field. If we want to have radio buttons, it is possible through forms.ChoiceField
    sex = forms.ChoiceField(label='وضعیت سکس‌تون', choices=sex_status, widget=forms.RadioSelect, error_messages={
        'required': 'یکی رو باید انتخاب کنی'
    })
    pet = forms.ChoiceField(label='پت‌تون', choices=pet_status, widget=forms.RadioSelect, error_messages={
        'required': 'یکی رو باید انتخاب کنی', 
    })
    neighbourhood = forms.CharField(label='محله‌تون', max_length=100, error_messages={
        'required': 'ما نمیایم خونه‌تون',
        'max_length': 'خداوکیلی اینجا زندگی می‌کنی؟'
    })

    # >>> Attention: The __init__ function allows us to pass attributes to the form fields. In the following case, we passed class and id attributes. It is also possible to pass these attributes through widget in the form field, but if we want to use for loop in the html template to populate fields, the only way is the init function.
    def __init__(self, *args, **kwargs):
        super(User_form, self).__init__(*args, **kwargs)
        self.fields['sex'].widget.attrs.update({'class': 'sexint'}) # sexint class will be used in the CSS file to apply desired styles
        self.fields['pet'].widget.attrs.update({'class': 'sexint'})
        self.fields['net'].widget.attrs.update({'style': 'font-family: Estedad;'})

        

        
