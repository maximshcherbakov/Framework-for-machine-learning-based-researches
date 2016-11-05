import framework.measurement.base.base_measurement as bm
from framework.measurement.absolute.mean_square_error import mean_square_error as mse

class root_mean_square_error(bm.base_measurement):
    
    def calculate(self, actual_set, forecasted_set):
        mse_result = mse().calculate(actual_set, forecasted_set)
        return mse_result ** 0.5

    def get_name(self):
	    return 'RMSE'




