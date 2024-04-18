
"""
Problem: Codeland Username Validation
https://coderbyte.com/results/limedosa:Codeland%20Username%20Validation:Python3
"""
# linda = 'jfndjkcnjc_!'
def CodelandUsernameValidation(strParam):

  # code goes here
  length = bool(len(strParam) >= 4 and len(strParam)<=25)
  letter = bool(ord(strParam[0].lower())>= 97 and ord(strParam[0].lower()) <=122 )
  end = bool(strParam[len(strParam)-1] != '_')
  return letter & length & end
# print(CodelandUsernameValidation(linda))