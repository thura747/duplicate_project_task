# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-today OpenERP SA (<http://www.openerp.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp.osv import fields, osv


class Task(osv.osv):
    _inherit = "project.task"
    _description = "Task"

    def copy(self, cr, uid, ids, default=None, context=None):
        vals = {
            'partner_id':       False,
            'date_end':         False,
            'date_deadline':    False,
            'categ_ids':        [(2, id)],
            'categ_ids':        [(3, id)],
            'categ_ids':        [(5, id)],
            'description':      False,
            'priority':         False,
            'date_last_stage_update': False,
        }
        return super(Task, self).copy(cr, uid, ids, vals, context=context)
