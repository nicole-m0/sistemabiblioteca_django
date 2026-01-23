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
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

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


class Autor(models.Model):
    id_autor = models.AutoField(primary_key=True, blank=True)
    nome = models.TextField()

    class Meta:
        managed = False
        db_table = 'autor'


class Cadastro(models.Model):
    id_cadastro = models.AutoField(primary_key=True, blank=True)
    login = models.TextField(unique=True)
    senha = models.TextField()
    data_cadastro = models.DateField()
    status = models.TextField()

    class Meta:
        managed = False
        db_table = 'cadastro'


class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nome = models.TextField()
    descricao = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'categoria'


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

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


class Editora(models.Model):
    id_editora = models.AutoField(primary_key=True, blank=True)
    nome = models.TextField()
    telefone = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'editora'


class Emprestimo(models.Model):
    id_emprestimo = models.AutoField(primary_key=True, blank=True)
    data_emprestimo = models.DateField()
    data_devolucao = models.DateField(blank=True)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')

    class Meta:
        managed = False
        db_table = 'emprestimo'


class ItemEmprestado(models.Model):
    pk = models.CompositePrimaryKey('id_emprestimo', 'id_livro')
    id_emprestimo = models.ForeignKey(Emprestimo, models.DO_NOTHING, db_column='id_emprestimo')
    id_livro = models.ForeignKey('Livro', models.DO_NOTHING, db_column='id_livro')

    class Meta:
        managed = False
        db_table = 'item_emprestado'


class Livro(models.Model):
    id_livro = models.AutoField(primary_key=True, blank=True)
    titulo = models.TextField()
    isbn = models.TextField(unique=True, blank=True)
    ano_publicacao = models.IntegerField(blank=True)
    id_categoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='id_categoria')
    id_editora = models.ForeignKey(Editora, models.DO_NOTHING, db_column='id_editora')

    class Meta:
        managed = False
        db_table = 'livro'


class LivroAutor(models.Model):
    pk = models.CompositePrimaryKey('id_livro', 'id_autor')
    id_livro = models.ForeignKey(Livro, models.DO_NOTHING, db_column='id_livro')
    id_autor = models.ForeignKey(Autor, models.DO_NOTHING, db_column='id_autor')

    class Meta:
        managed = False
        db_table = 'livro_autor'


class Multa(models.Model):
    id_multa = models.AutoField(primary_key=True, blank=True)
    valor = models.FloatField()
    data = models.DateField()
    status = models.TextField()
    id_emprestimo = models.OneToOneField(Emprestimo, models.DO_NOTHING, db_column='id_emprestimo')

    class Meta:
        managed = False
        db_table = 'multa'


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True, blank=True)
    nome = models.TextField()
    email = models.TextField(unique=True, blank=True)
    telefone = models.TextField(blank=True)
    id_cadastro = models.ForeignKey(Cadastro, models.DO_NOTHING, db_column='id_cadastro')

    class Meta:
        managed = False
        db_table = 'usuario'

