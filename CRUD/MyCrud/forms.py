from django import forms

class AddNewList(forms.Form):
    todo_name = forms.CharField(label = "Todo Name", max_length=200)
    check = forms.BooleanField(required=False, label="Completed")  # Checkbox for completion status