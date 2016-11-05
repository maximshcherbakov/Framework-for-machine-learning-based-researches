import code.measurement.base.base_measurement as bm
from statistics import median

class median_absolute_percentage_error(bm.base_measurement):
    
    def calculate(self, actual_set, forecasted_set):
         results = []
        
         for actual, forecasted in zip(actual_set, forecasted_set):
             p = abs(actual - forecasted) / actual
             results.append(100 * abs(p))

         return median(results)

    def get_name(self):
        return 'MdAPE'

