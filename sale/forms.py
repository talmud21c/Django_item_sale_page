from django import forms
from .models import SaleBill


class SaleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['wallet_addr'].widget.attrs.update({'class': 'textinput form-control setprice wallet_addr', 'maxlength':'10', 'required': 'true'})
        self.fields['purchase_quantity'].widget.attrs.update({'class': 'textinput form-control setprice purchase_quantity', 'min': '1', 'required': 'true'})
        self.fields['bill_no'].widget.attrs.update({'class': 'textinput form-control setprice bill_no', 'required': 'true'})

    class Meta:
        model = SaleBill
        fields = ['wallet_addr', 'purchase_quantity','total_price', 'bill_no']