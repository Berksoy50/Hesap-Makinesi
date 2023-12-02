while  True... : 
 print("--"*20)
 print("Toplama işlemi için + tuşuna basın ")
 print("Çıakrma işlemi için - tuşuna basın ")
 print("Çarpma işlemi için * tuşuna basın ")
 print("Bölme işlemi için / tuşuna basın ")
 print("Üssü işlemi için ** tuşuna basın ")
 print("Karekök işlemi için 6 tuşuna basınız")
 print("Çıkış yapmak için q ya da Q basın")
 print("--"*20)
 
 Process=input("Seçtiğiniz istediniz işlem nedir: ")
 print("--"*20)
 if Process == "+" :
  Number1=float(input("1.Sayıyı girin: "))
  Number2=float(input("2.Sayıyı girin: "))
  Total=Number1+Number2
  print("--"*20)
  print(f"Toplama işleminizin sonucu {Total}")

  print("--"*20)
 elif Process == "-" :
  Number1=float(input("1.Sayıyı girin: "))
  Number2=float(input("2.Sayıyı girin: "))
  Exrapcet=Number1-Number2
  print("--"*20)
  print(f"Çıkarma işleminizin sonucu {Exrapcet}")

  print("--"*20)
 elif Process == "*" :
  Number1=float(input("1.Sayıyı girin: "))
  Number2=float(input("2.Sayıyı girin: "))
  İmpacth=Number1*Number2
  print("--"*20)
  print(f"Çarpma işleminizin sonucu {İmpacth}")

  print("--"*20)
 elif Process == "/" :
  Number1=float(input("1.Sayıyı girin: "))
  Number2=float(input("2.Sayıyı girin: "))
  Divide=Number1/Number2
  print("--"*20)
  print(f"Çıkarma işleminizin sonucu {Divide}")

  print("--"*20)
 elif Process == "**" :
  Number1=float(input("Sayının tabanını girin: "))
  Number2=float(input("Sayının n kuvvetini girin: "))
  Base=Number1-Number2
  print("--"*20)
  print(f"Üslü işleminizin sonucu {Base}")

  print("--"*20)
 elif Process == "6" :
  import math
  Number=float(input("Karekökten çıkarmak istediğiniz sayıyı girin: "))
  Sqaretoo=math.sqrt(Number)
  print("--"*20)
  print(f"Karekökten çıkan sonuç {Sqaretoo}")

 else :
  Process == "q" and Process == "Q" 
  print("Hesap makinesinden ayrılıyor...")
  break
