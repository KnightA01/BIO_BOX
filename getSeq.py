
import gzip


line = ''
seq_list = [] #储存序列
score_list= [] #储存得分

with gzip.open('L:/Creation/melon-BZR1-3-bHLH/BZR1-3-1_FKDL210116444-1a_1.fq.gz', 'r') as f1:
    while f1.tell() != 4176912231:
        line = f1.readline().decode(encoding = 'utf-8') 
        if line[:1:] == '#': #写入序列
            score_list.append(line)
        else :
            seq_list.append(line)
            
        if (len(seq_list) == 10) && (len(score_list) == 10): # 写入文件并清空序列
            with open('L:/Creation/melon-BZR1-3-bHLH/BZR1-3-1_FKDL210116444-1a_1.fasta'), open('L:/Creation/melon-BZR1-3-bHLH/BZR1-3-1_FKDL210116444-1a_1.txt') as seq_file, score_file:
                seq_file.write(seq_list)
                score_file.write(score_list)
                seq_list = []
                score_list =[]
