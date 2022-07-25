from django.db import models 

class user1(models.Model):
    username = models.CharField(max_length=20 , primary_key =True)

    def __str__(self):
        return str(self.username)

class Interest(models.Model):

    INTEREST = ( ('makeup','makeup') , ('art','art') , ('henna','henna') , ('nature','nature') , ('recipes','recipes') ,
    ('friendship','friendship') , ('beauty_products','beauty_products') , ('flowers','flowers') , ('hairstyles','hairstyles') , ('babies','babies') ,
    ('child','child') , ('sketching','sketching') , ('travel','travel') , ('yoga','yoga') , ('nails','nails') ,
    ('birthday','birthday') , ('disney','disney') , ('dress','dress') , ('birds','birds') , ('jewellery','jewellery') ,
    ('positive_quotes','positive_quotes') , ('drawing','drawing') , ('love','love') , ('shoes','shoes') , ('morning','morning') )

    username = models.ForeignKey(user1 , on_delete = models.CASCADE)
    interest = models.CharField(max_length=20 , choices = INTEREST , null = False)

    def __str__(self):
        return str(self.username)

class Image(models.Model):

    INTEREST = ( ('makeup','makeup') , ('art','art') , ('henna','henna') , ('nature','nature') , ('recipes','recipes') ,
    ('friendship','friendship') , ('beauty_products','beauty_products') , ('flowers','flowers') , ('hairstyles','hairstyles') , ('babies','babies') ,
    ('child','child') , ('sketching','sketching') , ('travel','travel') , ('yoga','yoga') , ('nails','nails') ,
    ('birthday','birthday') , ('disney','disney') , ('dress','dress') , ('birds','birds') , ('jewellery','jewellery') ,
    ('positive_quotes','positive_quotes') , ('drawing','drawing') , ('love','love') , ('shoes','shoes') , ('morning','morning') , ('other' , 'other'))

    username = models.ForeignKey(user1 , on_delete=models.CASCADE)
    image_id = models.AutoField(primary_key = True)
    image = models.ImageField(upload_to = 'pins/')
    title = models.CharField(max_length=200 , null = False)
    description = models.CharField(max_length=500 , null = False)
    created_datetime = models.DateTimeField(auto_now_add = True)
    category = models.CharField(max_length=20 , choices = INTEREST , null = False)

    def __str__(self):
        return str(self.image_id)

class Like(models.Model):
    username = models.ForeignKey(user1 , on_delete=models.CASCADE)
    image_id = models.ForeignKey(Image , on_delete=models.CASCADE)

    def __str__(self):
        return str(self.username)

class Save(models.Model):
    username = models.ForeignKey(user1 , on_delete=models.CASCADE)
    image_id = models.ForeignKey(Image , on_delete=models.CASCADE)

    def __str__(self):
        return str(self.username)