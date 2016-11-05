import code.measurement.base.base_measurement as bm

class symmetric_mean_absolute_percentage_error(bm.base_measurement):
    
    def calculate(self, actual_set, forecasted_set):
        measurement = 0
        for actual, forecasted in zip(actual_set, forecasted_set):
            p = abs(actual - forecasted) / (actual + forecasted)
            measurement += 200 * abs(p)
        return measurement / len(actual_set)
    
    def get_name(self):
        return 'sMAPE'