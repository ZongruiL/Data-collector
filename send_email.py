from email.mime.text import MIMEText
import smtplib
def send_email(email,height, average_height, weight, average_weight, count):
	from_email = "zongruiliu1999@gmail.com"
	from_password = "liuzongrui20"
	to_email = email
	BMI = round((int(weight)/(int(height)/100*(int(height)/100))),1)
	subject = "Height data"
	if BMI<18.5:
		message = "Hey there, Within total <strong>%s</strong> people, your height is <strong>%s</strong>cm. Average height of all is <strong>%s</strong>cm.\n Your weight is <strong>%s</strong>kg. Average weight of all is <strong>%s</strong>kg.\n Your BMI is <strong>%s</strong>, which is underweight" % (count, height,average_height, weight, average_weight, BMI)
	if BMI>=18.5 and BMI<=24.9:
		message = "Hey there, Within total <strong>%s</strong> people, your height is <strong>%s</strong>cm. Average height of all is <strong>%s</strong>cm.\n Your weight is <strong>%s</strong>kg. Average weight of all is <strong>%s</strong>kg.\n Your BMI is <strong>%s</strong>, which is healthy" % (count, height,average_height, weight, average_weight, BMI)
	if BMI>=25.0 and BMI<=29.9:
		message = "Hey there, Within total <strong>%s</strong> people, your height is <strong>%s</strong>cm. Average height of all is <strong>%s</strong>cm.\n Your weight is <strong>%s</strong>kg. Average weight of all is <strong>%s</strong>kg.\n Your BMI is <strong>%s</strong>, which is overweight" % (count, height,average_height, weight, average_weight, BMI)
	if BMI>30:
		message = "Hey there, Within total <strong>%s</strong> people, your height is <strong>%s</strong>cm. Average height of all is <strong>%s</strong>cm.\n Your weight is <strong>%s</strong>kg. Average weight of all is <strong>%s</strong>kg.\n Your BMI is <strong>%s</strong>, which is obsese" % (count, height,average_height, weight, average_weight, BMI)
	
	msg = MIMEText(message, 'html')
	msg['Subject'] = subject
	msg['To'] = to_email
	msg['From'] = from_email

	gmail = smtplib.SMTP('smtp.gmail.com',587)
	gmail.ehlo()
	gmail.starttls()
	gmail.login(from_email, from_password)
	gmail.send_message(msg)