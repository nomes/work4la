# -*- coding: utf-8 -*-
import colander


class SubscribeSchema(colander.MappingSchema):
    email = colander.SchemaNode(colander.String(),
                                validator=colander.Email())
    job_id = colander.SchemaNode(colander.Integer(),
                                 validator=colander.Range(min=0, max=None))
