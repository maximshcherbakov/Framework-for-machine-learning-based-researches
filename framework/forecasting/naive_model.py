from framework.forecasting.base import base_model as bm

class naive_model(bm.base_model):

    def forecast(self, parameters, training_set, forecast_horison):
        forecast_values = {}
        for x in training_set:
        	forecast_values[x] = list(training_set[x][len(training_set) - forecast_horison:])

        return forecast_values

    def get_name(self):
    	return 'naive'