import pywaves as pw

with open("input.txt", "r") as f:    #Input file path
      for line in f:

                  #Get mnemonic and myAddress from line
         mnemonic = line.rstrip('\n')
         myAddress = pw.Address(seed=(mnemonic))

                  #Get keypair and seed
         keypair = str('Address: ' + str(myAddress.address) + ' | PrivateKey: ' + str(myAddress.privateKey) + ' | Seed: ' + str(myAddress.seed) + '\n')
         print(keypair)

         with open("output.txt", "a") as i:
            i.write(keypair)
