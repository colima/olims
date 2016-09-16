"""The request for analysis by a client. It contains analysis instances.
"""
import datetime
from base_olims_model import BaseOLiMSModel
from fields.string_field import StringField
from fields.text_field import TextField
from fields.boolean_field import BooleanField
from fields.date_time_field import DateTimeField
from fields.fixed_point_field import FixedPointField
from fields.widget.widget import StringWidget, TextAreaWidget, \
                                BooleanWidget, DateTimeWidget, \
                                DecimalWidget, RichWidget
from openerp import fields, models, api
from openerp.tools.translate import _
AR_STATES = (
    ('sample_registered','Sample Registered'),
    ('not_requested','Not Requested'),
    ('to_be_sampled','To Be Sampled'),
    ('sampled','Sampled'),
    ('to_be_preserved','To Be Preserved'),
    ('sample_due','Sample Due'),
    ('sample_received','Received'),
    ('attachment_due','Attachment Outstanding'),
    ('to_be_verified','To be verified'),
    ('verified','Verified'),
    ('published','Published'),
    ('invalid','Invalid'),
    ('cancelled', 'Cancel')
    )
COPY_OPTIONS=(
    ('0','Select-to-copy'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3')
    )

schema = (fields.Char(string='RequestID',
                      compute='compute_analysisRequestId',
        ),
    fields.Many2one(string='Client',
                    comodel_name='olims.client',
                    required=False,

    ),
    fields.Many2one(string='Contact',
                    comodel_name='olims.contact',
                    relation='ar_contact',
                    required=True
    ),
    fields.Many2one(string='Contact1',
                    comodel_name='olims.contact',
                    relation='ar_contact',
                    required=False
    ),
    fields.Many2one(string='Contact2',
                    comodel_name='olims.contact',
                    relation='ar_contact',
                    required=False
    ),
    fields.Many2one(string='Contact3',
                    comodel_name='olims.contact',
                    relation='ar_contact',
                    required=False
    ),
    fields.Many2one(string='CCContact',
                    comodel_name='olims.contact',
                    relation='ar__cc_contact',
                    required=False
    ),
    fields.Many2one(string='CCContact1',
                    comodel_name='olims.contact',
                    relation='ar__cc_contact',
                    required=False
    ),
    fields.Many2one(string='CCContact2',
                    comodel_name='olims.contact',
                    relation='ar__cc_contact',
                    required=False
    ),
    fields.Many2one(string='CCContact3',
                    comodel_name='olims.contact',
                    relation='ar__cc_contact',
                    required=False
    ),
    StringField(
        'CCEmails',
    ),
    StringField(
        'CCEmails1',
    ),
    StringField(
        'CCEmails2',
    ),
    StringField(
        'CCEmails3',
    ),
    fields.Char(string='Sample',
                        compute='Compute_AnalysisSample',

    ),
    fields.Many2one(string='Sample_id',
                        comodel_name='olims.sample',

    ),
    fields.Many2one(string='Sample_id1',
                        comodel_name='olims.sample',

    ),
    fields.Many2one(string='Sample_id2',
                        comodel_name='olims.sample',

    ),
    fields.Many2one(string='Sample_id3',
                        comodel_name='olims.sample',

    ),
    fields.Many2one(string='Batch',
                        comodel_name='olims.batch',

    ),
    fields.Many2one(string='Batch1',
                        comodel_name='olims.batch',

    ),
    fields.Many2one(string='Batch2',
                        comodel_name='olims.batch',

    ),
    fields.Many2one(string='Batch3',
                        comodel_name='olims.batch',

    ),
    fields.Many2one(string='SubGroup',
                        comodel_name='olims.subgroup',
                        relation='ar_subgroup'

    ),
    fields.Many2one(string='SubGroup1',
                        comodel_name='olims.subgroup',
                        relation='ar_subgroup'

    ),
    fields.Many2one(string='SubGroup2',
                        comodel_name='olims.subgroup',
                        relation='ar_subgroup'

    ),
    fields.Many2one(string='SubGroup3',
                        comodel_name='olims.subgroup',
                        relation='ar_subgroup'

    ),
    fields.Many2one(string='Template',
                        comodel_name='olims.ar_template',

    ),
    fields.Many2one(string='Template1',
                        comodel_name='olims.ar_template',

    ),
    fields.Many2one(string='Template2',
                        comodel_name='olims.ar_template',

    ),
    fields.Many2one(string='Template3',
                        comodel_name='olims.ar_template',

    ),
    fields.Many2one(string='AnalysisProfile',
                        comodel_name='olims.analysis_profile',
                        relation='ar_to_analysisprofile'

    ),
    fields.Many2one(string='AnalysisProfile1',
                        comodel_name='olims.analysis_profile',
                        relation='ar_to_analysisprofile'

    ),
    fields.Many2one(string='AnalysisProfile2',
                        comodel_name='olims.analysis_profile',
                        relation='ar_to_analysisprofile'

    ),
    fields.Many2one(string='AnalysisProfile3',
                        comodel_name='olims.analysis_profile',
                        relation='ar_to_analysisprofile'

    ),
    fields.One2many(string='Partition',
                     comodel_name='olims.ar_partition',
                    inverse_name='analysis_request_id',
    ),
    fields.One2many(string='Sample Partition',
                     comodel_name='olims.ar_sample_partition',
                    inverse_name='analysis_request_id',
    ),
    fields.One2many(string='Analyses',
                     comodel_name='olims.ar_analysis',
                    inverse_name='analysis_request_id',
    ),
    # Sample field
    DateTimeField('DateSampled',
    ),
    # Sample field
    fields.Many2one(string='Sampler',
        comodel_name="res.users",
        domain="[('groups_id', 'in', [14,18])]",
    ),
    fields.Many2one(string='Sampler1',
        comodel_name="res.users",
        domain="[('groups_id', 'in', [14,18])]",
    ),
    fields.Many2one(string='Sampler2',
        comodel_name="res.users",
        domain="[('groups_id', 'in', [14,18])]",
    ),
    fields.Many2one(string='Sampler3',
        comodel_name="res.users",
        domain="[('groups_id', 'in', [14,18])]",
    ),
    DateTimeField(
        'SamplingDate',
        required=1,
    ),
    DateTimeField(
        'SamplingDate1',
        required=0,
    ),
    DateTimeField(
        'SamplingDate2',
        required=0,
    ),
    DateTimeField(
        'SamplingDate3',
        required=0,
    ),
    fields.Many2one(string='SampleType',
                        comodel_name='olims.sample_type',
                        required=True

    ),
    fields.Many2one(string='SampleType1',
                        comodel_name='olims.sample_type',
                        required=False

    ),
    fields.Many2one(string='SampleType2',
                        comodel_name='olims.sample_type',
                        required=False

    ),
    fields.Many2one(string='SampleType3',
                        comodel_name='olims.sample_type',
                        required=False

    ),
    fields.Many2one(string='Specification',
                        comodel_name='olims.analysis_spec',
                        relation='ar_analysis_spec',
                        required=False,
    ),
    fields.Many2one(string='Specification1',
                        comodel_name='olims.analysis_spec',
                        relation='ar_analysis_spec',
                        required=False,
    ),
    fields.Many2one(string='Specification2',
                        comodel_name='olims.analysis_spec',
                        relation='ar_analysis_spec',
                        required=False,
    ),
    fields.Many2one(string='Specification3',
                        comodel_name='olims.analysis_spec',
                        relation='ar_analysis_spec',
                        required=False,
    ),
    fields.Many2one(string='SamplePoint',
                        comodel_name='olims.sample_point',

    ),
    fields.Many2one(string='SamplePoint1',
                        comodel_name='olims.sample_point',

    ),
    fields.Many2one(string='SamplePoint2',
                        comodel_name='olims.sample_point',

    ),
    fields.Many2one(string='SamplePoint3',
                        comodel_name='olims.sample_point',

    ),
    fields.Many2one(string='StorageLocation',
                        comodel_name='olims.storage_location',

    ),
    fields.Many2one(string='StorageLocation1',
                        comodel_name='olims.storage_location',

    ),
    fields.Many2one(string='StorageLocation2',
                        comodel_name='olims.storage_location',

    ),
    fields.Many2one(string='StorageLocation3',
                        comodel_name='olims.storage_location',

    ),
    StringField(
        'LotID',
    ),
    StringField(
        'LotID1',
    ),
    StringField(
        'LotID2',
    ),
    StringField(
        'LotID3',
    ),
    # Sample field
    StringField(
        'ClientReference',
        searchable=True,
    ),
    StringField(
        'ClientReference1',
        searchable=True,
    ),
    StringField(
        'ClientReference2',
        searchable=True,
    ),
    StringField(
        'ClientReference3',
        searchable=True,
    ),
    # Sample field
    StringField(
        'ClientSampleID',
        searchable=True,
    ),
    StringField(
        'ClientSampleID1',
        searchable=True,
    ),
    StringField(
        'ClientSampleID2',
        searchable=True,
    ),
    StringField(
        'ClientSampleID3',
        searchable=True,
    ),
    fields.Many2one(string='SamplingDeviation',
                        comodel_name='olims.sampling_deviation',

    ),
    fields.Many2one(string='SamplingDeviation1',
                        comodel_name='olims.sampling_deviation',

    ),
    fields.Many2one(string='SamplingDeviation2',
                        comodel_name='olims.sampling_deviation',

    ),
    fields.Many2one(string='SamplingDeviation3',
                        comodel_name='olims.sampling_deviation',

    ),
#     # Sample field
    fields.Many2one(string='SampleCondition',
                        comodel_name='olims.sample_condition',

    ),
    fields.Many2one(string='SampleCondition1',
                        comodel_name='olims.sample_condition',

    ),
    fields.Many2one(string='SampleCondition2',
                        comodel_name='olims.sample_condition',

    ),
    fields.Many2one(string='SampleCondition3',
                        comodel_name='olims.sample_condition',

    ),
    fields.Many2one(string='DefaultContainerType',
                        comodel_name='olims.container_type',

    ),
    fields.Many2one(string='DefaultContainerType1',
                        comodel_name='olims.container_type',

    ),
    fields.Many2one(string='DefaultContainerType2',
                        comodel_name='olims.container_type',

    ),
    fields.Many2one(string='DefaultContainerType3',
                        comodel_name='olims.container_type',

    ),
    # Sample field
    BooleanField(
        'AdHoc',
        default=False,
    ),
    BooleanField(
        'AdHoc1',
        default=False,
    ),
    BooleanField(
        'AdHoc2',
        default=False,
    ),
    BooleanField(
        'AdHoc3',
        default=False,
    ),
    # Sample field
    BooleanField(
        'Composite',
        default=False,
    ),
    BooleanField(
        'Composite1',
        default=False,
    ),
    BooleanField(
        'Composite2',
        default=False,
    ),
    BooleanField(
        'Composite3',
        default=False,
    ),
    BooleanField(
        'ReportDryMatter',
        default=False,
    ),
    BooleanField(
        'ReportDryMatter1',
        default=False,
    ),
    BooleanField(
        'ReportDryMatter2',
        default=False,
    ),
    BooleanField(
        'ReportDryMatter3',
        default=False,
    ),
    BooleanField(
        'InvoiceExclude',
        default=False,
    ),
    BooleanField(
        'InvoiceExclude1',
        default=False,
    ),
    BooleanField(
        'InvoiceExclude2',
        default=False,
    ),
    BooleanField(
        'InvoiceExclude3',
        default=False,
    ),
    DateTimeField(
        'DateReceived',
    ),
    DateTimeField(
        'DatePublished',
    ),
    DateTimeField(
        'DateDue',
    ),
    TextField(
        string='Remarks',
        searchable=True,
    ),
    FixedPointField(
        'MemberDiscount',
    ),
    fields.Many2one(string='ChildAnalysisRequest',
                        comodel_name='olims.analysis_request',

    ),
    fields.Many2one(string='ParentAnalysisRequest',
                        comodel_name='olims.analysis_request',

    ),
    fields.Many2one(string='Priority',
                   comodel_name='olims.ar_priority',
                   required=False,

    ),
    fields.Many2one(string='Priority1',
                   comodel_name='olims.ar_priority',
                   required=False,

    ),
    fields.Many2one(string='Priority2',
                   comodel_name='olims.ar_priority',
                   required=False,

    ),
    fields.Many2one(string='Priority3',
                   comodel_name='olims.ar_priority',
                   required=False,

    ),
    TextField(
        string='ResultsInterpretation',
    ),
    fields.One2many(string='LabService',
                     comodel_name='olims.field_analysis_service',
                    inverse_name='ar_service_lab_id',
    ),
    fields.One2many(string='FieldService',
                     comodel_name='olims.field_analysis_service',
                    inverse_name='analysis_request_id',
    ),
    fields.Float(string='Discount',
                 compute='_ComputeServiceCalculation',
                 default=0.00
    ),
    fields.Float(string='Discount1',
                 compute='_ComputeServiceCalculation',
                 default=0.00
    ),
    fields.Float(string='Discount2',
                 compute='_ComputeServiceCalculation',
                 default=0.00
    ),
    fields.Float(string='Discount3',
                 compute='_ComputeServiceCalculation',
                 default=0.00
    ),
    fields.Float(string='Subtotal',
                 compute='_ComputeServiceCalculation',
                 default=0.00
    ),
    fields.Float(string='Subtotal1',
                 compute='_ComputeServiceCalculation',
                 default=0.00
    ),
    fields.Float(string='Subtotal2',
                 compute='_ComputeServiceCalculation',
                 default=0.00
    ),
    fields.Float(string='Subtotal3',
                 compute='_ComputeServiceCalculation',
                 default=0.00
    ),
    fields.Float(string='VAT',
                 compute='_ComputeServiceCalculation',
                 default=0.00
    ),
    fields.Float(string='VAT1',
                 compute='_ComputeServiceCalculation',
                 default=0.00
    ),
    fields.Float(string='VAT2',
                 compute='_ComputeServiceCalculation',
                 default=0.00
    ),
    fields.Float(string='VAT3',
                 compute='_ComputeServiceCalculation',
                 default=0.00
    ),
    fields.Float(string='Total',
                 compute='_ComputeServiceCalculation',
                 default=0.00
    ),
    fields.Float(string='Total1',
                 compute='_ComputeServiceCalculation',
                 default=0.00
    ),
    fields.Float(string='Total2',
                 compute='_ComputeServiceCalculation',
                 default=0.00
    ),
    fields.Float(string='Total3',
                 compute='_ComputeServiceCalculation',
                 default=0.00
    ),
    fields.Selection(string='state',
                     selection=AR_STATES,
                     default='sample_registered',
                     select=True,
                     required=True, readonly=True,
                     copy=False, track_visibility='always'
    ),
    fields.Selection(string='result_option',
                     selection=(('general','General'),
                                ('sampling','Sampling')
                                ),
                     default='general',
    ),
    fields.One2many(string="Field_Manage_Result",
        comodel_name="olims.manage_analyses",
        inverse_name="manage_analysis_id"),
    fields.One2many(string="Lab_Manage_Result",
        comodel_name="olims.manage_analyses",
        inverse_name="lab_manage_analysis_id"),
    fields.One2many(string="AddAnalysis",
        comodel_name="olims.add_analysis",
        inverse_name="add_analysis_id"),
    fields.Selection(
        string='CopyContact',
        selection=COPY_OPTIONS,
        default='0',
        select=True,
    ),
    fields.Selection(
        string='CopyCCContact',
        selection=COPY_OPTIONS,
        default='0',
        select=True,
    ),
    fields.Selection(
        string='CopyEmail',
        selection=COPY_OPTIONS,
        default='0',
        select=True,
    ),
    fields.Selection(
        string='Copysample',
        selection=COPY_OPTIONS,
        default='0',
        select=True,
    ),
    fields.Selection(
        string='Copybatch',
        selection=COPY_OPTIONS,
        default='0',
        select=True,
    ),
    fields.Selection(
        string='Copysubgroup',
        selection=COPY_OPTIONS,
        default='0',
        select=True,
    ),
    fields.Selection(
        string='Copytemplate',
        selection=COPY_OPTIONS,
        default='0',
        select=True,
    ),
    fields.Selection(
        string='Copyprofile',
        selection=COPY_OPTIONS,
        default='0',
        select=True,
    ),
    fields.Selection(
        string='Copysmaplingdate',
        selection=COPY_OPTIONS,
        default='0',
        select=True,
    ),
    fields.Selection(
        string='Copysampler',
        selection=COPY_OPTIONS,
        default='0',
        select=True,
    ),
    fields.Selection(
        string='Copysampletype',
        selection=COPY_OPTIONS,
        default='0',
        select=True,
    ),
    fields.Selection(
        string='Copyspecification',
        selection=COPY_OPTIONS,
        default='0',
        select=True,
    ),
    fields.Selection(
        string='Copysamplepoint',
        selection=COPY_OPTIONS,
        default='0',
        select=True,
    ),
    fields.Selection(
        string='Copystorage',
        selection=COPY_OPTIONS,
        default='0',
        select=True,
    ),
    fields.Selection(
        string='CopyLotID',
        selection=COPY_OPTIONS,
        default='0',
        select=True,
    ),
    fields.Selection(
        string='CopyClientReference',
        selection=COPY_OPTIONS,
        default='0',
        select=True,
    ),
    fields.Selection(
        string='CopyClientSampleID',
        selection=COPY_OPTIONS,
        default='0',
        select=True,
    ),
    fields.Selection(
        string='CopySamplingDeviation',
        selection=COPY_OPTIONS,
        default='0',
        select=True,
    ),
    fields.Selection(
        string='CopySampleCondition',
        selection=COPY_OPTIONS,
        default='0',
        select=True,
    ),
    fields.Selection(
        string='CopyDefaultContainerType',
        selection=COPY_OPTIONS,
        default='0',
        select=True,
    ),
    fields.Selection(
        string='CopyAdHoc',
        selection=COPY_OPTIONS,
        default='0',
        select=True,
    ),
    fields.Selection(
        string='CopyComposite',
        selection=COPY_OPTIONS,
        default='0',
        select=True,
    ),
    fields.Selection(
        string='CopyReportDryMatter',
        selection=COPY_OPTIONS,
        default='0',
        select=True,
    ),
    fields.Selection(
        string='CopyInvoiceExclude',
        selection=COPY_OPTIONS,
        default='0',
        select=True,
    ),
    fields.Selection(
        string='CopyPriority',
        selection=COPY_OPTIONS,
        default='0',
        select=True,
    ),
    fields.Selection(
        string='CopyDiscount',
        selection=COPY_OPTIONS,
        default='0',
        select=True,
    ),
    fields.Selection(
        string='CopySubtotal',
        selection=COPY_OPTIONS,
        default='0',
        select=True,
    ),
    fields.Selection(
        string='CopyVAT',
        selection=COPY_OPTIONS,
        default='0',
        select=True,
    ),
    fields.Selection(
        string='CopyTotal',
        selection=COPY_OPTIONS,
        default='0',
        select=True,
    ),
)
schema_analysis = (fields.Many2one(string='Service',
                    comodel_name='olims.analysis_service',
                    relation='analysisservice_analysisrequest',
                    domain="[('PointOfCapture', '=', 'field'),('category', '=', Category)]"
    ),
    fields.Many2one(string='LabService',
                     comodel_name='olims.analysis_service',
                    relation='analysisservice_analysisrequest',
                    domain="[('PointOfCapture', '=', 'lab'),('category', '=', Category)]"
    ),
    StringField('CommercialID',
        compute='_ComputeFieldResults',
        widget=StringWidget(
            label=_("Commercial ID"),
            description=_("The service's commercial ID for accounting purposes")
        ),
    ),
    StringField('ProtocolID',
        compute='_ComputeFieldResults',
        widget=StringWidget(
            label=_("Protocol ID"),
            description=_("The service's analytical protocol ID")
        ),
    ),
    fields.Many2one(string='analysis_request_id',
        comodel_name='olims.analysis_request',
        ondelete='cascade'
    ),
    fields.Many2one(string='ar_service_lab_id',
        comodel_name='olims.analysis_request',
        ondelete='cascade'
    ),
    StringField(string="Error"),
    StringField(string="Min"),
    StringField(string="Max"),
    fields.Many2one(string='Category',
        comodel_name='olims.analysis_category'),
)

manage_result_schema = (
    StringField(string="Partition"),
    StringField(string="Result"),
    BooleanField('+-', default=False),
    DateTimeField('Capture'),
    DateTimeField('Due Date'),
    # fields.Many2one(string="Result",
    #     comodel_name="olims.result_option"),
    fields.Many2one(string="Instrument",
        comodel_name="olims.instrument"),
    fields.Many2one(string="Analyst",
        comodel_name="res.users",
        domain="[('groups_id', 'in', [14,22])]"),
    StringField('Specifications'),
    fields.Many2one(string='manage_analysis_id',
        comodel_name='olims.analysis_request',
        # domain="[('state', '=', 'sample_received')]",
        ondelete='cascade'
    ),
    fields.Many2one(string='lab_manage_analysis_id',
        comodel_name='olims.analysis_request',
        # domain="[('state', '=', 'sample_received')]",
        ondelete='cascade'
    ),
    fields.Many2one(string='Method',
        comodel_name='olims.method',
        ),
    fields.Many2one(string='Category',
        comodel_name='olims.analysis_category'),
    fields.Selection(string='state',
                     selection=AR_STATES,
                     default='sample_received',
                     select=True,
                     readonly=True,
                     copy=False, track_visibility='always'
    )
    )

class AnalysisRequest(models.Model, BaseOLiMSModel): #(BaseFolder):
    _name = 'olims.analysis_request'
    _rec_name = "RequestID"
    _inherit = ['mail.thread', 'ir.needaction_mixin']

    def compute_analysisRequestId(self):
        for record in self:
            record.RequestID = 'R-0' + str(record.id)
    @api.multi
    def Compute_AnalysisSample(self):
        for record in self:
            if not record.Sample_id:
                sample = self.env["olims.sample"].search([('Analysis_Request', '=', record.id)])
                record.Sample = sample.SampleID
                record.Sample_id = sample.id
            else:
                record.Sample = record.Sample_id.SampleID

    @api.model
    def create(self, values):
        """Overwrite the create method of Odoo and create sample model data
           with fields SamplingDate and SampleType
        """
        list_of_dicts = []
        analysis_request_0_dict, analysis_request_1_dict, analysis_request_2_dict, analysis_request_3_dict = self.get_fields_value_dicts(
            values)

        analysis_object = super(AnalysisRequest, self).search([])
        if len(analysis_object) > 0:
            for ar_item in analysis_object[len(analysis_object)-1]:
                Partition = 'P-0'+ str(ar_item.id+1)+'-R-0'+str(ar_item.id+1)
        else:
            Partition = "P-01-R-01"
        data, field_result_list, lab_result_list = self.create_field_and_lab_analyses(Partition, values)

        analysis_request_0_dict.update({"Field_Manage_Result": field_result_list,
            "Lab_Manage_Result": lab_result_list})
        analysis_request_1_dict.update({"Field_Manage_Result": field_result_list,
            "Lab_Manage_Result": lab_result_list})
        analysis_request_2_dict.update({"Field_Manage_Result": field_result_list,
            "Lab_Manage_Result": lab_result_list})
        analysis_request_3_dict.update({"Field_Manage_Result": field_result_list,
                                        "Lab_Manage_Result": lab_result_list})

        list_of_dicts.append(analysis_request_0_dict)
        list_of_dicts.append(analysis_request_1_dict)
        list_of_dicts.append(analysis_request_2_dict)
        list_of_dicts.append(analysis_request_3_dict)

        for ar_values in list_of_dicts:
            if ar_values.get("Contact") and ar_values.get('SamplingDate') and ar_values.get('SampleType'):
                res = super(AnalysisRequest, self).create(ar_values)
                new_sample = self.create_sample(ar_values, res)

                analysis_object = super(AnalysisRequest, self).search([('id', '=',res.id)])
                analysis_object.write({"Sample_id":new_sample.id})

                ar_p = self.create_ar_partitions(res)
                ar_analysis_object = self.env['olims.ar_analysis']
                ar_service_lab_id = None
                for rec in data:
                    self.create_sample_partition(ar_analysis_object, ar_p, ar_values, rec, res)
        return res

    def create_sample_partition(self, ar_analysis_object, ar_p, ar_values, rec, res):
        if "LabService" in rec[2]:
            serv_temp = rec[2]['LabService']
        elif "Service" in rec[2]:
            serv_temp = rec[2]['Service']
        analyses_values = {
            'Priority': ar_values.get('Priority'),
            'Partition': ar_p.id,
            'analysis_request_id': res.id,
            'Category': rec[2]['Category'],
            'Services': serv_temp,
            'Min': rec[2]['Min'],
            'Max': rec[2]['Max'],
            'Error': rec[2]['Error']
        }
        ar_analysis_object.create(analyses_values)

    def create_ar_partitions(self, res):
        partition_values = {'State': res.state,
                            'analysis_request_id': res.id,
                            'Partition': 'P-0' + str(res.id) + '-R-0' + str(res.id)
                            }
        ar_partition_object = self.env["olims.ar_partition"]
        ar_sample_partition_object = self.env["olims.ar_sample_partition"]
        ar_sample_partition_object.create(partition_values)
        ar_p = ar_partition_object.create(partition_values)
        return ar_p

    def create_sample(self, ar_values, res):
        smaple_vals_dict = {
            'SamplingDate': ar_values.get('SamplingDate'),
            'SampleType': ar_values.get('SampleType'),
            'Client': ar_values.get('Client'),
            'Analysis_Request': res.id,
            'ClientReference': ar_values.get('ClientReference'),
            'ClientSampleID': ar_values.get('ClientSampleID'),
            'SamplePoint': ar_values.get('SamplePoint'),
            'StorageLocation': ar_values.get('StorageLocation'),
            'SamplingDeviation': ar_values.get('SamplingDeviation'),
            'SampleCondition': ar_values.get('SampleCondition'),
        }
        sample_object = self.env["olims.sample"]
        new_sample = sample_object.create(smaple_vals_dict)
        return new_sample

    def create_field_and_lab_analyses(self, Partition, values):
        data = []
        lab_result_list = []
        field_result_list = []
        for LabService in values.get('LabService'):
            Specification = ">" + str(LabService[2]['Min']) + ", <" + str(LabService[2]['Max']) + ", %" + str(
                LabService[2]['Error'])
            service_instance = self.env['olims.analysis_service'].search([('id', '=', LabService[2]['LabService'])])
            if service_instance._Method and service_instance.InstrumentEntryOfResults == False:
                LabService[2].update({'Method': service_instance._Method.id})
            elif service_instance.InstrumentEntryOfResults:
                LabService[2].update({'Method': None, 'Instrument': service_instance.Instrument})
            LabService[2].update({'Specifications': Specification,
                                  "Due Date": datetime.datetime.now(),
                                  'Partition': Partition})
            lab_result_list.append([0, 0, LabService[2]])
            data.append(LabService)
        for FieldService in values.get('FieldService'):
            Specification = ">" + str(FieldService[2]['Min']) + ", <" + str(FieldService[2]['Max']) + ", %" + str(
                FieldService[2]['Error'])
            service_instance = self.env['olims.analysis_service'].search([('id', '=', FieldService[2]['Service'])])
            if service_instance._Method and service_instance.InstrumentEntryOfResults == False:
                FieldService[2].update({'Method': service_instance._Method.id})
            elif service_instance.InstrumentEntryOfResults:
                FieldService[2].update({'Method': None, 'Instrument': service_instance.Instrument})
            FieldService[2].update({'Specifications': Specification,
                                    "Due Date": datetime.datetime.now(),
                                    'Partition': Partition})

            field_result_list.append([0, 0, FieldService[2]])
            data.append(FieldService)

        return data, field_result_list, lab_result_list

    def get_fields_value_dicts(self, values):
        client = values.get('Client', None)
        if not client:
            client = self._context.get('client_context', None)
        analysis_request_0_dict = {
            'StorageLocation': values.get('StorageLocation', None),
            'AdHoc': values.get('AdHoc', None),
            'Template': values.get('Template', None),
            'AnalysisProfile': values.get('AnalysisProfile', None),
            'ClientSampleID': values.get('ClientSampleID', None),
            'LotID': values.get('LotID', None),
            'SubGroup': values.get('SubGroup', None),
            'SampleType': values.get('SampleType', None),
            'Batch': values.get('Batch', None),
            'SamplingDeviation': values.get('SamplingDeviation', None),
            'ResultsInterpretation': values.get('ResultsInterpretation', None),
            'Sample Partition': values.get('Sample Partition', None),
            'SamplePoint': values.get('SamplePoint', None),
            'Specification': values.get('Specification', None),
            'Priority': values.get('Priority', None),
            'Partition': values.get('Partition', None),
            'SamplingDate': values.get('SamplingDate', None),
            'ReportDryMatter': values.get('ReportDryMatter', None),
            'Contact': values.get('Contact', None),
            'FieldService': values.get('FieldService', None),
            'CCEmails': values.get('CCEmails', None),
            'CCContact': values.get('CCContact', None),
            'Sampler': values.get('Sampler', None),
            'Composite': values.get('Composite', None),
            'Sample_id': values.get('Sample_id', None),
            'Analyses': values.get('Analyses', None),
            'Client': client,
            'InvoiceExclude': values.get('InvoiceExclude', None),
            'LabService': values.get('LabService', None),
            'Lab_Manage_Result': values.get('Lab_Manage_Result', None),
            'result_option': values.get('result_option', None),
            'Field_Manage_Result': values.get('Field_Manage_Result', None),
            'SampleCondition': values.get('SampleCondition', None),
            'Remarks': values.get('Remarks', None),
            'DefaultContainerType': values.get('DefaultContainerType', None),
        }
        analysis_request_1_dict = {
            'StorageLocation': values.get('StorageLocation1', None),
            'AdHoc': values.get('AdHoc1', None),
            'Template': values.get('Template1', None),
            'AnalysisProfile': values.get('AnalysisProfile1', None),
            'ClientSampleID': values.get('ClientSampleID1', None),
            'LotID': values.get('LotID1', None),
            'SubGroup': values.get('SubGroup1', None),
            'SampleType': values.get('SampleType1', None),
            'Batch': values.get('Batch1', None),
            'SamplingDeviation': values.get('SamplingDeviation1', None),
            'ResultsInterpretation': values.get('ResultsInterpretation', None),
            'Sample Partition': values.get('Sample Partition', None),
            'SamplePoint': values.get('SamplePoint1', None),
            'Specification': values.get('Specification1', None),
            'Priority': values.get('Priority1', None),
            'Partition': values.get('Partition', None),
            'SamplingDate': values.get('SamplingDate1', None),
            'ReportDryMatter': values.get('ReportDryMatter1', None),
            'Contact': values.get('Contact1', None),
            'FieldService': values.get('FieldService', None),
            'CCEmails': values.get('CCEmails1', None),
            'CCContact': values.get('CCContact1', None),
            'Sampler': values.get('Sampler1', None),
            'Composite': values.get('Composite1', None),
            'Sample_id': values.get('Sample_id1', None),
            'Analyses': values.get('Analyses', None),
            'Client': client,
            'InvoiceExclude': values.get('InvoiceExclude1', None),
            'LabService': values.get('LabService', None),
            'Lab_Manage_Result': values.get('Lab_Manage_Result', None),
            'result_option': values.get('result_option', None),
            'Field_Manage_Result': values.get('Field_Manage_Result', None),
            'SampleCondition': values.get('SampleCondition1', None),
            'Remarks': values.get('Remarks', None),
            'DefaultContainerType': values.get('DefaultContainerType1', None),
        }
        analysis_request_2_dict = {
            'StorageLocation': values.get('StorageLocation2', None),
            'AdHoc': values.get('AdHoc2', None),
            'Template': values.get('Template2', None),
            'AnalysisProfile': values.get('AnalysisProfile2', None),
            'ClientSampleID': values.get('ClientSampleID2', None),
            'LotID': values.get('LotID2', None),
            'SubGroup': values.get('SubGroup2', None),
            'SampleType': values.get('SampleType2', None),
            'Batch': values.get('Batch2', None),
            'SamplingDeviation': values.get('SamplingDeviation2', None),
            'ResultsInterpretation': values.get('ResultsInterpretation', None),
            'Sample Partition': values.get('Sample Partition', None),
            'SamplePoint': values.get('SamplePoint2', None),
            'Specification': values.get('Specification2', None),
            'Priority': values.get('Priority2', None),
            'Partition': values.get('Partition', None),
            'SamplingDate': values.get('SamplingDate2', None),
            'ReportDryMatter': values.get('ReportDryMatter2', None),
            'Contact': values.get('Contact2', None),
            'FieldService': values.get('FieldService', None),
            'CCEmails': values.get('CCEmails2', None),
            'CCContact': values.get('CCContact2', None),
            'Sampler': values.get('Sampler2', None),
            'Composite': values.get('Composite2', None),
            'Sample_id': values.get('Sample_id2', None),
            'Analyses': values.get('Analyses', None),
            'Client': client,
            'InvoiceExclude': values.get('InvoiceExclude2', None),
            'LabService': values.get('LabService', None),
            'Lab_Manage_Result': values.get('Lab_Manage_Result', None),
            'result_option': values.get('result_option', None),
            'Field_Manage_Result': values.get('Field_Manage_Result', None),
            'SampleCondition': values.get('SampleCondition2', None),
            'Remarks': values.get('Remarks', None),
            'DefaultContainerType': values.get('DefaultContainerType2', None),
        }
        analysis_request_3_dict = {
            'StorageLocation': values.get('StorageLocation3', None),
            'AdHoc': values.get('AdHoc3', None),
            'Template': values.get('Template3', None),
            'AnalysisProfile': values.get('AnalysisProfile3', None),
            'ClientSampleID': values.get('ClientSampleID2', None),
            'LotID': values.get('LotID3', None),
            'SubGroup': values.get('SubGroup3', None),
            'SampleType': values.get('SampleType3', None),
            'Batch': values.get('Batch2', None),
            'SamplingDeviation': values.get('SamplingDeviation3', None),
            'ResultsInterpretation': values.get('ResultsInterpretation', None),
            'Sample Partition': values.get('Sample Partition', None),
            'SamplePoint': values.get('SamplePoint3', None),
            'Specification': values.get('Specification3', None),
            'Priority': values.get('Priority3', None),
            'Partition': values.get('Partition', None),
            'SamplingDate': values.get('SamplingDate3', None),
            'ReportDryMatter': values.get('ReportDryMatter3', None),
            'Contact': values.get('Contact3', None),
            'FieldService': values.get('FieldService', None),
            'CCEmails': values.get('CCEmails3', None),
            'CCContact': values.get('CCContact3', None),
            'Sampler': values.get('Sampler3', None),
            'Composite': values.get('Composite3', None),
            'Sample_id': values.get('Sample_id3', None),
            'Analyses': values.get('Analyses', None),
            'Client': client,
            'InvoiceExclude': values.get('InvoiceExclude3', None),
            'LabService': values.get('LabService', None),
            'Lab_Manage_Result': values.get('Lab_Manage_Result', None),
            'result_option': values.get('result_option', None),
            'Field_Manage_Result': values.get('Field_Manage_Result', None),
            'SampleCondition': values.get('SampleCondition3', None),
            'Remarks': values.get('Remarks', None),
            'DefaultContainerType': values.get('DefaultContainerType3', None),
        }
        return analysis_request_0_dict, analysis_request_1_dict, analysis_request_2_dict, analysis_request_3_dict

    @api.multi
    def write(self, values):
        result_val_dict = {}
        if values.get("Analyses", None):
            for items in values.get("Analyses"):
                if items[0] == 0:
                    result_val_dict.update({
                            "Specifications":">"+str(items[2].get("Min", None))+", <"+str(items[2].get("Max", None))+", %"+str(items[2].get("Error", None)),
                            "Category": items[2].get("Category"),
                            'Due Date':datetime.datetime.now()
                            })
                    if items[2].get("Partition", None):
                        partition = self.env["olims.ar_partition"].search([("id", '=', items[2].get("Partition"))])
                        result_val_dict.update({"Partition": partition.Partition})
                    else:
                        result_val_dict.update({"Partition": 'P-0'+ str(self.id)+'-R-0'+str(self.id)})
                    if items[2].get("Services", None):
                        service = self.env["olims.analysis_service"].search([('id', '=', items[2].get("Services"))])
                        if service._Method and service.InstrumentEntryOfResults == False:
                            result_val_dict.update({'Method':service._Method.id})
                        elif service.InstrumentEntryOfResults:
                            result_val_dict.update({'Method':None, 'Instrument': service.Instrument})
                        if service.PointOfCapture == 'field':
                            result_val_dict.update({
                                'Service': items[2].get("Services"),
                                })
                            values.update({"Field_Manage_Result": [[0, False, result_val_dict]]})
                        else:
                            result_val_dict.update({
                                'LabService': items[2].get("Services"),
                                })
                            values.update({"Lab_Manage_Result": [[0, False, result_val_dict]]})
                if items[0] == 2:
                    pass
                if items[0] == 1:
                   pass
        res = super(AnalysisRequest, self).write(values)
        return res  

    @api.multi
    def publish_analysis_request(self):
        # self.filtered(lambda s: s.state == 'draft').write({'state': 'sent'})
        return self.env['report'].get_action(self, 'olims.report_analysis_request')

    def actionToBeSampled(self,cr,uid,ids,context=None):
        self.write(cr, uid, ids, {
            'state': 'to_be_sampled',
        }, context=context)
        return True

    def getSubtotalTotalPrice(self):
        """ Compute the price with VAT but no member discount"""
        return self.getSubtotal() + self.getSubtotalVATAmount()

    @api.onchange('LabService','FieldService')
    def _ComputeServiceCalculation(self):
        """
        It computes and returns the analysis service's discount amount without VAT, SubToatl and Total
        """
        for record in self:
            discount = 0.0
            vatamout = 0.0
            service_price = 0.0
            service_discount = 0.0
            service_subtotal = 0.0
            service_vat = 0.0
            service_total = 0.0
            if record.FieldService and record.LabService:
                for service in record.FieldService:

                    service_price = service.Service.Price

                    service_discount += service_price * 33.33 / 100

                    #compute subtotal
                    discount = service_price * 33.33 / 100
                    service_subtotal += float(service_price) - float(discount)

                    #compute VAT
                    service_vat += service.Service.VATAmount

                    service_total = service_subtotal + service_vat

                for service in record.LabService:

                    service_price = service.LabService.Price

                    service_discount += service_price * 33.33 / 100

                    #compute subtotal
                    discount = service_price * 33.33 / 100
                    service_subtotal += float(service_price) - float(discount)

                    #compute VAT
                    service_vat += service.LabService.VATAmount

                    service_total = service_subtotal + service_vat
                if record.Copyprofile == '1':
                    record.Discount = record.Discount1 = service_discount
                    record.Discount2 = record.Discount3 = None
                    record.Subtotal = record.Subtotal1 = service_subtotal
                    record.Subtotal2 = record.Subtotal3 = None
                    record.VAT = record.VAT1 = service_vat
                    record.VAT2 = record.VAT3 = None
                    record.Total = record.Total1 = service_total
                    record.Total2 = record.Total3 = None
                elif record.Copyprofile == '2':
                    record.Discount = record.Discount1 = record.Discount2 = service_discount
                    record.Discount3 = None
                    record.Subtotal = record.Subtotal1 = record.Subtotal2 = service_subtotal
                    record.Subtotal3 = None
                    record.VAT = record.VAT1 = record.VAT2 = service_vat
                    record.VAT3 = None
                    record.Total = record.Total1 = record.Total2 = service_total
                    record.Total3 = None
                elif record.Copyprofile == '3':
                    record.Discount = record.Discount1 = record.Discount2 = record.Discount3 = service_discount
                    record.Subtotal = record.Subtotal1 = record.Subtotal2 = record.Subtotal3 = service_subtotal
                    record.VAT = record.VAT1 = record.VAT2 = record.VAT3= service_vat
                    record.Total = record.Total1 = record.Total2 = record.Total3 = service_total
                else:
                    record.Discount = service_discount
                    record.Subtotal = service_subtotal
                    record.VAT = service_vat
                    record.Total = service_total
            elif record.FieldService or record.LabService:
                if record.FieldService:
                    for service in record.FieldService:

                        service_price = service.Service.Price

                        service_discount += service_price * 33.33 / 100

                        #compute subtotal
                        discount = service_price * 33.33 / 100
                        service_subtotal += float(service_price) - float(discount)

                        #compute VAT
                        service_vat += service.Service.VATAmount

                        service_total = service_subtotal + service_vat
                    if record.Copyprofile == '1':
                        record.Discount = record.Discount1 = service_discount
                        record.Discount2 = record.Discount3 = None
                        record.Subtotal = record.Subtotal1 = service_subtotal
                        record.Subtotal2 = record.Subtotal3 = None
                        record.VAT = record.VAT1 = service_vat
                        record.VAT2 = record.VAT3= None
                        record.Total = record.Total1 = service_total
                        record.Total2 = record.Total3 = None
                    elif record.Copyprofile == '2':
                        record.Discount = record.Discount1 = record.Discount2 = service_discount
                        record.Discount3 = None
                        record.Subtotal = record.Subtotal1 = record.Subtotal2 = service_subtotal
                        record.Subtotal3 = None
                        record.VAT = record.VAT1 = record.VAT2 = service_vat
                        record.VAT3 = None
                        record.Total = record.Total1 = record.Total2 = service_total
                        record.Total3 = None
                    elif record.Copyprofile == '3':
                        record.Discount = record.Discount1 = record.Discount2 = record.Discount3 = service_discount
                        record.Subtotal = record.Subtotal1 = record.Subtotal2 = record.Subtotal3 = service_subtotal
                        record.VAT = record.VAT1 = record.VAT2 = record.VAT3= service_vat
                        record.Total = record.Total1 = record.Total2 = record.Total3 = service_total
                    else:
                        record.Discount = service_discount
                        record.Subtotal = service_subtotal
                        record.VAT = service_vat
                        record.Total = service_total
                if record.LabService:
                    for service in record.LabService:
                        service_price = service.LabService.Price

                        service_discount += service_price * 33.33 / 100

                        #compute subtotal
                        discount = service_price * 33.33 / 100
                        service_subtotal += float(service_price) - float(discount)

                        #compute VAT
                        service_vat += service.LabService.VATAmount

                        service_total = service_subtotal + service_vat
                    if record.Copyprofile == '1':
                        record.Discount = record.Discount1 = service_discount
                        record.Discount2 = record.Discount3 = None
                        record.Subtotal = record.Subtotal1 = service_subtotal
                        record.Subtotal2 = record.Subtotal3 = None
                        record.VAT = record.VAT1 = service_vat
                        record.VAT2 = record.VAT3= None
                        record.Total = record.Total1 = service_total
                        record.Total2 = record.Total3 = None
                    elif record.Copyprofile == '2':
                        record.Discount = record.Discount1 = record.Discount2 = service_discount
                        record.Discount3 = None
                        record.Subtotal = record.Subtotal1 = record.Subtotal2 = service_subtotal
                        record.Subtotal3 = None
                        record.VAT = record.VAT1 = record.VAT2 = service_vat
                        record.VAT3 = None
                        record.Total = record.Total1 = record.Total2 = service_total
                        record.Total3 = None
                    elif record.Copyprofile == '3':
                        record.Discount = record.Discount1 = record.Discount2 = record.Discount3 = service_discount
                        record.Subtotal = record.Subtotal1 = record.Subtotal2 = record.Subtotal3 = service_subtotal
                        record.VAT = record.VAT1 = record.VAT2 = record.VAT3= service_vat
                        record.Total = record.Total1 = record.Total2 = record.Total3 = service_total
                    else:
                        record.Discount = service_discount
                        record.Subtotal = service_subtotal
                        record.VAT = service_vat
                        record.Total = service_total

    def getTotalPrice(self):
        """
        It gets the discounted price from analyses and profiles to obtain the total value with the VAT
        and the discount applied
        :return: the analysis request's total price including the VATs and discounts
        """
        for record in self:
            record.Total = record.Subtotal + record.VAT

    def isInvalid(self,cr,uid,ids,context=None):
        """ return if the Analysis Request has been invalidated
        """
        return self.write(cr, uid, ids, {
            'state': 'invalid',
        }, context=context)
        return True

    def workflow_script_receive(self,cr,uid,ids,context=None):
        analysis_request_obj = self.pool.get('olims.analysis_request').browse(cr,uid,ids,context)
        for ar_object in analysis_request_obj:
            data_list = []
            for items in ar_object.Analyses:
                analysis_dict = {}
                analysis_dict.update({
                    'category':items.Category.id,
                    'client': ar_object.Client.id,
                    'order':ar_object.LotID,
                    'priority':ar_object.Priority.id,
                    'due_date':ar_object.DateDue,
                    'received_date':datetime.datetime.now(),
                    'analysis':items.Services.id,
                    'sample_type': ar_object.SampleType.id
                    })
                data_list.append([0,0, analysis_dict])
            ar_object.write({'AddAnalysis': data_list})

        datereceived = datetime.datetime.now()
        self.write(cr, uid, ids, {
            'state': 'sample_received', 'DateReceived' : datereceived,
        }, context=context)
        return True

    def workflow_script_preserve(self,cr,uid,ids,context=None):
        self.write(cr, uid, ids, {
            'state': 'preserved',
        }, context=context)
        return True

    def workflow_script_sample(self,cr,uid,ids,context=None):
        self.write(cr, uid, ids, {
            'state': 'sampled',
        }, context=context)

        return True

    def workflow_script_to_be_preserved(self,cr,uid,ids,context=None):
        self.write(cr, uid, ids, {
            'state': 'to_be_preserved',
        }, context=context)
        return True

    def workflow_script_sample_due(self,cr,uid,ids,context=None):
        self.write(cr, uid, ids, {
            'state': 'sample_due', 'DateDue':datetime.datetime.now()
        }, context=context)
        return True

    def workflow_script_to_be_verified(self,cr,uid,ids,context=None):
        data_list = []
        for items in self.browse(cr,uid,ids,context):
            for objects in items.AddAnalysis:
                data_list.append([2, objects.id])

        self.write(cr, uid, ids, {
            'state': 'to_be_verified', 'AddAnalysis': data_list
        }, context=context)
        return True

    def workflow_script_verify(self):
        self.write({
            'state': 'verified',
        })
        return True

    def workflow_script_publish(self):
        datepublished = datetime.datetime.now()
        self.write({
            'state': 'published', 'DatePublished' : datepublished
        })
        return True

    def workflow_script_cancel(self,cr,uid,ids,context=None):
        self.write(cr, uid, ids,{
            'state': 'cancelled'
        },context)
        return True

    @api.multi
    @api.onchange("AnalysisProfile","AnalysisProfile1","AnalysisProfile2","AnalysisProfile3")
    def _add_values_in_analyses(self):
        self.LabService = None
        self.FieldService = None
        for record in self:
            for service in record.AnalysisProfile.Service:
                if service.Services.PointOfCapture == 'lab':
                    l_service = {'LabService':service.Services.id,
                        'Category':service.Services.category.id}
                    record.LabService += record.LabService.new(l_service)
                if service.Services.PointOfCapture == 'field':
                    f_service = {'Service':service.Services.id,
                        'Category':service.Services.category.id}
                    record.FieldService += record.FieldService.new(f_service)

    def bulk_change_states(self,state,cr,uid,ids,context=None):
        previous_state = ""
        if state == "sample_due":
            previous_state = "to_be_sampled"
        elif state == "sample_received":
            previous_state = "sample_due"
        requests = self.browse(cr,uid,ids)
        sample_ids = []
        for request in requests:
            if request.state != previous_state:
                ids.remove(request.id)
            else:
                sample_ids.append(request.Sample_id.id)
        self.browse(cr,uid,ids).signal_workflow(state)
        self.pool.get("olims.sample").browse(cr,uid,sample_ids).signal_workflow(state)
        return True

    @api.onchange('CopyContact')
    def copy_contact(self):
        if self.CopyContact == '1':
            self.Contact1 = self.Contact
            self.Contact2 = self.Contact3 = None
        elif self.CopyContact == '2':
            self.Contact1 = self.Contact2 = self.Contact
            self.Contact3 = None
        elif self.CopyContact == '3':
            self.Contact1 = self.Contact2 = self.Contact3 = self.Contact
        else:
            pass

    @api.onchange('CopyCCContact')
    def copy_cccontact(self):
        if self.CopyCCContact == '1':
            self.CCContact1 = self.CCContact
            self.CCContact2 = self.CCContact3 = None
        elif self.CopyCCContact == '2':
            self.CCContact1 = self.CCContact2 = self.CCContact
            self.CCContact3 = None
        elif self.CopyCCContact == '2':
            self.CCContact1 = self.CCContact2 = self.CCContact3 = self.CCContact
        else:
            pass

    @api.onchange('CopyEmail')
    def copy_email(self):
        if self.CopyEmail == '1':
            self.CCEmails1 = self.CCEmails
            self.CCEmails2 = self.CCEmails3 = None
        elif self.CopyEmail == '2':
            self.CCEmails1 = self.CCEmails2 = self.CCEmails
            self.CCEmails3 = None
        elif self.CopyEmail == '3':
            self.CCEmails1 = self.CCEmails2 = self.CCEmails3 = self.CCEmails
        else:
            pass

    @api.onchange('Copysample')
    def copy_sample(self):
        if self.Copysample == '1':
            self.Sample_id1 = self.Sample_id
            self.Sample_id2 = self.Sample_id3 = None
        elif self.Copysample == '2':
            self.Sample_id1 = self.Sample_id2 = self.Sample_id
            self.Sample_id3 = None
        elif self.Copysample == '3':
            self.Sample_id1 = self.Sample_id2 = self.Sample_id3 = self.Sample_id
        else:
            pass

    @api.onchange('Copybatch')
    def copy_batch(self):
        if self.Copybatch == '1':
            self.Batch1 = self.Batch
            self.Batch2 = self.Batch3 = None
        elif self.Copybatch == '2':
            self.Batch1 = self.Batch2 = self.Batch
            self.Batch3 = None
        elif self.Copybatch == '3':
            self.Batch1 = self.Batch2 = self.Batch3 = self.Batch
        else:
            pass
            

    @api.onchange('Copysubgroup')
    def copy_subgroup(self):
        if self.Copysubgroup == '1':
            self.SubGroup1 = self.SubGroup
            self.SubGroup2 = self.SubGroup3 = None
        elif self.Copysubgroup == '2':
            self.SubGroup1 = self.SubGroup2 = self.SubGroup
            self.SubGroup3 = None
        elif self.Copysubgroup == '3':
            self.SubGroup1 = self.SubGroup2 = self.SubGroup3 = self.SubGroup
        else:
            pass

    @api.onchange('Copytemplate')
    def copy_template(self):
        if self.Copytemplate == '1':
            self.Template1 = self.Template
            self.Template2 = self.Template3 = None
        elif self.Copytemplate == '2':
            self.Template1 = self.Template2 = self.Template
            self.Template3 = None
        elif self.Copytemplate == '3':
            self.Template1 = self.Template2 = self.Template3 = self.Template
        else:
            pass

    @api.onchange('Copyprofile')
    def copy_profile(self):
        if self.Copyprofile == '1':
            self.AnalysisProfile1 = self.AnalysisProfile
            self.AnalysisProfile2 = self.AnalysisProfile3 = None
        elif self.Copyprofile == '2':
            self.AnalysisProfile1 = self.AnalysisProfile2 = self.AnalysisProfile
            self.AnalysisProfile3 = None
        elif self.Copyprofile == '3':
            self.AnalysisProfile1 = self.AnalysisProfile2 = self.AnalysisProfile3 = self.AnalysisProfile
        else:
            pass

    @api.onchange('Copysmaplingdate')
    def copy_sampledate(self):
        if self.Copysmaplingdate == '1':
            self.SamplingDate1 = self.SamplingDate
            self.SamplingDate2 = self.SamplingDate3 = None
        elif self.Copysmaplingdate == '2':
            self.SamplingDate1 = self.SamplingDate2 = self.SamplingDate
            self.SamplingDate3 = None
        elif self.Copysmaplingdate == '3':
            self.SamplingDate1 = self.SamplingDate2 = self.SamplingDate3 = self.SamplingDate
        else:
            pass

    @api.onchange('Copysampler')
    def copy_sampler(self):
        if self.Copysampler == '1':
            self.Sampler1 = self.Sampler
            self.Sampler2 = self.Sampler3 = None
        elif self.Copysampler == '2':
            self.Sampler1 = self.Sampler2 = self.Sampler
            self.Sampler3 = None
        elif self.Copysampler == '3':
            self.Sampler1 = self.Sampler2 = self.Sampler3 = self.Sampler
        else:
            pass

    @api.onchange('Copysampletype')
    def copy_sample_type(self):
        if self.Copysampletype == '1':
            self.SampleType1 = self.SampleType
            self.SampleType2 = self.SampleType3 = None
        elif self.Copysampletype == '2':
            self.SampleType1 = self.SampleType2 = self.SampleType
            self.SampleType3 = None
        elif self.Copysampletype == '3':
            self.SampleType1 = self.SampleType2 = self.SampleType3 = self.SampleType
        else:
            pass

    @api.onchange('Copyspecification')
    def copy_specification(self):
        if self.Copyspecification == '1':
            self.Specification1 = self.Specification
            self.Specification2 = self.Specification3 = None
        elif self.Copyspecification == '2':
            self.Specification1 = self.Specification2 = self.Specification
            self.Specification3 = None
        elif self.Copyspecification == '3':
            self.Specification1 = self.Specification2 = self.Specification3 = self.Specification
        else:
            pass

    @api.onchange('Copysamplepoint')
    def copy_sample_point(self):
        if self.Copysamplepoint == '1':
            self.SamplePoint1 = self.SamplePoint
            self.SamplePoint2 = self.SamplePoint3 = None
        elif self.Copysamplepoint == '2':
            self.SamplePoint1 = self.SamplePoint2 = self.SamplePoint
            self.SamplePoint3 = None
        elif self.Copysamplepoint == '3':
            self.SamplePoint1 = self.SamplePoint2 = self.SamplePoint3 = self.SamplePoint
        else:
            pass


    @api.onchange('Copystorage')
    def copy_storage_location(self):
        if self.Copystorage == '1':
            self.StorageLocation1 = self.StorageLocation
            self.StorageLocation2 = self.StorageLocation3 = None
        elif self.Copystorage == '2':
            self.StorageLocation1 = self.StorageLocation2 = self.StorageLocation
            self.StorageLocation3 = None
        elif self.Copystorage == '3':
            self.StorageLocation1 = self.StorageLocation2 = self.StorageLocation3 = self.StorageLocation
        else:
            pass

    @api.onchange('CopyLotID')
    def copy_client_order_num(self):
        if self.CopyLotID == '1':
            self.LotID1 = self.LotID
            self.LotID2 = self.LotID3 = None
        elif self.CopyLotID == '2':
            self.LotID1 = self.LotID2 = self.LotID
            self.LotID3 = None
        elif self.CopyLotID == '3':
            self.LotID1 = self.LotID2 = self.LotID3 = self.LotID
        else:
            pass


    @api.onchange('CopyClientReference')
    def copy_client_reference(self):
        if self.CopyClientReference == '1':
            self.ClientReference1 = self.ClientReference
            self.ClientReference2 = self.ClientReference3 = None
        elif self.CopyClientReference == '2':
            self.ClientReference1 = self.ClientReference2 = self.ClientReference
            self.ClientReference3 = None
        elif self.CopyClientReference == '3':
            self.ClientReference1 = self.ClientReference2 = self.ClientReference3 = self.ClientReference
        else:
            pass


    @api.onchange('CopyClientSampleID')
    def copy_client_sample_id(self):
        if self.CopyClientSampleID == '1':
            self.ClientSampleID1 = self.ClientSampleID
            self.ClientSampleID2 = self.ClientSampleID3 = None
        elif self.CopyClientSampleID == '2':
            self.ClientSampleID1 = self.ClientSampleID2 = self.ClientSampleID
            self.ClientSampleID3 = None
        elif self.CopyClientSampleID == '3':
            self.ClientSampleID1 = self.ClientSampleID2 = self.ClientSampleID3 = self.ClientSampleID
        else:
            pass

    @api.onchange('CopySamplingDeviation')
    def copy_sampling_deviation(self):
        if self.CopySamplingDeviation == '1':
            self.SamplingDeviation1 = self.SamplingDeviation
            self.SamplingDeviation2 = self.SamplingDeviation3 = None
        elif self.CopySamplingDeviation == '2':
            self.SamplingDeviation1 = self.SamplingDeviation2 = self.SamplingDeviation
            self.SamplingDeviation3 = None
        elif self.CopySamplingDeviation == '3':
            self.SamplingDeviation1 = self.SamplingDeviation2 = self.SamplingDeviation3 = self.SamplingDeviation
        else:
            pass

    @api.onchange('CopySampleCondition')
    def copy_sample_condition(self):
        if self.CopySampleCondition == '1':
            self.SampleCondition1 = self.SampleCondition
            self.SampleCondition2 = self.SampleCondition3 = None
        elif self.CopySampleCondition == '2':
            self.SampleCondition1 = self.SampleCondition2 = self.SampleCondition
            self.SampleCondition3 = None
        elif self.CopySampleCondition == '3':
            self.SampleCondition1 = self.SampleCondition2 = self.SampleCondition3 = self.SampleCondition
        else:
            pass

    @api.onchange('CopyDefaultContainerType')
    def copy_container_type(self):
        if self.CopyDefaultContainerType == '1':
            self.DefaultContainerType1 = self.DefaultContainerType
            self.DefaultContainerType2 = self.DefaultContainerType3 = None
        elif self.CopyDefaultContainerType == '2':
            self.DefaultContainerType1 = self.DefaultContainerType2 = self.DefaultContainerType
            self.DefaultContainerType3 = None
        elif self.CopyDefaultContainerType == '3':
            self.DefaultContainerType1 = self.DefaultContainerType2 = self.DefaultContainerType3 = self.DefaultContainerType
        else:
            pass


    @api.onchange('CopyAdHoc')
    def copy_adhoc(self):
        if self.CopyAdHoc == '1':
            self.AdHoc1 = self.AdHoc
            self.AdHoc2 = self.AdHoc3 = False
        elif self.CopyAdHoc == '2':
            self.AdHoc1 = self.AdHoc2 = self.AdHoc
            self.AdHoc3 = False
        elif self.CopyAdHoc == '3':
            self.AdHoc1 = self.AdHoc2 = self.AdHoc3 = self.AdHoc
        else:
            pass

    @api.onchange('CopyComposite')
    def copy_composite(self):
        if self.CopyComposite == '1':
            self.Composite1 = self.Composite
            self.Composite2 = self.Composite3 = False
        elif self.CopyComposite == '2':
            self.Composite1 = self.Composite2 = self.Composite
            self.Composite3 = False
        elif self.CopyComposite == '3':
            self.Composite1 = self.Composite2 = self.Composite3 = self.Composite
        else:
            pass

    @api.onchange('CopyReportDryMatter')
    def copy_report_dry_matter(self):
        if self.CopyReportDryMatter == '1':
            self.ReportDryMatter1 = self.ReportDryMatter
            self.ReportDryMatter2 = self.ReportDryMatter3 = False
        elif self.CopyReportDryMatter == '2':
            self.ReportDryMatter1 = self.ReportDryMatter2 = self.ReportDryMatter
            self.ReportDryMatter3 = False
        elif self.CopyReportDryMatter == '3':
            self.ReportDryMatter1 = self.ReportDryMatter2 = self.ReportDryMatter3 = self.ReportDryMatter
        else:
            pass

    @api.onchange('CopyInvoiceExclude')
    def copy_invoice_exclude(self):
        if self.CopyInvoiceExclude == '1':
            self.InvoiceExclude1 = self.InvoiceExclude
            self.InvoiceExclude2 = self.InvoiceExclude3 = False
        elif self.CopyInvoiceExclude == '2':
            self.InvoiceExclude1 = self.InvoiceExclude2 = self.InvoiceExclude
            self.InvoiceExclude3 = False
        elif self.CopyInvoiceExclude == '3':
            self.InvoiceExclude1 = self.InvoiceExclude2 = self.InvoiceExclude3 = self.InvoiceExclude
        else:
            pass

    @api.onchange('CopyPriority')
    def copy_priority(self):
        if self.CopyPriority == '1':
            self.Priority1 = self.Priority
            self.Priority2 = self.Priority3 = None
        elif self.CopyPriority == '2':
            self.Priority1 = self.Priority2 = self.Priority
            self.Priority3 = None
        elif self.CopyPriority == '3':
            self.Priority1 = self.Priority2 = self.Priority3 = self.Priority
        else:
            pass

    @api.multi
    def action_report_send(self):
        '''
        This function opens a window to compose an email, with the edi sale template message loaded by default
        '''
        self.ensure_one()
        ir_model_data = self.env['ir.model.data']
        try:
            template_id = ir_model_data.get_object_reference('olims', 'email_template_edi_ar')[1]
        except ValueError:
            template_id = False
        try:
            compose_form_id = ir_model_data.get_object_reference('mail', 'email_compose_message_wizard_form')[1]
        except ValueError:
            compose_form_id = False
        ctx = dict()
        ctx.update({
            'default_model': 'olims.analysis_request',
            'default_res_id': self.ids[0],
            'default_use_template': bool(template_id),
            'default_template_id': template_id,
            'default_composition_mode': 'comment',
            'mark_so_as_sent': True
        })
        return {
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(compose_form_id, 'form')],
            'view_id': compose_form_id,
            'target': 'new',
            'context': ctx,
        }

