from odoo import models, fields, api
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class Booking(models.Model):
    _name = 'booking'
    _rec_name = 'id'

    check_in = fields.Date(string='Check-in', default=datetime.today())
    check_out = fields.Date(string='Check-out')
    amount_adult = fields.Integer(string='Adult')
    amount_child = fields.Integer(string='Child ')
    cost = fields.Float(compute='_calculate_cost', string='Cost')
    service = fields.Many2many(comodel_name='service', string='Service')
    promotion = fields.Many2one(comodel_name='promotion', string='Promotion')
    room_ids = fields.One2many(comodel_name='rooms', inverse_name='booking_id', string='Rooms')

    def _calculate_cost(self):
        for booking in self:
            total = 0
            if booking.service:
                for service in booking.service:
                    total += service.price
            if booking.room_ids:
                for price in booking.room_ids:
                    total += price.price_room
            if booking.promotion:
                total = total - total * booking.promotion.promotion
            booking.cost = total

    def confirm_button(self):
        self.room_ids.write({'room_state': 'operational'})



    # def write(self,vals):
    #     if "room_ids" in vals:
    #         logging.info('room ids: %s' % vals['room_ids'])
    #         change_room_by_booking(room_ids)
    # #
    # #def create(self,vals):
    #     #call function to change room here!
    #     #self.change_room_by_booking(room_ids)
    #
    # def change_room_by_booking(self,room_ids):
    #     #change room here!
    #     for room in self.room_ids:
    #         room_ids = room.write({'room_state':'confirmed'})
    #     return super(booking, self).write(room_ids)