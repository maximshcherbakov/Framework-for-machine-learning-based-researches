from code.measurement.base import base_measurement as bm

class mean_square_error(bm.base_measurement):
    
    def calculate(self, actual_set, forecasted_set):
        measure = 0
        for actual, forecasted in zip(actual_set, forecasted_set):
            measure += (actual - forecasted) ** 2
        return measure / len(actual_set)

    def get_name(self):
        return 'MSE'



