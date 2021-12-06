require 'openssl'
require 'base64'

# string = 'JDiLOoP3iIY='
string = 'U2FsdGVkX1/WxiJIr4MPE1WnT3Kb8VExq6ZuuUlHMowcVGpWUNGv85Qj2RhDbM1fU/UCeWAiSaE='

def decrypt(cpass)
  cipher = OpenSSL::Cipher::Cipher.new("des-ede3")
  cipher.decrypt
  # cipher.key = "37,19,88,164,71,3,227,30,19,174,45,84,23,253,149,108,12,107,16,192,98,22,179,200".split(',').map { |x| x.to_i }.pack('c*')
  # cipher.iv = "47,108,239,71,33,98,177,13".split(',').map { |x| x.to_i }.pack('c*')
  cipher.key = "113,181,3,5,176,208,105,37,84,196,6,97,170,46,52,171,189,114,126,134,89,61,52,145".split(',').map { |x| x.to_i }.pack('c*')
  cipher.iv = "198,137,244,176,70,244,36,248".split(',').map { |x| x.to_i }.pack('c*')
  return cipher.update(Base64.decode64(cpass)) + cipher.final
end

decrypted = decrypt(string)

puts "decrypted string: #{decrypted}"
