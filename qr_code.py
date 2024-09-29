import qrcode
upi_id = input("Enter UPI ID = ")


#upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

phonepay_url = f'upi://pay?pa={upi_id}&pn=Recipie%nt%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipie%nt%20Name&mc=1234'
googlepay_url = f'upi://pay?pa={upi_id}&pn=Recipie%nt%20Name&mc=1234'

phonepay_qr = qrcode.make(phonepay_url)
paytm_qr = qrcode.make(paytm_url)
googlepay_qr = qrcode.make(googlepay_url)

phonepay_qr.save('phonepay_qr.png')
paytm_qr.save('paytm_qr.png')
googlepay_qr.save('googlepay_qr.png')

phonepay_qr.show()
paytm_qr.show()
googlepay_qr.show()