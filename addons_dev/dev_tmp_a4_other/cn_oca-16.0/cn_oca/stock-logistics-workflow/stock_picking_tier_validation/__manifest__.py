# Copyright 2021 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Stock Picking Tier Validation",
    "summary": "Extends the functionality of Transfers to "
    "support a tier validation process.",
    "version": "16.0.0.0.0",
    "category": "Warehouse Management",
    "website": "https://github.com/OCA/stock-logistics-workflow",
    "author": "Ecosoft, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "depends": ["stock", "base_tier_validation", "stock_picking_batch"],
    "data": ["views/stock_picking_views.xml"],
    "installable": True,
    "development_status": "Alpha",
}
