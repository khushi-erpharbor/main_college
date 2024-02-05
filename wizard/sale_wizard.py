from odoo import fields, models


class Sale(models.TransientModel):
    _name = "sale.sale"
    _description = "sale"

    product_template_id = fields.Many2one("product.template",string="Product")

    def action_submit_stud(self):
        print("Content:::::::::::",self.env.context)
        ctx = self.env.context
        print("ctx",ctx.get('active_id'),ctx.get('active_model'))
        sale_id = self.env['sale.order'].browse(ctx.get('active_id'))
        print("::::::::::::::::::::::::::;",sale_id)
        # model=self.env.context.get('active_model')
        # ids=self.env.context.get('active_id')
        # record=self.env[model].browse(ids)
        # print(record,"                     ------               ")
        # record={"product_template_id":self.product_template_id.id}
        # print("\n\n\n\n\n\n\n\nreorcs::::::::::::::::::::::::::::",record)
        # result = record.update({
        #     'order_line': [(fields.Command.create({"product_template_id":self.product_template_id.id }))]
        # })
        # print(result)

    # def action_cancel(self):
    #     print('\n\n1111111111111111111')
    #     print('\n\nCONTEXT', self.env.context)
    #     ctx = self.env.context
    #     print('ctx', ctx.get('active_id'), ctx.get('active_model'))
    #     student_id = self.env['college.student'].browse(ctx.get('active_id'))
    #     print("\n\n\n",student_id)
    #     student_id.cancellation_reason = self.name
                                                           
