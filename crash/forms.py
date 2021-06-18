from django import forms

class betForm(forms.Form):
    def __init__(self, *args, **kwargs):
        if kwargs.get('user') != None:
            self.user = kwargs.pop('user')
            super(betForm, self).__init__(*args, **kwargs)
            self.fields['bet'] = forms.IntegerField(label='Enter bet amount', min_value=1, max_value=self.user.stats.balance)

    bet = forms.IntegerField(label='Enter bet amount', min_value=1, max_value=1000) #in the future change max value to the user's balance
    multiplier = forms.FloatField(label='Enter cashout multiplier', min_value=1)

    class Meta:
        fields = ["bet amount","cashout multiplier"]
    
    