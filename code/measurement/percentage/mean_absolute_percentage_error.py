import code.measurement.base.base_measurement as bm

class mean_absolute_percentage_error(bm.base_measurement):
    
    def calculate(self, actual_set, forecasted_set):
        measurement = 0
        for actual, forecasted in zip(actual_set, forecasted_set):
            p = abs(actual - forecasted) / actual
            measurement += 100 * abs(p)
        return measurement / len(actual_set)

    def get_name():
        return 'MAPE'
