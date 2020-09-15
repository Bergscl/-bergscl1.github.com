# -*- coding: utf-8 -*-

from BeautifulReport import BeautifulReport
import unittest
import main
import sys
import testError

class TestFunction(unittest.TestCase):
	@classmethod
	def setUp(self):
		print("开始测试")
	@classmethod
	def tearDown(self):
		print("测试结束")
		
	def text_self(self):
		print("正在读取orig.txt")
		a = main.SimilarityMethod(r'sim_0.8\orig.txt', r'sim_0.8\orig.txt')
		print('%.2f'%a.JaccardSim(a.str_a,a.str_b))

	def text_add(self):
		print("正在读取orig_0.8_add.txt")
		a = main.SimilarityMethod(r'sim_0.8\orig.txt', r'sim_0.8\orig_0.8_add.txt')
		print('%.2f'%a.JaccardSim(a.str_a,a.str_b))

	def text_del(self):
		print("正在读取orig_0.8_del.txt")
		a = main.SimilarityMethod(r'sim_0.8\orig.txt', r'sim_0.8\orig_0.8_del.txt')
		print('%.2f'%a.JaccardSim(a.str_a,a.str_b))
		
	def text_dis_1(self):
		print("正在读取orig_0.8_dis_1.txt")
		a = main.SimilarityMethod(r'sim_0.8\orig.txt', r'sim_0.8\orig_0.8_dis_1.txt')
		print('%.2f'%a.JaccardSim(a.str_a,a.str_b))
		
	def text_dis_3(self):
		print("正在读取orig_0.8_dis_3.txt")
		a = main.SimilarityMethod(r'sim_0.8\orig.txt', r'sim_0.8\orig_0.8_dis_3.txt')
		print('%.2f'%a.JaccardSim(a.str_a,a.str_b))
		
	def text_dis_7(self):
		print("正在读取orig_0.8_dis_7.txt")
		a = main.SimilarityMethod(r'sim_0.8\orig.txt', r'sim_0.8\orig_0.8_dis_7.txt')
		print('%.2f'%a.JaccardSim(a.str_a,a.str_b))	
			
	def text_dis_10(self):
		print("正在读取orig_0.8_dis_10.txt")
		a = main.SimilarityMethod(r'sim_0.8\orig.txt', r'sim_0.8\orig_0.8_dis_10.txt')
		print('%.2f'%a.JaccardSim(a.str_a,a.str_b))
		
	def text_dis_15(self):
		print("正在读取orig_0.8_dis_15.txt")
		a = main.SimilarityMethod(r'sim_0.8\orig.txt', r'sim_0.8\orig_0.8_dis_15.txt')
		print('%.2f'%a.JaccardSim(a.str_a,a.str_b))
				
	def text_mix(self):
		print("正在读取orig_0.8_mix.txt")
		a = main.SimilarityMethod(r'sim_0.8\orig.txt', r'sim_0.8\orig_0.8_mix.txt')
		print('%.2f'%a.JaccardSim(a.str_a,a.str_b))
		
	def text_rep(self):
		print("正在读取orig_0.8_rep.txt")
		a = main.SimilarityMethod(r'sim_0.8\orig.txt', r'sim_0.8\orig_0.8_rep.txt')
		print('%.2f'%a.JaccardSim(a.str_a,a.str_b))


if __name__ == '__main__':
	tests = unittest.TestSuite()
	tests.addTest(TestFunction('text_self'))
	tests.addTest(TestFunction('text_add'))
	tests.addTest(TestFunction('text_del'))
	tests.addTest(TestFunction('text_dis_1'))
	tests.addTest(TestFunction('text_dis_3'))
	tests.addTest(TestFunction('text_dis_7'))
	tests.addTest(TestFunction('text_dis_10'))
	tests.addTest(TestFunction('text_dis_15'))
	tests.addTest(TestFunction('text_mix'))
	tests.addTest(TestFunction('text_rep'))
	runner = BeautifulReport(tests)  
	runner.report(
    description='Similarity测试报告',  # => 报告描述
    filename='texts.html',  # => 生成的报告文件名
    log_path='.'  # => 报告路径
)
