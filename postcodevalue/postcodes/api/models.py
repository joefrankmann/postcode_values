from django.db import models

class Outcode(models.Model):
    outcode_code = models.CharField(max_length=8)
    listing_count = models.IntegerField()
    average_daily_rate = models.FloatField()

    def __str__(self):
        return f'{self.outcode_code}'

class NexusOutcode(models.Model):
    outcode_code = models.CharField(max_length=8)
    listing_count = models.IntegerField()
    average_daily_rate = models.FloatField()

    next_outcode_1 = models.ForeignKey(Outcode, related_name='nexus1', on_delete=models.CASCADE, blank=True, null=True)
    distance_1 = models.CharField(max_length=8, blank=True, null=True) 

    next_outcode_2 = models.ForeignKey(Outcode, related_name='nexus2', on_delete=models.CASCADE, blank=True, null=True)
    distance_2 = models.CharField(max_length=8, blank=True, null=True)
    
    next_outcode_3 = models.ForeignKey(Outcode, related_name='nexus3', on_delete=models.CASCADE, blank=True, null=True)
    distance_3 = models.CharField(max_length=8, blank=True, null=True)

    next_outcode_4 = models.ForeignKey(Outcode, related_name='nexus4', on_delete=models.CASCADE, blank=True, null=True)
    distance_4 = models.CharField(max_length=8, blank=True, null=True)
    
    next_outcode_5 = models.ForeignKey(Outcode, related_name='nexus5', on_delete=models.CASCADE, blank=True, null=True)
    distance_5 = models.CharField(max_length=8, blank=True, null=True)
    
    next_outcode_6 = models.ForeignKey(Outcode, related_name='nexus6', on_delete=models.CASCADE, blank=True, null=True)
    distance_6 = models.CharField(max_length=8, blank=True, null=True)
    
    next_outcode_7 = models.ForeignKey(Outcode, related_name='nexus7', on_delete=models.CASCADE, blank=True, null=True)
    distance_7 = models.CharField(max_length=8, blank=True, null=True)
    
    next_outcode_8 = models.ForeignKey(Outcode, related_name='nexus8', on_delete=models.CASCADE, blank=True, null=True)
    distance_8 = models.CharField(max_length=8, blank=True, null=True)
    
    next_outcode_9 = models.ForeignKey(Outcode, related_name='nexus9', on_delete=models.CASCADE, blank=True, null=True)
    distance_9 = models.CharField(max_length=8, blank=True, null=True)
    
    next_outcode_10 = models.ForeignKey(Outcode, related_name='nexus10', on_delete=models.CASCADE, blank=True, null=True)
    distance_10 = models.CharField(max_length=8, blank=True, null=True)
    

    def __str__(self):
        return f'{self.outcode_code}'