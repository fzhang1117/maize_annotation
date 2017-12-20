## auto annotation ##
## 2016-01-23 ## 
## zhangfei ##
## Run in Command Line Model, Give the input and output path you want ##
## reconsitution: 2017-04-19 ##

import sys
FH_anno = open(sys.argv[1], 'r')
FH_query = open(sys.argv[2], 'r')
FH_output = open(sys.argv[3], 'a')

def anno_dicbuild():
	anno_dic = {}
	for line in FH_anno:
		line = line.strip('\n')
		line = line.split('\t')
		anno_dic[line[2]] = line
	return anno_dic

anno_dic = anno_dicbuild()
#print anno_dic

output_title = ['query','LocusName','transcriptName','best-hit-in-Arabidopsis','Arabidopsis-defline']
FH_output.writelines('\t'.join(output_title))
FH_output.writelines('\n')
for line in FH_query:
	line = line.strip('\r\n')
	if line[:2] == 'GR':
		line = list(line)
		transcript = line + ['_','T','0','1']
		transcript = ''.join(transcript)
		if anno_dic.get(transcript) != None:
			value = [anno_dic[transcript][10], anno_dic[transcript][12]]
			output = [''.join(line), transcript] + value
			FH_output.writelines('\t'.join(output))
			FH_output.writelines('\n')
		else:
			output = [''.join(line), transcript, '', '']
			FH_output.writelines('\t'.join(output))
			FH_output.writelines('\n')
			print transcript, ' was not found!'
	else:
		line = list(line)
		transcript = line[:13] + ['T'] + line[13:]
		transcript = ''.join(transcript)
		if anno_dic.get(transcript) != None:
			value = [anno_dic[transcript][10], anno_dic[transcript][12]]
			output = [''.join(line), transcript] + value
			FH_output.writelines('\t'.join(output))
			FH_output.writelines('\n')
		else:
			output = [''.join(line), transcript, '', '']
			FH_output.writelines('\t'.join(output))
			FH_output.writelines('\n')
			print transcript, ' was not found!'

FH_anno.close()
FH_query.close()
FH_output.close()
# older version: 2016-01-23
"""
import re,sys
annofile=open(sys.argv[1],'r')# An Annotation File, Format as photozome annotation #
queryfile=open(sys.argv[2],'r')#An Query File, One item in One Line#
output=open(sys.argv[3],'a')#Output File you want#
title='query','\t','LocusName','\t','transciptName','\t','best-hit-in-Arabidopsis','\t','Arabidopsis-defline','\n'
output.writelines(title)
def dicbuild(filehand):
    dic={}
    for line in filehand:
        storage=line.split('\t')
        dic[storage[2]]=storage
    return dic

def writeanno(filehand):
    for line in filehand:
        query=line.strip('\n')
        m=re.compile(query)
        for key in dic.keys():
               if m.match(str(key)):
                   data=dic.get(key)
                   string=query,'\t',data[1],'\t',key,'\t',data[10],'\t',data[12]
                   output.writelines(string)
    print 'done ^_^'
    return 0

dic=dicbuild(annofile)
writeanno(queryfile)
annofile.close()
queryfile.close()
output.close()
#raw_input()
"""
