import wx
import template
import mysql.connector
conn = mysql.connector.connect(host="localhost",port=3306,user="root",password="",database="kalori")
cursor=conn.cursor() 
from datetime import date

class frame_login(template.Frame_Login):
  def __init__(self, parent):
    template.Frame_Login.__init__(self,parent)

  def function_Login(self, event):
    username = self.username_login_input.GetValue()
    password = self.password_login_input.GetValue()
    cursor.execute("SELECT * FROM akun WHERE username = '{}' and password = '{}'".format(
      username,password
    ))

    result = cursor.fetchall()
    if result != []:
      aplikasi = frame_aplikasi(None,result[0][0])
      login.Destroy()
      aplikasi.Show()

      return True
    else:
      wx.MessageBox("username atau password yang anda masukan salah!")
      return False


  def function_registrasi(self, event):
    username = self.username_registrasi_input.GetValue()
    password = self.password_registrasi_input.GetValue()
    
    if username != "" and password != "":
      cursor.execute("INSERT INTO akun VALUES(0,'{}','{}','')".format(
        username,password
      ))
      conn.commit()
      self.username_registrasi_input.SetValue("")
      self.password_registrasi_input.SetValue("")
      wx.MessageBox("Registrasi Berhasil Silahkan Melakukan Login")
      return True
    
    else:
      wx.MessageBox("Semua Form Harus Terisi ! ")
      return False
  
class frame_aplikasi(template.Frame_Aplikasi):
  def __init__(self, parent,id):
    template.Frame_Aplikasi.__init__(self,parent)
    self.id = id
    self.tabel_riwayat.SetColLabelValue(0,"asupan : waktu tambah : keterangan")
    self.tabel_riwayat.SetColSize(0,250)
    cursor.execute("SELECT riwayat FROM akun WHERE id = {}".format(self.id))
    riwayat = (cursor.fetchall()[0][0])
    tabel_riwayat = []
    row = ""
    for char in riwayat:
      if char == "\n":
        tabel_riwayat.append(row)
        row = ""
      else:
        row += char
    for index_row,row in enumerate(tabel_riwayat):
      self.tabel_riwayat.AppendRows(1)
      self.tabel_riwayat.SetCellValue(index_row,0,row)

  def function_tambah_kalori(self, event):
    jumlah_kalori = self.jumlah_kalori_input.GetValue()
    if jumlah_kalori.isnumeric():
      
      if int(jumlah_kalori) < 2000:
        kualitas = "Kurang"
      
      elif int(jumlah_kalori) >= 2000 and int(jumlah_kalori) <= 2500:
        kualitas = "Baik"
      else:
        kualitas = "Berlebihan"
      

      today = date.today()
      waktu = today.strftime("%d/%m/%Y")
      cursor.execute("SELECT riwayat FROM akun WHERE id = {}".format(self.id))
      riwayat = (cursor.fetchall()[0][0])
      
      riwayat = "kalori = "+str(jumlah_kalori)+"\t:"+waktu+"\t"+kualitas+"\n"+riwayat

      cursor.execute("UPDATE akun SET riwayat = '{}'".format(riwayat))
      conn.commit()
      wx.MessageBox("Berhasil menambahkan kalori")
      self.jumlah_kalori_input.SetValue("")
      while True:
        try:
          self.tabel_riwayat.DeleteRows(0,1)
        except:
          break
      
      cursor.execute("SELECT riwayat FROM akun WHERE id = {}".format(self.id))
      riwayat = (cursor.fetchall()[0][0])
      tabel_riwayat = []
      row = ""
      for char in riwayat:
        if char == "\n":
          tabel_riwayat.append(row)
          row = ""
        else:
          row += char
      for index_row,row in enumerate(tabel_riwayat):
        self.tabel_riwayat.AppendRows(1)
        self.tabel_riwayat.SetCellValue(index_row,0,row)

      return True
    else:
      wx.MessageBox("Input Harus Berupa Integer")
      self.jumlah_kalori_input.SetValue("")
      return False


  def function_tambah_protein(self,event):
    jumlah_protein = self.jumlah_protein_input.GetValue()
    if jumlah_protein.isnumeric():
      
      if int(jumlah_protein) < 46:
        kualitas = "Kurang"
      
      elif int(jumlah_protein) >= 46 and int(jumlah_protein) <= 70:
        kualitas = "Baik"
      else:
        kualitas = "Berlebihan"
      

      today = date.today()
      waktu = today.strftime("%d/%m/%Y")
      cursor.execute("SELECT riwayat FROM akun WHERE id = {}".format(self.id))
      riwayat = (cursor.fetchall()[0][0])
      
      riwayat = "protein = "+str(jumlah_protein)+"\t:"+waktu+"\t"+kualitas+"\n"+riwayat

      cursor.execute("UPDATE akun SET riwayat = '{}'".format(riwayat))
      conn.commit()
      wx.MessageBox("Berhasil menambahkan protein")
      self.jumlah_protein_input.SetValue("")
      while True:
        try:
          self.tabel_riwayat.DeleteRows(0,1)
        except:
          break
      
      cursor.execute("SELECT riwayat FROM akun WHERE id = {}".format(self.id))
      riwayat = (cursor.fetchall()[0][0])
      tabel_riwayat = []
      row = ""
      for char in riwayat:
        if char == "\n":
          tabel_riwayat.append(row)
          row = ""
        else:
          row += char
      for index_row,row in enumerate(tabel_riwayat):
        self.tabel_riwayat.AppendRows(1)
        self.tabel_riwayat.SetCellValue(index_row,0,row)

      return True
    else:
      wx.MessageBox("Input Harus Berupa Integer")
      self.jumlah_protein_input.SetValue("")
      return False

  


  
myApp = wx.App()
login = frame_login(None)
login.Show()


myApp.MainLoop()