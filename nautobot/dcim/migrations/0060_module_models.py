import uuid

import django.core.serializers.json
from django.db import migrations, models
import django.db.models.deletion

import nautobot.core.models.fields
import nautobot.extras.models.mixins
import nautobot.extras.models.roles
import nautobot.extras.models.statuses


class Migration(migrations.Migration):
    dependencies = [
        ("tenancy", "0009_update_all_charfields_max_length_to_255"),
        ("extras", "0106_populate_default_statuses_and_roles_for_contact_associations"),
        ("dcim", "0059_add_role_field_to_interface_models"),
    ]

    operations = [
        migrations.CreateModel(
            name="Module",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True, null=True)),
                ("last_updated", models.DateTimeField(auto_now=True, null=True)),
                (
                    "_custom_field_data",
                    models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder),
                ),
                ("serial", models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ("asset_tag", models.CharField(blank=True, max_length=255, null=True, unique=True)),
                (
                    "location",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="modules",
                        to="dcim.location",
                    ),
                ),
            ],
            options={
                "ordering": ("parent_module_bay", "location", "module_type", "asset_tag", "serial"),
            },
            bases=(
                models.Model,
                nautobot.extras.models.mixins.DynamicGroupMixin,
                nautobot.extras.models.mixins.NotesMixin,
            ),
        ),
        migrations.AlterField(
            model_name="consoleport",
            name="device",
            field=nautobot.core.models.fields.ForeignKeyWithAutoRelatedName(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="console_ports",
                to="dcim.device",
            ),
        ),
        migrations.AlterField(
            model_name="consoleporttemplate",
            name="device_type",
            field=nautobot.core.models.fields.ForeignKeyWithAutoRelatedName(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="console_port_templates",
                to="dcim.devicetype",
            ),
        ),
        migrations.AlterField(
            model_name="consoleserverport",
            name="device",
            field=nautobot.core.models.fields.ForeignKeyWithAutoRelatedName(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="console_server_ports",
                to="dcim.device",
            ),
        ),
        migrations.AlterField(
            model_name="consoleserverporttemplate",
            name="device_type",
            field=nautobot.core.models.fields.ForeignKeyWithAutoRelatedName(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="console_server_port_templates",
                to="dcim.devicetype",
            ),
        ),
        migrations.AlterField(
            model_name="frontport",
            name="device",
            field=nautobot.core.models.fields.ForeignKeyWithAutoRelatedName(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="front_ports",
                to="dcim.device",
            ),
        ),
        migrations.AlterField(
            model_name="frontporttemplate",
            name="device_type",
            field=nautobot.core.models.fields.ForeignKeyWithAutoRelatedName(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="front_port_templates",
                to="dcim.devicetype",
            ),
        ),
        migrations.AlterField(
            model_name="interface",
            name="device",
            field=nautobot.core.models.fields.ForeignKeyWithAutoRelatedName(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="interfaces",
                to="dcim.device",
            ),
        ),
        migrations.AlterField(
            model_name="interfacetemplate",
            name="device_type",
            field=nautobot.core.models.fields.ForeignKeyWithAutoRelatedName(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="interface_templates",
                to="dcim.devicetype",
            ),
        ),
        migrations.AlterField(
            model_name="poweroutlet",
            name="device",
            field=nautobot.core.models.fields.ForeignKeyWithAutoRelatedName(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="power_outlets",
                to="dcim.device",
            ),
        ),
        migrations.AlterField(
            model_name="poweroutlettemplate",
            name="device_type",
            field=nautobot.core.models.fields.ForeignKeyWithAutoRelatedName(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="power_outlet_templates",
                to="dcim.devicetype",
            ),
        ),
        migrations.AlterField(
            model_name="powerport",
            name="device",
            field=nautobot.core.models.fields.ForeignKeyWithAutoRelatedName(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="power_ports",
                to="dcim.device",
            ),
        ),
        migrations.AlterField(
            model_name="powerporttemplate",
            name="device_type",
            field=nautobot.core.models.fields.ForeignKeyWithAutoRelatedName(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="power_port_templates",
                to="dcim.devicetype",
            ),
        ),
        migrations.AlterField(
            model_name="rearport",
            name="device",
            field=nautobot.core.models.fields.ForeignKeyWithAutoRelatedName(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="rear_ports",
                to="dcim.device",
            ),
        ),
        migrations.AlterField(
            model_name="rearporttemplate",
            name="device_type",
            field=nautobot.core.models.fields.ForeignKeyWithAutoRelatedName(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="rear_port_templates",
                to="dcim.devicetype",
            ),
        ),
        migrations.CreateModel(
            name="ModuleType",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True, null=True)),
                ("last_updated", models.DateTimeField(auto_now=True, null=True)),
                (
                    "_custom_field_data",
                    models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder),
                ),
                ("model", models.CharField(max_length=255)),
                ("part_number", models.CharField(blank=True, max_length=255)),
                ("front_image", models.ImageField(blank=True, upload_to="devicetype-images")),
                ("rear_image", models.ImageField(blank=True, upload_to="devicetype-images")),
                (
                    "device_family",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="module_types",
                        to="dcim.devicefamily",
                    ),
                ),
                (
                    "manufacturer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, related_name="module_types", to="dcim.manufacturer"
                    ),
                ),
                ("tags", nautobot.core.models.fields.TagsField(through="extras.TaggedItem", to="extras.Tag")),
            ],
            options={
                "ordering": ("manufacturer", "model"),
                "unique_together": {("manufacturer", "model")},
            },
            bases=(
                models.Model,
                nautobot.extras.models.mixins.DynamicGroupMixin,
                nautobot.extras.models.mixins.NotesMixin,
            ),
        ),
        migrations.CreateModel(
            name="ModuleBay",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True, null=True)),
                ("last_updated", models.DateTimeField(auto_now=True, null=True)),
                (
                    "_custom_field_data",
                    models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder),
                ),
                ("position", models.CharField(max_length=255)),
                ("label", models.CharField(blank=True, max_length=255)),
                ("description", models.CharField(blank=True, max_length=255)),
                (
                    "device",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="module_bays",
                        to="dcim.device",
                    ),
                ),
                (
                    "parent_module",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="module_bays",
                        to="dcim.module",
                    ),
                ),
                ("tags", nautobot.core.models.fields.TagsField(through="extras.TaggedItem", to="extras.Tag")),
            ],
            options={
                "ordering": ("device", "parent_module__id", "position"),
                "unique_together": {("device", "position"), ("parent_module", "position")},
            },
            bases=(
                models.Model,
                nautobot.extras.models.mixins.DynamicGroupMixin,
                nautobot.extras.models.mixins.NotesMixin,
            ),
        ),
        migrations.AddField(
            model_name="module",
            name="module_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, related_name="modules", to="dcim.moduletype"
            ),
        ),
        migrations.AddField(
            model_name="module",
            name="parent_module_bay",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="installed_module",
                to="dcim.modulebay",
            ),
        ),
        migrations.AddField(
            model_name="module",
            name="role",
            field=nautobot.extras.models.roles.RoleField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="modules",
                to="extras.role",
            ),
        ),
        migrations.AddField(
            model_name="module",
            name="status",
            field=nautobot.extras.models.statuses.StatusField(
                on_delete=django.db.models.deletion.PROTECT, related_name="modules", to="extras.status"
            ),
        ),
        migrations.AddField(
            model_name="module",
            name="tags",
            field=nautobot.core.models.fields.TagsField(through="extras.TaggedItem", to="extras.Tag"),
        ),
        migrations.AddField(
            model_name="module",
            name="tenant",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="modules",
                to="tenancy.tenant",
            ),
        ),
        migrations.AddField(
            model_name="consoleport",
            name="module",
            field=nautobot.core.models.fields.ForeignKeyWithAutoRelatedName(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="console_ports",
                to="dcim.module",
            ),
        ),
        migrations.AddField(
            model_name="consoleporttemplate",
            name="module_type",
            field=nautobot.core.models.fields.ForeignKeyWithAutoRelatedName(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="console_port_templates",
                to="dcim.moduletype",
            ),
        ),
        migrations.AddField(
            model_name="consoleserverport",
            name="module",
            field=nautobot.core.models.fields.ForeignKeyWithAutoRelatedName(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="console_server_ports",
                to="dcim.module",
            ),
        ),
        migrations.AddField(
            model_name="consoleserverporttemplate",
            name="module_type",
            field=nautobot.core.models.fields.ForeignKeyWithAutoRelatedName(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="console_server_port_templates",
                to="dcim.moduletype",
            ),
        ),
        migrations.AddField(
            model_name="frontport",
            name="module",
            field=nautobot.core.models.fields.ForeignKeyWithAutoRelatedName(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="front_ports",
                to="dcim.module",
            ),
        ),
        migrations.AddField(
            model_name="frontporttemplate",
            name="module_type",
            field=nautobot.core.models.fields.ForeignKeyWithAutoRelatedName(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="front_port_templates",
                to="dcim.moduletype",
            ),
        ),
        migrations.AddField(
            model_name="interface",
            name="module",
            field=nautobot.core.models.fields.ForeignKeyWithAutoRelatedName(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="interfaces",
                to="dcim.module",
            ),
        ),
        migrations.AddField(
            model_name="interfacetemplate",
            name="module_type",
            field=nautobot.core.models.fields.ForeignKeyWithAutoRelatedName(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="interface_templates",
                to="dcim.moduletype",
            ),
        ),
        migrations.AddField(
            model_name="poweroutlet",
            name="module",
            field=nautobot.core.models.fields.ForeignKeyWithAutoRelatedName(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="power_outlets",
                to="dcim.module",
            ),
        ),
        migrations.AddField(
            model_name="poweroutlettemplate",
            name="module_type",
            field=nautobot.core.models.fields.ForeignKeyWithAutoRelatedName(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="power_outlet_templates",
                to="dcim.moduletype",
            ),
        ),
        migrations.AddField(
            model_name="powerport",
            name="module",
            field=nautobot.core.models.fields.ForeignKeyWithAutoRelatedName(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="power_ports",
                to="dcim.module",
            ),
        ),
        migrations.AddField(
            model_name="powerporttemplate",
            name="module_type",
            field=nautobot.core.models.fields.ForeignKeyWithAutoRelatedName(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="power_port_templates",
                to="dcim.moduletype",
            ),
        ),
        migrations.AddField(
            model_name="rearport",
            name="module",
            field=nautobot.core.models.fields.ForeignKeyWithAutoRelatedName(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="rear_ports",
                to="dcim.module",
            ),
        ),
        migrations.AddField(
            model_name="rearporttemplate",
            name="module_type",
            field=nautobot.core.models.fields.ForeignKeyWithAutoRelatedName(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="rear_port_templates",
                to="dcim.moduletype",
            ),
        ),
        migrations.CreateModel(
            name="ModuleBayTemplate",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True, null=True)),
                ("last_updated", models.DateTimeField(auto_now=True, null=True)),
                (
                    "_custom_field_data",
                    models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder),
                ),
                ("position", models.CharField(max_length=255)),
                ("label", models.CharField(blank=True, max_length=255)),
                ("description", models.CharField(blank=True, max_length=255)),
                (
                    "device_type",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="module_bay_templates",
                        to="dcim.devicetype",
                    ),
                ),
                (
                    "module_type",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="module_bay_templates",
                        to="dcim.moduletype",
                    ),
                ),
            ],
            options={
                "ordering": ("device_type", "module_type", "position"),
                "unique_together": {("device_type", "position"), ("module_type", "position")},
            },
        ),
        migrations.AlterUniqueTogether(
            name="module",
            unique_together={("module_type", "serial")},
        ),
    ]
