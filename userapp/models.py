from django.db import models

# Create your models here.

class UserModel(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(help_text='user_name',max_length=500)
    user_email = models.CharField(help_text='user_email',max_length=500)
    user_password = models.CharField(help_text='user_password',max_length=800)
    user_phone = models.CharField(help_text='user_phone',max_length=100)
    user_city = models.CharField(help_text='user_city',max_length=300)
    user_pic = models.ImageField(upload_to ='uploads/',max_length=300)
    # user_key = models.CharField(help_text='user_key',max_length=500,null=True)
    
    class Meta:
        db_table = 'user_details'
    

class ComplaintModel(models.Model):
    complaint_id = models.AutoField(primary_key=True)
    suspect_name = models.CharField(help_text='suspect_name',max_length=500)
    Complaint_type = models.CharField(help_text='complaint_type',max_length=30)
    Evidence = models.FileField(upload_to='uploads/', max_length=500,default=None)
    Approx_date = models.DateField(auto_now=False)
    occured_place = models.CharField(help_text='occured_place',max_length=100)
    complaint_date = models.DateTimeField(auto_now=True)
    status = models.CharField(help_text='status',default='Received',max_length=20)
    suspect_block_chain = models.CharField(help_text='suspect_block_chain',max_length=100,null=True)
    Complaint_type_block_chain = models.CharField(help_text='Complaint_type_block_chain',max_length=100,null=True)
    Approx_date_block_chain = models.CharField(help_text='Approx_date_block_chain',max_length=100,null=True)
    occured_place_block_chain = models.CharField(help_text='occured_place_block_chain',max_length=100,null=True)
    Evidence_block_chain = models.CharField(help_text='Evidence_block_chain',max_length=500,null=True)
    user = models.ForeignKey(UserModel,models.CASCADE,null=True)
    Case_fill_as = models.CharField(help_text='case_fill_as',max_length=50,null=True,default=None)
    Discard_reason = models.CharField(help_text='Disard_reason',max_length=500,null=True,default=None)
    
    class Meta:
        db_table = 'user_complaints'
        
class FeedbackModel(models.Model):
    feedback_id =  models.AutoField(primary_key=True)
    star = models.IntegerField()
    comment = models.CharField(help_text='comment',max_length=500)
    user = models.ForeignKey(UserModel,models.CASCADE,null=True)
    
    class Meta:
        db_table = 'user_comments'       