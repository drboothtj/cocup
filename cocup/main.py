'''
main routine for CoCuP
'''

from cocup.parser import parser
from cocup.builder import scaffold

def main():
  args = parser.parse_args()
  scaffold(args.project_name)
  


  #make the scaffold directories
  #populate directories

if __name__ == "__main__":
    main()



# make directories

#add template files