class FieldAnalysisService(models.Model, BaseOLiMSModel):
    _name = 'olims.field_analysis_service'

    @api.onchange('Service','LabService')
    def _ComputeFieldResults(self):
        for item in self:
            if item.Service:
                item.CommercialID = item.Service.CommercialID
                item.ProtocolID  = item.Service.ProtocolID
            if item.LabService:
                item.CommercialID = item.LabService.CommercialID
                item.ProtocolID  = item.LabService.ProtocolID

class ManageAnalyses(models.Model, BaseOLiMSModel):
    _inherit = 'olims.field_analysis_service'
    _name = 'olims.manage_analyses'

    @api.multi
    def bulk_verify(self):
        ar_ids = []
        for record in self:
            if not record.Result:
                continue
            record.write({"state":"to_be_verified"})
            if len(record.Service) != 0:
                analysis_id = record.Service.id
                request_id = record.manage_analysis_id.id
            else:
                analysis_id = record.LabService.id
                request_id = record.lab_manage_analysis_id.id
            analyses = self.env["olims.ws_manage_results"].search([
                ("analysis","=",analysis_id),
                ("request_analysis_id","=",request_id)
                ])
            for analysis in analyses:
                analysis.write({"state":"to_be_verified","result":record.Result})
            arecs = self.env["olims.manage_analyses"].search([
                "|",("manage_analysis_id","=",request_id),
                    ("lab_manage_analysis_id","=",request_id)
                ])
            all_submitted = True
            for arec in arecs:
                if arec.state != "to_be_verified":
                    all_submitted = False
                    break
            if all_submitted:
                ar_ids.append(request_id)
        self.env["olims.analysis_request"].browse(ar_ids).signal_workflow("submit")
        return True


AnalysisRequest.initialze(schema)
FieldAnalysisService.initialze(schema_analysis)
ManageAnalyses.initialze(manage_result_schema)

