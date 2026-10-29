"""课程 65481 的 Tortoise ORM 学习模型骨架。"""
from tortoise import fields
from tortoise.models import Model
class User(Model):
 id=fields.IntField(pk=True); username=fields.CharField(max_length=50,unique=True); password=fields.CharField(max_length=255); name=fields.CharField(max_length=50); department=fields.CharField(max_length=50,null=True); created_at=fields.DatetimeField(auto_now_add=True)
 class Meta: table='t_users'
class Section(Model):
 id=fields.IntField(pk=True); user_id=fields.IntField(); source_name=fields.CharField(max_length=255,null=True); name=fields.CharField(max_length=100); created_at=fields.DatetimeField(auto_now_add=True); updated_at=fields.DatetimeField(auto_now=True)
 class Meta: table='t_sections'
class Title(Model):
 id=fields.IntField(pk=True); section_id=fields.IntField(); title=fields.CharField(max_length=255); sort_order=fields.IntField(); content=fields.TextField(null=True); status=fields.CharField(max_length=255,null=True); view_count=fields.CharField(max_length=255,null=True); like_count=fields.CharField(max_length=255,null=True); created_at=fields.DatetimeField(auto_now_add=True); updated_at=fields.DatetimeField(auto_now=True)
 class Meta: table='t_titles'
