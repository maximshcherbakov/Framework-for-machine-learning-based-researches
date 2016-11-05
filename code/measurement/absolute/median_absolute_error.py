from code.measurement.base import base_measurement as bm
from statistics import median

class median_absolute_error(bm.base_measurement):

    def calculate(self, actual_set, forecasted_set):
        results = []
        
        for actual, predicted in zip(actual_set, forecasted_set):
            results.append(abs(actual - forecasted))

        return median(results)

    def get_name(self):
        return 'MdAE'