class base_model(object):
    
    def forecast(self, parameters, training_set, forecast_horizon):
        raise NotImplementedError('Calling method of base_model class is not eligible')


