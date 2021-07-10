#Öncelikle kullanıcıdan bir internet adresi girmesini istiyoruz
url = input("Lütfen ulaşmak istediğiniz sitenin adresini yazın: ")

#Şimdi de bu adresin bulunamadığı konusunda kullanıcıyı bilgilendiriyoruz
print("Hata! Google Chrome", url, "sitesini bulamadı")

#Şimdi de bu adresin bulunamadığı konusunda kullanıcıyı bilgilendiriyoruz
print("Hata! Google Chrome", "'" + url + "'", "sitesini bulamadı")

print("Hata! Google Chrome '" + url + "' sitesini bulamadı")

#Şimdi de bu adresin bulunamadığı konusunda kullanıcıyı bilgilendiriyoruz
print("Hata! Google Chrome {} sitesini bulamadı".format(url))

print("Hata! Google Chrome '{}' sitesini bulamadı".format(url))
