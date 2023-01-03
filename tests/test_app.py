from kivy_resource.main import MainApp
from .conftest import *

class AppTest(GraphicUnitTest):

	def test_app(self):
		app = MainApp()
		assert app