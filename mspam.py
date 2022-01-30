import smtplib as root
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
 
def send_mail():
    login = input( 'Mail: ' )
    password = input( 'Password: ' )
    url = "smtp." + input( 'URL: smtp.' )
    number = int( input( 'Msg value: ' ) )
    toaddr = input( 'Whom: ' )
    topic = input( 'Subject: ' )
    message = input( 'Msg: ' )
 
    for value in range( number ):
        msg = MIMEMultipart()
 
        msg[ 'Subject' ] = topic
        msg[ 'From' ] = login
        body = message
 
        msg.attach( MIMEText( body, 'plain' ) )
 
        server = root.SMTP_SSL( url, 465 )
        server.login( login, password )
        server.sendmail( login, toaddr, msg.as_string() )

        value+=1
        print(f"sus: {value}")