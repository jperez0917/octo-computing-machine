from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404

from accounts.forms import CustomUserCreationForm
from accounts.models import CustomUser


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class UserProfileView(DetailView):
    model = CustomUser
    template_name = 'accounts/user_profile.html'
    context_object_name = 'user_profile'

    def get_object(self):
        stuff =  get_object_or_404(CustomUser, username=self.kwargs['username'])

        # print(dir(stuff))
        # ['DoesNotExist', 'EMAIL_FIELD', 'Meta', 'MultipleObjectsReturned', 'REQUIRED_FIELDS', 'USERNAME_FIELD', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_check_column_name_clashes', '_check_constraints', '_check_default_pk', '_check_field_name_clashes', '_check_fields', '_check_id_field', '_check_index_together', '_check_indexes', '_check_local_fields', '_check_long_column_names', '_check_m2m_through_same_relationship', '_check_managers', '_check_model', '_check_model_name_db_lookup_clashes', '_check_ordering', '_check_property_name_related_field_accessor_clashes', '_check_single_primary_key', '_check_swappable', '_check_unique_together', '_do_insert', '_do_update', '_get_FIELD_display', '_get_expr_references', '_get_next_or_previous_by_FIELD', '_get_next_or_previous_in_order', '_get_pk_val', '_get_unique_checks', '_meta', '_password', '_perform_date_checks', '_perform_unique_checks', '_prepare_related_fields_for_save', '_save_parents', '_save_table', '_set_pk_val', '_state', 'check', 'check_password', 'clean', 'clean_fields', 'date_error_message', 'date_joined', 'delete', 'email', 'email_user', 'first_name', 'from_db', 'full_clean', 'get_all_permissions', 'get_deferred_fields', 'get_email_field_name', 'get_full_name', 'get_group_permissions', 'get_next_by_date_joined', 'get_previous_by_date_joined', 'get_session_auth_hash', 'get_short_name', 'get_user_permissions', 'get_username', 'groups', 'has_module_perms', 'has_perm', 'has_perms', 'has_usable_password', 'id', 'is_active', 'is_anonymous', 'is_authenticated', 'is_staff', 'is_superuser', 'last_login', 'last_name', 'links', 'logentry_set', 'natural_key', 'normalize_username', 'objects', 'password', 'pk', 'prepare_database_save', 'refresh_from_db', 'save', 'save_base', 'serializable_value', 'set_password', 'set_unusable_password', 'unique_error_message', 'user_permissions', 'username', 'username_validator', 'validate_unique']

        # print(dir(stuff.links))
        # [
        #     '__call__', '__class__', '__class_getitem__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__slotnames__', '__str__', '__subclasshook__', '__weakref__', '_apply_rel_filters', '_constructor_args', '_db', '_get_queryset_methods', '_hints', '_insert', '_queryset_class', '_remove_prefetched_objects', '_set_creation_counter', '_update', 'add', 'aggregate', 'alias', 'all', 'annotate', 'auto_created', 'bulk_create', 'bulk_update', 'check', 'complex_filter', 'contains', 'contribute_to_class', 'core_filters', 'count', 'create', 'creation_counter', 'dates', 'datetimes', 'db', 'db_manager', 'deconstruct', 'defer', 'difference', 'distinct', 'do_not_call_in_templates', 'earliest', 'exclude', 'exists', 'explain', 'extra', 'field', 'filter', 'first', 'from_queryset', 'get', 'get_or_create', 'get_prefetch_queryset', 'get_queryset', 'in_bulk', 'instance', 'intersection', 'iterator', 'last', 'latest', 'model', 'name', 'none', 'only', 'order_by', 'prefetch_related', 'raw', 'reverse', 'select_for_update', 'select_related', 'set', 'union', 'update', 'update_or_create', 'use_in_migrations', 'using', 'values', 'values_list'
        # ]

        # print(stuff.links.all())
        # <QuerySet [
        #     <Link: 21 : admin : FlexBox>,
        #     <Link: 18 : admin : https://www.django-rest-framework.org/api-guide/generic-views/#retrieveapiview>,
        #     <Link: 17 : admin : https://www.django-rest-framework.org/>,
        #     <Link: 5 : admin : Octo Computing Machine>,
        #     <Link: 4 : admin : TAP>,
        #     <Link: 1 : admin : Octopi Public - admin>
        # ]>
        
        # print(stuff.links.count())
        # 6

        # print(stuff.links.values())
        # <QuerySet [
        #     {
        #         'id': 21, 'url_label': 'FlexBox', 'url': 'https://css-tricks.com/snippets/css/a-guide-to-flexbox/', 'notes': 'CSS FlexBox', 'date_created': datetime.datetime(2022, 4, 30, 17, 14, 30, 421090, tzinfo=datetime.timezone.utc), 'public': True, 'owner_id': 1
        #     },
        #     {
        #         'id': 18, 'url_label': 'https://www.django-rest-framework.org/api-guide/generic-views/#retrieveapiview', 'url': 'https://www.django-rest-framework.org/api-guide/generic-views/#retrieveapiview', 'notes': 'RetrieveAPIView', 'date_created': datetime.datetime(2022, 4, 28, 15, 18, 41, 606643, tzinfo=datetime.timezone.utc), 'public': False, 'owner_id': 1
        #     },
        #     {
        #         'id': 17, 'url_label': 'https://www.django-rest-framework.org/', 'url': 'https://www.django-rest-framework.org/', 'notes': 'https://www.django-rest-framework.org/', 'date_created': datetime.datetime(2022, 4, 28, 15, 18, 21, 4028, tzinfo=datetime.timezone.utc), 'public': True, 'owner_id': 1
        #     },
        #     {
        #         'id': 5, 'url_label': 'Octo Computing Machine', 'url': 'https://github.com/jperez0917/octo-computing-machine', 'notes': 'This is the most-awesome repo of code from the minds of Josse Perez and Bruce Stull.', 'date_created': datetime.datetime(2022, 4, 25, 22, 17, 22, 836319, tzinfo=datetime.timezone.utc), 'public': True, 'owner_id': 1
        #     },
        #     {
        #         'id': 4, 'url_label': 'TAP', 'url': 'https://technology-and-perceptibility.herokuapp.com/', 'notes': 'Farm-to-table chambray gochujang meh, knausgaard health goth edison bulb biodiesel. XOXO put a bird on it blue bottle hot chicken, cloud bread enamel pin edison bulb squid stumptown kogi microdosing chia. Normcore green juice air plant umami, selfies typewriter flannel meh. Bespoke fanny pack cornhole health goth coloring book slow-carb tote bag etsy letterpress la croix brooklyn semiotics roof party.', 'date_created': datetime.datetime(2022, 4, 25, 22, 10, 29, 513724, tzinfo=datetime.timezone.utc), 'public': False, 'owner_id': 1
        #     },
        #     {
        #         'id': 1, 'url_label': 'Octopi Public - admin', 'url': 'http://octopi.local/', 'notes': 'Man bun butcher enamel pin, tote bag venmo taxidermy disrupt fashion axe four dollar toast. Unicorn fanny pack tbh 3 wolf moon, truffaut single-origin coffee bicycle rights. Vape photo booth cred, chartreuse yr tofu etsy cloud bread deep v lyft pop-up tbh. Fingerstache celiac ennui green juice mlkshk cronut narwhal bespoke. Stumptown kinfolk sriracha kombucha hella man bun tousled art party freegan jianbing vice celiac salvia lumbersexual fanny pack.', 'date_created': datetime.datetime(2022, 4, 25, 22, 9, 10, 373621, tzinfo=datetime.timezone.utc), 'public': True, 'owner_id': 1
        #     }
        # ]>

        return stuff