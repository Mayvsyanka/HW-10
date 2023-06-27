from django.forms import ModelForm, CharField, Textarea, ModelChoiceField, MultipleChoiceField, Select, SelectMultiple, TextInput, ModelMultipleChoiceField
from .models import Quote, Author, Tag
from .utils import connection

class QuoteForm(ModelForm):
    quote = CharField(widget=Textarea)
    author = ModelChoiceField(queryset=Author.objects.all().order_by("fullname"), widget=Select())
    tags = ModelMultipleChoiceField(queryset=Tag.objects.all().order_by("name"), required=True, widget=SelectMultiple)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].label_from_instance = lambda obj: obj.fullname
    

    class Meta:
        model = Quote
        fields = '__all__'


class AuthorForm(ModelForm):
    fullname = CharField(max_length=50, widget=TextInput())
    born_date = CharField(max_length=50, widget=TextInput())
    born_location = CharField(max_length=150, widget=TextInput())
    description = CharField(widget=Textarea)

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']


class TagForm(ModelForm):
    name = ModelMultipleChoiceField(queryset=Tag.objects.all().order_by("name"), required=True, widget=SelectMultiple)

    class Meta:
        model = Tag
        fields = ['name']