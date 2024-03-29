# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountsRoles(models.Model):
    roleid = models.AutoField(db_column='roleId', primary_key=True)  # Field name made lowercase.
    rolename = models.CharField(db_column='roleName', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'accounts_roles'


class AccountsUsers(models.Model):
    userid = models.AutoField(db_column='userID', primary_key=True)  # Field name made lowercase.
    useremail = models.CharField(db_column='userEmail', unique=True, max_length=50)  # Field name made lowercase.
    userpassword = models.CharField(db_column='userPassword', max_length=20)  # Field name made lowercase.
    usertype = models.CharField(db_column='UserType', max_length=45, blank=True, null=True)  # Field name made lowercase.
    usertypekey = models.CharField(db_column='UserTypeKey', unique=True, max_length=10, blank=True, null=True)  # Field name made lowercase.
    roleid_id = models.CharField(db_column='roleId_id', max_length=80)  # Field name made lowercase.
    isactive = models.IntegerField(db_column='isActive', blank=True, null=True)  # Field name made lowercase.
    createdon = models.DateTimeField(db_column='createdOn')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'accounts_users'


class AttendanceMaxattendance(models.Model):
    maxattkey = models.AutoField(db_column='Maxattkey', primary_key=True)  # Field name made lowercase.
    subjectcode = models.CharField(db_column='SubjectCode', max_length=10)  # Field name made lowercase.
    section = models.CharField(db_column='Section', max_length=1)  # Field name made lowercase.
    maxclasses = models.IntegerField(db_column='MaxClasses')  # Field name made lowercase.
    fid = models.CharField(db_column='FID', max_length=10)  # Field name made lowercase.
    sem = models.IntegerField(db_column='Sem')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'attendance_maxattendance'


class AttendanceStudentattendance(models.Model):
    maxattkey = models.OneToOneField(AttendanceMaxattendance, models.DO_NOTHING, db_column='MaxAttkey', primary_key=True)  # Field name made lowercase. The composite primary key (MaxAttkey, USN) found, that is not supported. The first column is selected.
    usn = models.CharField(db_column='USN', max_length=45)  # Field name made lowercase.
    attended = models.IntegerField(db_column='Attended', blank=True, null=True)  # Field name made lowercase.
    percentage = models.FloatField(db_column='Percentage', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'attendance_studentattendance'
        unique_together = (('maxattkey', 'usn'), ('maxattkey', 'usn'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
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
    id = models.BigAutoField(primary_key=True)
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


class FacultyFacultymaster(models.Model):
    facultyid = models.CharField(db_column='facultyID', primary_key=True, max_length=10)  # Field name made lowercase.
    facultyname = models.CharField(db_column='facultyName', max_length=30)  # Field name made lowercase.
    gender = models.CharField(max_length=1)
    facultyphone = models.CharField(db_column='facultyPhone', unique=True, max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'faculty_facultymaster'


class FacultyFacultysubject(models.Model):
    section = models.CharField(max_length=1)
    facultyid = models.OneToOneField(FacultyFacultymaster, models.DO_NOTHING, db_column='facultyID_id', primary_key=True)  # Field name made lowercase. The composite primary key (facultyID_id, subjectCode_id, section) found, that is not supported. The first column is selected.
    subjectcode = models.ForeignKey('SubjectsSubjectmaster', models.DO_NOTHING, db_column='subjectCode_id')  # Field name made lowercase.
    sem = models.IntegerField(db_column='Sem')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'faculty_facultysubject'
        unique_together = (('facultyid', 'subjectcode', 'section'),)


class MarksMarksrecords(models.Model):
    usn = models.OneToOneField('StudentsStudentsubject', models.DO_NOTHING, db_column='usn', primary_key=True)  # The composite primary key (usn, subjectCode) found, that is not supported. The first column is selected.
    subjectcode = models.ForeignKey('StudentsStudentsubject', models.DO_NOTHING, db_column='subjectCode', related_name='marksmarksrecords_subjectcode_set')  # Field name made lowercase.
    ia1score = models.IntegerField(db_column='IA1Score')  # Field name made lowercase.
    ia2score = models.IntegerField(db_column='IA2Score')  # Field name made lowercase.
    ia3score = models.IntegerField(db_column='IA3Score', blank=True, null=True)  # Field name made lowercase.
    averageia = models.FloatField(db_column='AverageIA')  # Field name made lowercase.
    assignment1score = models.IntegerField(db_column='Assignment1Score', blank=True, null=True)  # Field name made lowercase.
    assignment2score = models.IntegerField(db_column='Assignment2Score', blank=True, null=True)  # Field name made lowercase.
    quiz1score = models.IntegerField(db_column='Quiz1Score', blank=True, null=True)  # Field name made lowercase.
    quiz2score = models.IntegerField(db_column='Quiz2Score', blank=True, null=True)  # Field name made lowercase.
    labrecordmarks = models.IntegerField(db_column='labRecordMarks', blank=True, null=True)  # Field name made lowercase.
    labobservationmarks = models.IntegerField(db_column='labObservationMarks', blank=True, null=True)  # Field name made lowercase.
    labvivamarks = models.IntegerField(db_column='labVivaMarks', blank=True, null=True)  # Field name made lowercase.
    finalia = models.IntegerField(db_column='FinalIA', blank=True, null=True)  # Field name made lowercase.
    eamarks = models.IntegerField(db_column='EAMarks', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'marks_marksrecords'
        unique_together = (('usn', 'subjectcode'),)


class StudentsStudentmaster(models.Model):
    usn = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=30)
    currentsem = models.IntegerField(db_column='currentSem')  # Field name made lowercase.
    section = models.CharField(max_length=3)
    gender = models.CharField(max_length=3)
    dateofbirth = models.DateField(db_column='dateOfBirth')  # Field name made lowercase.
    phone = models.CharField(unique=True, max_length=12)
    parentnumber = models.CharField(db_column='parentNumber', unique=True, max_length=12)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'students_studentmaster'


class StudentsStudentsubject(models.Model):
    subjectcode = models.OneToOneField('SubjectsSubjectmaster', models.DO_NOTHING, db_column='subjectCode_id', primary_key=True)  # Field name made lowercase. The composite primary key (subjectCode_id, usn_id) found, that is not supported. The first column is selected.
    usn = models.ForeignKey(StudentsStudentmaster, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'students_studentsubject'
        unique_together = (('subjectcode', 'usn'),)


class SubjectsSubjectmaster(models.Model):
    subjectcode = models.CharField(db_column='subjectCode', primary_key=True, max_length=10)  # Field name made lowercase.
    subjectname = models.CharField(db_column='subjectName', max_length=30)  # Field name made lowercase.
    subjecttype = models.IntegerField(db_column='subjectType')  # Field name made lowercase.
    sem = models.IntegerField()
    iselective = models.IntegerField(db_column='isElective')  # Field name made lowercase.
    credits = models.IntegerField()
    ia1 = models.IntegerField(db_column='IA1')  # Field name made lowercase.
    ia2 = models.IntegerField(db_column='IA2')  # Field name made lowercase.
    ia3 = models.IntegerField(db_column='IA3', blank=True, null=True)  # Field name made lowercase.
    avgia = models.FloatField(db_column='avgIA')  # Field name made lowercase.
    assignment1 = models.IntegerField(blank=True, null=True)
    assignment2 = models.IntegerField(blank=True, null=True)
    quiz1 = models.IntegerField(blank=True, null=True)
    quiz2 = models.IntegerField(blank=True, null=True)
    maxiamarks = models.IntegerField(db_column='maxIAMarks')  # Field name made lowercase.
    labobservation = models.IntegerField(db_column='labObservation', blank=True, null=True)  # Field name made lowercase.
    labrecord = models.IntegerField(db_column='labRecord', blank=True, null=True)  # Field name made lowercase.
    labviva = models.IntegerField(db_column='labViva', blank=True, null=True)  # Field name made lowercase.
    maxeamarks = models.IntegerField(db_column='maxEAMarks')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'subjects_subjectmaster'
