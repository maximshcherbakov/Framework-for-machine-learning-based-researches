from framework.measurement.base import base_measurement as bm

class mean_absolute_error(bm.base_measurement):
    
    def calculate(self, actual_set, forecasted_set):
        measure = 0
        for actual, forecasted in zip(actual_set, forecasted_set):
            measure += abs(actual - forecasted)
        return measure / len(actual_set)

    def get_name(self):
    	return 'MAE'