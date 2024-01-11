from django.contrib import admin
from .models import Transaksi, DetailTransaksi


class TransaksiAdmin(admin.ModelAdmin):
    list_display = ("no_transaksi", "total_transaki",
                    "status", "tanggal_kirim",)


class DetailTransaksiAdmin(admin.ModelAdmin):
    list_display = ("no_transaksi", "produk", "jumlah",)


admin.site.register(Transaksi), TransaksiAdmin
admin.site.register(DetailTransaksi, DetailTransaksiAdmin)
