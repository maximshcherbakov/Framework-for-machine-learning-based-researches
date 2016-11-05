import code.measurement.base.base_measurement as bm
from statistics import median


class symmetric_median_absolute_percentage_error(bm.base_measurement):
    
    def calculate(self, actual_set, forecast_set):
         results = []
        
         for actual, forecasted in zip(actual_set, forecast_set):
             p = abs(actual - forecasted) / (actual + forecasted)
             results.append(200 * abs(p))

         return median(results)

    def get_name(self):
        return 'sMdAPE'
