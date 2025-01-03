"""From https://refactoring.guru/design-patterns/singleton/python/example"""


class Singleton(type):
	"""Metaclass used to define singleton pattern."""

	_instances = {}

	def __call__(cls, *args, **kwargs):
		if cls not in cls._instances:
			instance = super().__call__(*args, **kwargs)
			cls._instances[cls] = instance
		return cls._instances[cls]
