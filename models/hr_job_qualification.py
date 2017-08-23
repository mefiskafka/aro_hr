# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __openerp__.py file at the root folder of this module.                   #
###############################################################################

from openerp import models, fields, api
from openerp.tools.translate import _
from logging import getLogger


_logger = getLogger(__name__)




class HrJobQualification(models.Model):
    """ The summary line for a class docstring should fit on one line.

    Fields:
      name (Char): Human readable name which will identify each record.

    """

    _name = 'hr.job.qualification'
    _description = u'Hr job qualification'

    _rec_name = 'name'
    _order = 'name ASC'

    name = fields.Many2one(string='qual.type', 'Qualification Requise')
    branche_id = fields.Many2one(string='hr.employee.branche', 'Branche')
    specialite = fields.Char('Specialite', size=64)
    job_id = fields.Many2one(string='hr.job', 'Poste')


