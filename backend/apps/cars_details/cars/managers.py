
from django.db import models


class CarManager(models.Manager):
    def all_cars_with_price(self):
        return self.prefetch_related('price').all()  # як приклад відфільтрувати щось і зменшити навантаження на API

    def all_cars_by_premium_seller_id(self, pk):
        return self.prefetch_related('cars').filter(premium_seller_id=pk)

    # def save(self, *args, **kwargs):
    #     if self.attempts >= 3:
    #         self.attempts = 0
    #         messages.warning('Ad creation car blocked. Contact manager to unblocked')
    #         return super(CarModel, self).save(*args, **kwargs)
