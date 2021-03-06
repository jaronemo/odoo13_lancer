# -*- coding: utf-8 -*-
# Author: Jason Wu (jaronemo@msn.com)

from odoo import api, fields, models


class LancerRoutingMaterial(models.Model):
    _name = 'lancer.routing.material'
    _rec_name = 'name'
    _description = 'Lancer Routing Material Item'

    name = fields.Char(string='組裝-材料名稱')
    active = fields.Boolean(default=True, string='是否啟用')
    sequence = fields.Integer(required=True, default=10)
