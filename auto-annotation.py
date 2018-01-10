## auto annotation ##
## 2016-01-23 ## 
## zhangfei ##
## Run in Command Line Model, Give the input and output path you want ##
## reconsitution: 2017-04-19 ##
## update: 2018-01-02 ##
## ADD KEGG/EC KO AND GO information ##
## update: 2018-01-10 ##
## ADD TF and Arabidopsis alias information ##
## Load library and output result to a identified address ##

import sys

## Part1: load library and dic build ##
FH_anno = open("./library/Zmays_284_5b+.annotation_info.txt", 'r')
FH_TF = open("./library/Zma_TF_list", 'r')
FH_zma = open("./library/ZmB73_5a_gene_descriptiors.txt", 'r')
FH_zma2 = open("./library/zma_function.txt", 'r')

FH_query = open(sys.argv[1], 'r')
FH_output = open(sys.argv[2], 'a')

def anno_dicbuild(fh):
    anno_dic = {}
    for line in fh:
        line = line.strip('\n')
	line = line.split('\t')
        if anno_dic.get(line[1]) is None:
            line[10] = line[10].split('.')[0]
	    anno_dic[line[1]] = [line[1], line[7], line[8], line[9], line[10], line[11], line[12]]
    fh.close()
    return anno_dic

def TF_dicbuild(fh):
    dic = {}
    for line in fh:
        line = line.strip('\r\n')
        line = line.split('\t')
        if dic.get(line[1]) is None:
            dic[line[1]] = line[2]
    fh.close()
    return dic

def zma_dicbuild(fh):
    dic = {}
    for line in fh:
        line = line.strip('\r\n')
        line = line.split('\t')
        if dic.get(line[0]) is None:
            dic[line[0]] = [line[2], line[3]]
    fh.close()
    return dic

def zma2_dicbuild(fh):
    dic = {}
    for line in fh:
        line = line.strip('\r\n')
        line = line.split('\t')
        if dic.get(line[0]) is None:
            dic[line[0]] = [line[1], line[2], line[4], line[5], line[6]]
    fh.close()
    return dic

anno_dic = anno_dicbuild(FH_anno)
TF_dic = TF_dicbuild(FH_TF)
zma_dic = zma_dicbuild(FH_zma)
zma2_dic = zma2_dicbuild(FH_zma2)

## Part2: Combine data ##
## GD = Gene_description ##
dic_combine = {}
for key in anno_dic.keys():
    GD = anno_dic[key]
    if TF_dic.get(key) is not None:
        GD = GD + [TF_dic[key]]
    else:
        GD = GD + ['-']
    if zma_dic.get(key) is not None:
        GD = GD + zma_dic[key]
    else:
        GD = GD + ['-', '-']
    if zma2_dic.get(key) is not None:
        GD = GD + zma2_dic[key]
    else:
        GD = GD + ['-', '-', '-', '-', '-']

    GD = GD + ['-']
    ## fill alter name
    if GD[10] != '-':
        GD[15] = GD[10]
    elif GD[5] != '':
        GD[15] = GD[5] + '(Ara)'
    else:
        GD[15] = GD[0]
    GD = [GD[0], GD[15], GD[8], GD[12], GD[13], GD[14], GD[10], GD[11], GD[9], GD[4], GD[5], GD[6], GD[7], GD[1], GD[2], GD[3]]
    dic_combine[key] = GD

## Output ##
output_title = ['GeneSymbol', 'altName', 'NCBI_Accession', 'Chr', 'Start', 'End', 'Zma_alias', 'Zma_fullname', 'Zma_description', 'Ara_ortholog', 'Ara_alias', 'Annotation', 'TF', 'EC', 'KO', 'GO']
FH_output.writelines('\t'.join(output_title))
FH_output.writelines('\n')

for line in FH_query:
    line = line.strip('\r\n')
    if dic_combine.get(line) is not None:
        output = dic_combine[line]
        FH_output.writelines('\t'.join(output))
        FH_output.writelines('\n')
    else:
        print line, ' is not found!'
        FH_output.writelines(line)
        FH_output.writelines('\n')

"""
output_title = ['LocusName','transcriptName','KEGG/EC', 'KO', 'GO', 'best-hit-in-Arabidopsis','Arabidopsis-defline']
FH_output.writelines('\t'.join(output_title))
FH_output.writelines('\n')




for line in FH_query:
    line = line.strip('\r\n')
    if line[:2] == 'GR':
        transcript = line + '_T01'
        Gene_id = line
	if anno_dic.get(transcript) != None:
            Ara_id = anno_dic[trancript][]
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
		value = [anno_dic[transcript][7], anno_dic[transcript][8], anno_dic[transcript][9], anno_dic[transcript][10], anno_dic[transcript][12]]
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
