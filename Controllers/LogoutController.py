from flask_script import Option
from Library.Controller import Controller
from Services.KahlaAuthApiService import KahlaAuthApiService
from Services.StorageCookieService import StorageCookieService
from Services.KahlaSignInStatusCheckService import KahlaSignInStatusCheckService
import json
import os

class LogoutController(Controller):
	def __init__(self):
		self.checksignstatus = KahlaSignInStatusCheckService()

	# 定义参数
	def get_options(self):
		return []

	# 处理输入参数, 检查合法性
	def run(self):
		# 这条必须编写, 并且带上传入的参数
		self.compute()

	# 处理业务逻辑
	def main(self):
		if self.checksignstatus.check() == True:
			try:
				os.remove("./user.cookie.bin")
				return ""
			except:
				return "You are not logged in!"
		else:
			return "You are not logged in!"