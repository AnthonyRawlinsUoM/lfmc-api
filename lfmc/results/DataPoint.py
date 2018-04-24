from marshmallow import Schema, fields
import datetime as dt

class DataPoint:
    def __init__(self, observation_time: fields.String(), value: fields.Decimal(), mean: fields.Decimal(), minimum: fields.Decimal(), maximum: fields.Decimal(), deviation: fields.Decimal()):
        """Short summary.

        Parameters
        ----------
        observation_time : type
                Description of parameter `observation_time`.
        value : type
                Description of parameter `value`.
        mean : type
                Description of parameter `mean`.
        minimum : type
                Description of parameter `minimum`.
        maximum : type
                Description of parameter `maximum`.
        deviation : type
                Description of parameter `deviation`.

        Returns
        -------
        type
                Description of returned object.

        """
        self.name = observation_time
        self.value = value
        self.mean = mean
        self.minimum = minimum
        self.maximum = maximum
        self.deviation = deviation


class DataPointSchema(Schema):
    # date = fields.Date(attribute="test")
    # name = fields.DateTime(format="%Y-%m-%dT00:00:00.000Z")
    name = fields.String()
    value = fields.Decimal()
    mean = fields.Decimal()
    minimum = fields.Decimal()
    maximum = fields.Decimal()
    deviation = fields.Decimal()
