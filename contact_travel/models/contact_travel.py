from odoo import _,api,fields, models

class Voyage(models.Model):
    _name = 'voyage'  #model name here
    _description = 'Voyage'

    name = fields.Char(string="Nom de voyage",required=True)
    departureDate = fields.Date(string="Date de départ")
    returnDate = fields.Date(string="Date de retour")
    destination = fields.Char(string="Destination")
    currency_id = fields.Many2one('res.currency',string="Devise",default=lambda self: self.env.user.company_id.currency_id,readonly=True) #used to show monetary fields currency corresponds to the current user company currency 
    price  = fields.Monetary(string="Prix de voyage",required=True) #monetary field is used instead of integer,helps with currency
    partner_id = fields.Many2one('res.partner',string="Contact",required=True) #used many2one field so that 1 'voyage' is defined for only 1 user

class Partner(models.Model):
    _inherit = "res.partner" #inherit the odoo native model res_parnter

    count_travels = fields.Integer(compute="_compute_count_travels") #this helps to find the number of travels for that user
    
    rec_levels = fields.Selection(selection=[
        ('silver','Argent'),
        ('gold','Or'),
        ('platinium','Platine')
    ],
    string="Niveaux de récompense",
    default="silver",
    required=True,
    compute="_compute_rec_levels"
    )


    currency_id = fields.Many2one('res.currency',string="Devise",default=lambda self: self.env.user.company_id.currency_id,readonly=True)
    total_despense = fields.Monetary(string="Total dépensé",compute="_compute_total_depense") #this field is created and used to compute the rec_levels 


    def _compute_total_depense(self): #this will compute the sum of each voyage assossiated to the partner
        for rec in self:
            total = 0.0
            travels = self.env['voyage'].search([('partner_id','=',rec.id)]) #this will get all the voyage objects which partner_id equals to this partner
            for travel in travels :
                total += travel.price
            rec.total_despense = total

    @api.depends('total_despense') #rec_levels values are depending on total_despense
    def _compute_rec_levels(self):  #this will put the value of rec_levels depends on total_despense value
       for rec in self:
            if rec.total_despense < 5000 :
                rec.rec_levels = 'silver'
            elif rec.total_despense >= 5000 and rec.total_despense < 10000 :
                rec.rec_levels = 'gold'
            elif rec.total_despense >= 10000 :
                rec.rec_levels = 'platinium'

    def _compute_count_travels(self): #compute number of voyage records that belongs to this partner
        for rec in self :
            travels = self.env['voyage'].search([('partner_id','=',self.id)])
            self.count_travels = len(travels)    #len(travels) return the number of records found in travels

    def get_voyages(self): #Calling this function in the view will redirect the user to voyage model showing only records which partner_id equals to this partner
        domain= [("partner_id", "=", self.id)]
        return {
                    'name': _('Voyage'),
                    'domain':domain,
                    'view_mode': 'tree,form',
                    'res_model': 'voyage',
                    'type': 'ir.actions.act_window',
                }
    