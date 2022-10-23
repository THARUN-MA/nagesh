from django.contrib import admin
from fs.models import userdetail,subdetail,srtmvcounter,albcounter,short,album

admin.site.register(userdetail)
admin.site.register(subdetail)
admin.site.register(albcounter)
admin.site.register(srtmvcounter)
admin.site.register(short)
admin.site.register(album)
# Register your models here.
