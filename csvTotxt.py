#encoding:utf-8
import csv
from string import Template

def load_csv(file):
	with open(file,'r') as csv_file:
		reader = csv.reader(csv_file)
		head_row = next(reader)
		each_cases = []
		for row in reader:
			each_case = {}
			for index in range(len(head_row)):
				each_case[head_row[index]] = row[index]
			each_cases.append(each_case)
		return each_cases

def load_template(temp):
	with open(temp,'r') as demo:
		str = demo.read()
		return str

def write_txt(string,features):
	for feature in features:
		tem = Template(string)
		feature_name = feature['name']+'.feature'
		print "feature name is "+ feature_name
		content = tem.substitute(feature)
		with open("features/"+feature_name,'w') as f:
			f.write(content)

def main():
	inputfile = "csv/data.csv"
	template = "template/template.txt"
	#read csv
	features =load_csv(inputfile)
	# convert txt to string
	template_str = load_template(template)
	#write txt
	write_txt(template_str,features)

if __name__ == '__main__':
	main()