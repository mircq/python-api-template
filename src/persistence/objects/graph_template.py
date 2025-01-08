from neomodel import config, AsyncStructuredNode, StringProperty, IntegerProperty, UniqueIdProperty, RelationshipTo


class Template(AsyncStructuredNode):
	""" """

	id = UniqueIdProperty()
	description = StringProperty(required=True)
