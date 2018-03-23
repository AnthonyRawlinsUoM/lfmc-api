from lfmc.query.Query import Query, QuerySchema
from marshmallow import Schema, fields
from lfmc.query.TemporalQuery import TemporalQuery, TemporalQuerySchema
from lfmc.query.SpatialQuery import SpatialQuery, SpatialQuerySchema


class SpatioTemporalQuery(Query, object):
  def __init__(self, lat1, lon1, lat2, lon2, start, finish):
    """Short summary.

    Parameters
    ----------
    lat1 : type
        Description of parameter `lat1`.
    lon1 : type
        Description of parameter `lon1`.
    lat2 : type
        Description of parameter `lat2`.
    lon2 : type
        Description of parameter `lon2`.
    start : type
        Description of parameter `start`.
    finish : type
        Description of parameter `finish`.

    Returns
    -------
    type
        Description of returned object.

    """
    self.spatial = SpatialQuery(lat1, lon1, lat2, lon2)
    self.temporal = TemporalQuery(start, finish)


class SpatioTemporalQuerySchema(Schema):
  meta = fields.Nested(QuerySchema)
  spatial = fields.Nested(SpatialQuerySchema)
  temporal = fields.Nested(TemporalQuerySchema)