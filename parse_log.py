import pstats
import sys

#o_file= sys.argv[1] if len(sys.argv)>1 else out.

#print(n_lines)
p = pstats.Stats('log_profile.txt')
#p.sort_stats('cumulative').print_stats(n_lines)
p.sort_stats('cumulative').print_stats()
