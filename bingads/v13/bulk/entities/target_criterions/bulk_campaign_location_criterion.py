from bingads.v13.bulk.entities import *
from bingads.service_client import _CAMPAIGN_OBJECT_FACTORY_V13
from bingads.v13.internal.bulk.entities.single_record_bulk_entity import _SingleRecordBulkEntity
from bingads.v13.internal.bulk.mappings import _SimpleBulkMapping
from bingads.v13.internal.bulk.string_table import _StringTable
from bingads.v13.internal.extensions import *

class BulkCampaignLocationCriterion(_SingleRecordBulkEntity):
    """ Represents an Campaign Location Criterion that can be read or written in a bulk file.

    This class exposes the :attr:`biddable_campaign_criterion` property that can be read and written as fields of the
    Campaign Location Criterion record in a bulk file.

    For more information, see Campaign Location Criterion at https://go.microsoft.com/fwlink/?linkid=846127.

    *See also:*

    * :class:`.BulkServiceManager`
    * :class:`.BulkOperation`
    * :class:`.BulkFileReader`
    * :class:`.BulkFileWriter`
    """

    def __init__(self,
                 biddable_campaign_criterion=None,
                 campaign_name=None, ):
        super(BulkCampaignLocationCriterion, self).__init__()

        self._biddable_campaign_criterion = biddable_campaign_criterion
        self._campaign_name = campaign_name

    _MAPPINGS = [
        _SimpleBulkMapping(
            _StringTable.Status,
            field_to_csv=lambda c: bulk_str(c.biddable_campaign_criterion.Status),
            csv_to_field=lambda c, v: setattr(c.biddable_campaign_criterion, 'Status', v if v else None)
        ),
        _SimpleBulkMapping(
            _StringTable.Id,
            field_to_csv=lambda c: bulk_str(c.biddable_campaign_criterion.Id),
            csv_to_field=lambda c, v: setattr(c.biddable_campaign_criterion, 'Id', int(v) if v else None)
        ),
        _SimpleBulkMapping(
            _StringTable.ParentId,
            field_to_csv=lambda c: bulk_str(c.biddable_campaign_criterion.CampaignId),
            csv_to_field=lambda c, v: setattr(c.biddable_campaign_criterion, 'CampaignId', int(v) if v else None)
        ),
        _SimpleBulkMapping(
            _StringTable.Campaign,
            field_to_csv=lambda c: c.campaign_name,
            csv_to_field=lambda c, v: setattr(c, 'campaign_name', v)
        ),
        _SimpleBulkMapping(
            _StringTable.BidAdjustment,
            field_to_csv=lambda c: field_to_csv_BidAdjustment(c.biddable_campaign_criterion),
            csv_to_field=lambda c, v: csv_to_field_BidAdjustment(c.biddable_campaign_criterion, float(v) if v else None)
        ),
        _SimpleBulkMapping(
            _StringTable.Target,
            field_to_csv=lambda c: field_to_csv_LocationTarget(c.biddable_campaign_criterion),
            csv_to_field=lambda c, v: csv_to_field_LocationTarget(c.biddable_campaign_criterion, int(v) if v else None)
        ),
        _SimpleBulkMapping(
            _StringTable.SubType,
            field_to_csv=lambda c: field_to_csv_LocationType(c.biddable_campaign_criterion),
            csv_to_field=lambda c, v: csv_to_field_LocationType(c.biddable_campaign_criterion, v)
        ),
        _SimpleBulkMapping(
            _StringTable.Name,
            field_to_csv=lambda c: field_to_csv_LocationName(c.biddable_campaign_criterion),
            csv_to_field=lambda c, v: csv_to_field_LocationName(c.biddable_campaign_criterion, v)
        ),
    ]

    @property
    def biddable_campaign_criterion(self):
        """ Defines a Campaign Criterion """

        return self._biddable_campaign_criterion

    @biddable_campaign_criterion.setter
    def biddable_campaign_criterion(self, biddable_campaign_criterion):
        self._biddable_campaign_criterion = biddable_campaign_criterion

    @property
    def campaign_name(self):
        """ The name of the Campaign

        :rtype: str
        """

        return self._campaign_name

    @campaign_name.setter
    def campaign_name(self, campaign_name):
        self._campaign_name = campaign_name

    def process_mappings_to_row_values(self, row_values, exclude_readonly_data):
        self._validate_property_not_null(self.biddable_campaign_criterion, 'biddable_campaign_criterion')
        self.convert_to_values(row_values, BulkCampaignLocationCriterion._MAPPINGS)

    def process_mappings_from_row_values(self, row_values):
        self._biddable_campaign_criterion = _CAMPAIGN_OBJECT_FACTORY_V13.create('BiddableCampaignCriterion')
        self._biddable_campaign_criterion.Type = 'BiddableCampaignCriterion'
        self._biddable_campaign_criterion.Criterion = _CAMPAIGN_OBJECT_FACTORY_V13.create('LocationCriterion')
        self._biddable_campaign_criterion.Criterion.Type = 'LocationCriterion'
        self._biddable_campaign_criterion.CriterionBid = _CAMPAIGN_OBJECT_FACTORY_V13.create('BidMultiplier')
        self._biddable_campaign_criterion.CriterionBid.Type = 'BidMultiplier'
        row_values.convert_to_entity(self, BulkCampaignLocationCriterion._MAPPINGS)

    def read_additional_data(self, stream_reader):
        super(BulkCampaignLocationCriterion, self).read_additional_data(stream_reader)
