# This function matches the predictions from different systems and writes the matches and reports the match percentage

import sys
import pandas as pd
file1 = sys.argv[1]

df = pd.read_excel(file1, sheet_name='verified')
total=0
matched=0
matched_results = []
for i,ele in enumerate(df['predicted']):
	elements1 = [j for j in ele.split('\n') if len(j)!=0]
	elements2 = [k for k in df['verified'][i].split('\n') if len(k)!=0]
	tags1 = [ele1.split(':')[0] for ele1 in elements1]
	tags2 = [ele1.split(':')[0] for ele1 in elements2]
	
	phrases1 = [':'.join(ele1.split(':')[1:]) for ele1 in elements1]

	temp=''
	for j,ele1 in enumerate(tags1):
		if ele1!=tags2[j]:
			continue
		temp=temp+ele1+': '+ phrases1[j]+'\n'
		matched+=1
	matched_results.append(temp)
	total+= len(tags1)
df['matched']=matched_results
df.to_excel(file1, sheet_name='verified')
print ("{}% of the tags match for both the prediction systems".format(round(matched*1.0/total*100),2))
