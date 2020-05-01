# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = True
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CoursesContent(models.Model):
    object_id = models.IntegerField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    module = models.ForeignKey('CoursesModule', models.DO_NOTHING)
    order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'courses_content'


class CoursesCourse(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(unique=True, max_length=200)
    overview = models.TextField()
    created = models.DateTimeField()
    owner = models.ForeignKey(AuthUser, models.DO_NOTHING)
    subject = models.ForeignKey('CoursesSubject', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'courses_course'


class CoursesFile(models.Model):
    title = models.CharField(max_length=250)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    file = models.CharField(max_length=100)
    owner = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'courses_file'


class CoursesImage(models.Model):
    title = models.CharField(max_length=250)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    file = models.CharField(max_length=100)
    owner = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'courses_image'


class CoursesModule(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    course = models.ForeignKey(CoursesCourse, models.DO_NOTHING)
    order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'courses_module'


class CoursesSubject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(unique=True, max_length=200)

    class Meta:
        managed = False
        db_table = 'courses_subject'


class CoursesText(models.Model):
    title = models.CharField(max_length=250)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    content = models.TextField()
    owner = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'courses_text'


class CoursesVideo(models.Model):
    title = models.CharField(max_length=250)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    url = models.CharField(max_length=200)
    owner = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'courses_video'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
