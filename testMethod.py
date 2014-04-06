class TestCase:
	def __init__(self, name):
		self.name = name
	def setUp(self):
		pass
	def run(self):
		self.setUp()
		method = getattr(self, self.name)
		method()

class WasRun(TestCase):
	def __init__(self, name):
		TestCase.__init__(self, name)
	def testMethod(self):
		self.wasRun= 1
		self.log = self.log + "testMethod "
	def setUp(self):
		self.wasRun= None
		self.log = "setUp "

class TestCaseTest(TestCase):
	def testTemplateMethod(self):
		test = WasRun("testMethod")
		test.run()
		assert("setUp testMethod " == test.log)

TestCaseTest("testTemplateMethod").run()
