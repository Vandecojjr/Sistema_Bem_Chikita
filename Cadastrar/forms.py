from django import forms


class cadastor_m_prima(forms.Form):
    nome = forms.CharField(label='nome')
    descricao = forms.CharField(label='descricao')
    uMedida = forms.CharField(label='u_medida')
    valor = forms.CharField(label='valor')