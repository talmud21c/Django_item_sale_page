from django import forms
from .models import SaleBill


class SaleForm(forms.ModelForm):

    #template_name = salesform.html

    class Meta:
        model = SaleBill
        fields = ['wallet_addr', 'purchase_quantity', 'bill_no']