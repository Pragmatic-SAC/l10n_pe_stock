# -*- coding: utf-8 -*-
{
    # App information
    "name": "Localization Inventory - Peru",
    "category": "Localization",
    "summary": "Base module containing common models localization Peru.",
    "version": "14.0.0",
    "license": "OPL-1",
    "website": "https://www.pragmatic.com.pe/",
    "contributors": [
        "Kelvin Meza <kmeza@pragmatic.com.pe>",
    ],
    "depends": [
        "l10n_pe_conf", "stock"
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/type_of_operation_sunat_table_12.xml",
        "views/stock_picking.xml",
        "views/stock_picking_type.xml",
        "views/stock_scrap.xml",
        "views/stock_inventory.xml",
    ],
    # Odoo Store Specific
    "images": [

    ],

    # Author
    "author": "Pragmatic S.A.C",
    "website": "pragmatic.com.pe",
    "maintainer": "Pragmatic S.A.C.",

    # Technical
    "installable": True,
    "auto_install": False,
    "application": True,
    "currency": "PEN",
}
