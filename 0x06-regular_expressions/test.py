lis = ['6-phone_number.rb','7-OMG_WHY_ARE_YOU_SHOUTING.rb']
for i in lis:
    with open(i,'w') as file:
        file.write("#!/usr/bin/env ruby\n")
        file.write("puts ARGV[0].scan(//).join\n\n")
