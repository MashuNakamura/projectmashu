def arithmetic_arranger(input, input2 = False):
  nilai:list[list[str]] = []
  value = 0
  spasi = "    "
  line_satu = ""
  line_dua = ""
  line_tiga = ""
  line_empat = ""
  if len(input) > 5:
      return "Error: Too many problems."
  for dataloop in input:
      splitting = dataloop.split()
      nilai.append(splitting)

  nilai_len = len(nilai)
  for i in range(nilai_len):
      convertint = []
      varnum = []
      proses = ""
      for list2 in range (len(nilai[i])):
          proses2 = nilai[i][list2]
          proses2.strip()
          if proses2.isdigit() is True:
              if len(proses2) > 4:
                  return "Error: Numbers cannot be more than four digits."
              varnum.append(len(proses2))
              convertint.append(int(proses2))
          elif proses2 == "+":
              proses = "+"
          elif proses2 == "-":
              proses = "-"
          elif proses2 == "/" or proses2 == "x":
              return "Error: Operator must be '+' or '-'."
          else:
              return "Error: Numbers must only contain digits."
      longest=0

      for number in varnum:
          if number > longest:
              longest = number
      for i in range(len(convertint)):
          if i == len(convertint) - 1:
              if proses == "+":
                  value = convertint[0] + convertint[1]
              else:
                  value = convertint[0] - convertint[1]
              panjang_number = len(str(value))
              line_empat += " " * (longest + 2 - panjang_number) + str(value) + spasi
              line_dua += proses + " " + " " * (longest - varnum[i]) + str(convertint[i]) + spasi
          else:
              line_satu += " " * (longest - varnum[i]+2) + str(convertint[i]) + spasi
      line_tiga += "-" * (longest + 2) + spasi
      hasil = line_satu.rstrip() + "\n" + line_dua.rstrip() + "\n" + line_tiga.rstrip()
      if input2 == True:
          hasil += "\n" + line_empat.rstrip()
  return hasil.rstrip()
if __name__ == "__main__":
    print(arithmetic_arranger(['100 + 20', '200 - 10', '100 + 25', '133 + 12'], True))