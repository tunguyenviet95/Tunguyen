from odoo import api, fields, models


class Rooms(models.Model):
    _name = 'rooms'
    _rec_name = 'room_code'

    room_avatar = fields.Binary(string='Image')
    room_code = fields.Char(string='Mã Phòng')
    room_type = fields.Selection(selection=[('standard', 'Standard'),
                                            ('superior', 'Superior'),
                                            ('deluxe', 'Deluxe'),
                                            ('suite', 'Suite')],
                                 string='Type Room', default='superior')
    room_state = fields.Selection(selection=[('available', 'Available'),
                                             ('confirmed', 'Confirmed'),
                                             ('operational', 'Operational')],
                                  string='State', default='available')
    price_room = fields.Float(string='Price')
    room_description = fields.Text(string='Description')
    wifi = fields.Boolean('Wifi')
    air_conditioned = fields.Boolean('Air Conditioned')
    alarm_clock = fields.Boolean('Alarm Clock')
    Bathtub = fields.Boolean('Bathtub')
    coffeemaker = fields.Boolean('Coffeemaker')
    Connecting_Rooms = fields.Boolean('Connecting Rooms')
    Free_Newspaper = fields.Boolean('Free Newspaper')
    Hairdryer_In_Room = fields.Boolean('Hairdryer In Room')
    High_Speed_Internet = fields.Boolean('High Speed Internet')
    Iron = fields.Boolean('Iron')
    Ironing_Board = fields.Boolean('Ironing Board')
    Lake_View = fields.Boolean('Lake View')
    Modem_in_Room = fields.Boolean('Modem in Room')
    Shower = fields.Boolean('Shower')
    Telephone = fields.Boolean('Telephone')
    Toilet = fields.Boolean('Toilet')
    Turndown_Service = fields.Boolean('Turndown Service')
    TV = fields.Boolean('TV')
    WC = fields.Boolean('WC')
    booking_id = fields.Many2one(comodel_name='booking', string='Booking')

    @api.depends('booking_id')
    def change_state(self):
        for i in self:
            if i.booking_id:
                i.room_state = 'confirmed'
            else:
                i.room_state = 'available'

    def avalable_change(self):
        self.room_state = 'available'

    def confirm_change(self):
        self.room_state = 'confirmed'

    def operational_change(self):
        self.room_state = 'operational'

