from code.forecasting_models.base import base_model as bm

class naive_model(bm.base_model):

    def forecast(self, parameters, training_set, forecast_horison):
        forecast_values = None

        forecast_values = training_set[len(training_set) - forecast_horison:len(training_set)]

        return forecast_values

