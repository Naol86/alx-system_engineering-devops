lis = ['0-simply_match_school.rb',"1-repetition_token_0.rb",'2-repetition_token_1.rb','3-repetition_token_2.rb','4-repetition_token_3.rb','5-beginning_and_end.rb']
for i in lis:
    with open(i,'w') as file:
        file.write("#!/usr/bin/env ruby\n")
        file.write("puts ARGV[0].scan(//).join\n\n")
