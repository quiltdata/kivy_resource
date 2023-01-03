from kivy_resource.main import MainApp
from .conftest import *

class AppTest(GraphicUnitTest):

	def test_runtouchapp(self):
		# non-integrated approach
		from kivy.app import runTouchApp
		from kivy.uix.button import Button

		button = Button()
		runTouchApp(button)

		# get your Window instance safely
		from kivy.base import EventLoop
		EventLoop.ensure_window()
		window = EventLoop.window

		# your asserts
		self.assertEqual(window.children[0], button)
		self.assertEqual(
			window.children[0].height,
			window.height
		)


	def untest_app(self):
		app = MainApp()
		assert app